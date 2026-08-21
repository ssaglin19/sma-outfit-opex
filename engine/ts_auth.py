"""
TradeStation OAuth 2.0 — One-time authorization to get refresh token.

Run this once:
    python ts_auth.py

It will:
1. Start a local server on port 3000
2. Open TradeStation login in your browser
3. You log in and authorize
4. It catches the callback, exchanges for tokens
5. Saves refresh_token to .env
"""

import http.server
import urllib.parse
import webbrowser
import requests
import os
import sys

# Load from .env
def load_env():
    env = {}
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()
    return env

env = load_env()
CLIENT_ID = env.get('TS_CLIENT_ID', '')
CLIENT_SECRET = env.get('TS_CLIENT_SECRET', '')
REDIRECT_URI = 'http://localhost:8080'
AUTH_URL = 'https://signin.tradestation.com/authorize'
TOKEN_URL = 'https://signin.tradestation.com/oauth/token'

if not CLIENT_ID or not CLIENT_SECRET:
    print("ERROR: TS_CLIENT_ID and TS_CLIENT_SECRET must be set in .env")
    sys.exit(1)


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    auth_code = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if 'code' in params:
            CallbackHandler.auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h2>Authorization successful. You can close this tab.</h2></body></html>')
        elif 'error' in params:
            error = params.get('error', ['unknown'])[0]
            desc = params.get('error_description', [''])[0]
            self.send_response(400)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<html><body><h2>Error: {error}</h2><p>{desc}</p></body></html>'.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # suppress request logs


def main():
    # Build authorization URL
    auth_params = urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'audience': 'https://api.tradestation.com',
        'scope': 'openid profile offline_access MarketData ReadAccount',
    })
    full_auth_url = f"{AUTH_URL}?{auth_params}"

    print("=" * 60)
    print("  TradeStation OAuth Setup")
    print("=" * 60)
    print(f"\n  Opening browser for authorization...")
    print(f"  If it doesn't open, go to:\n")
    print(f"  {full_auth_url}\n")

    webbrowser.open(full_auth_url)

    # Start local server to catch callback
    server = http.server.HTTPServer(('localhost', 8080), CallbackHandler)
    print("  Waiting for callback on http://localhost:8080 ...")

    while CallbackHandler.auth_code is None:
        server.handle_request()

    auth_code = CallbackHandler.auth_code
    print(f"\n  Got authorization code: {auth_code[:10]}...")

    # Exchange code for tokens
    print("  Exchanging for tokens...")
    resp = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
    })

    if resp.status_code != 200:
        print(f"\n  ERROR: Token exchange failed ({resp.status_code})")
        print(f"  {resp.text}")
        sys.exit(1)

    tokens = resp.json()
    access_token = tokens.get('access_token', '')
    refresh_token = tokens.get('refresh_token', '')

    if not refresh_token:
        print(f"\n  ERROR: No refresh_token in response")
        print(f"  Response: {tokens}")
        sys.exit(1)

    # Save refresh token to .env
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    with open(env_path, 'r') as f:
        content = f.read()

    if 'TS_REFRESH_TOKEN' in content:
        # Replace existing
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('TS_REFRESH_TOKEN'):
                new_lines.append(f'TS_REFRESH_TOKEN={refresh_token}')
            else:
                new_lines.append(line)
        content = '\n'.join(new_lines)
    else:
        content = content.rstrip() + f'\nTS_REFRESH_TOKEN={refresh_token}\n'

    with open(env_path, 'w') as f:
        f.write(content)

    print(f"\n  SUCCESS!")
    print(f"  Access token:  {access_token[:20]}...")
    print(f"  Refresh token: {refresh_token[:20]}...")
    print(f"  Saved to .env")
    print(f"\n  You can now run the alert engine.")


if __name__ == '__main__':
    main()
