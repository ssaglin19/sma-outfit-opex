"""
InfluxDB Setup Script
======================
Creates the org, bucket, and initial token for the SMA alert system.
Run this ONCE after installing InfluxDB 2.x on your machine.

Prerequisites:
  1. Install InfluxDB 2.x:
     - Windows: https://portal.influxdata.com/downloads/
       Download the .zip, extract, run influxd.exe
     - Or via chocolatey: choco install influxdb2
  2. Start the server: influxd
  3. Run this script: python influxdb_setup.py

This will configure InfluxDB via its API and save the token to .env.
"""

import requests
import sys
import os

INFLUX_URL = "http://localhost:8086"

def check_influxdb():
    """Check if InfluxDB is running."""
    try:
        resp = requests.get(f"{INFLUX_URL}/health", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            print(f"InfluxDB is running: {data.get('name', '?')} v{data.get('version', '?')}")
            return True
    except requests.ConnectionError:
        pass
    print("ERROR: InfluxDB is not running at", INFLUX_URL)
    print("Start it with: influxd")
    return False


def setup_influxdb():
    """Run initial onboarding setup."""
    # Check if already set up
    resp = requests.get(f"{INFLUX_URL}/api/v2/setup")
    if resp.json().get("allowed") is False:
        print("InfluxDB is already set up.")
        # Try to read existing token from .env
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith("INFLUXDB_TOKEN="):
                        token = line.strip().split("=", 1)[1]
                        print(f"Token from .env: {token[:10]}...")
                        return token
        print("No token found in .env. You may need to create one manually in the InfluxDB UI.")
        print(f"Open {INFLUX_URL} in your browser.")
        return None

    # Run onboarding
    print("Setting up InfluxDB for first time...")
    setup_data = {
        "username": "admin",
        "password": "sma-alerts-2026",
        "org": "sma-alerts",
        "bucket": "market_data",
        "retentionPeriodSeconds": 0,  # infinite retention
    }

    resp = requests.post(f"{INFLUX_URL}/api/v2/setup", json=setup_data)
    if resp.status_code != 201:
        print(f"Setup failed: {resp.status_code} — {resp.text}")
        return None

    result = resp.json()
    token = result.get("auth", {}).get("token", "")
    org_id = result.get("org", {}).get("id", "")
    bucket_id = result.get("bucket", {}).get("id", "")

    print(f"Setup complete!")
    print(f"  Org: sma-alerts (ID: {org_id})")
    print(f"  Bucket: market_data (ID: {bucket_id})")
    print(f"  Token: {token[:20]}...")

    # Save token to .env
    save_to_env("INFLUXDB_TOKEN", token)
    save_to_env("INFLUXDB_ORG", "sma-alerts")
    save_to_env("INFLUXDB_URL", INFLUX_URL)

    return token


def save_to_env(key, value):
    """Add or update a key in .env file."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    lines = []
    found = False
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.strip().startswith(f"{key}="):
                    lines.append(f"{key}={value}\n")
                    found = True
                else:
                    lines.append(line)
    if not found:
        lines.append(f"{key}={value}\n")
    with open(env_path, 'w') as f:
        f.writelines(lines)
    print(f"  Saved {key} to .env")


def create_additional_buckets(token):
    """Create buckets for SMA computations and scoring."""
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
    }

    # Get org ID
    resp = requests.get(f"{INFLUX_URL}/api/v2/orgs", headers=headers)
    orgs = resp.json().get("orgs", [])
    org_id = None
    for org in orgs:
        if org["name"] == "sma-alerts":
            org_id = org["id"]
            break

    if not org_id:
        print("ERROR: Could not find org 'sma-alerts'")
        return

    buckets_to_create = [
        {"name": "sma_values", "description": "Pre-computed SMA values for all tickers/timeframes"},
        {"name": "penny_matches", "description": "OHLC-to-SMA exact penny matches"},
        {"name": "scoring", "description": "Aggregated scoring by outfit and ticker"},
    ]

    for bucket_def in buckets_to_create:
        data = {
            "orgID": org_id,
            "name": bucket_def["name"],
            "description": bucket_def["description"],
            "retentionRules": [],  # infinite retention
        }
        resp = requests.post(f"{INFLUX_URL}/api/v2/buckets", headers=headers, json=data)
        if resp.status_code == 201:
            print(f"  Created bucket: {bucket_def['name']}")
        elif resp.status_code == 422:
            print(f"  Bucket already exists: {bucket_def['name']}")
        else:
            print(f"  Failed to create {bucket_def['name']}: {resp.status_code} — {resp.text[:200]}")


if __name__ == "__main__":
    if not check_influxdb():
        sys.exit(1)

    token = setup_influxdb()
    if token:
        create_additional_buckets(token)
        print("\nDone! InfluxDB is ready.")
        print(f"  UI: {INFLUX_URL}")
        print(f"  Username: admin")
        print(f"  Password: sma-alerts-2026")
    else:
        print("\nSetup incomplete. Check the InfluxDB UI or re-run this script.")
