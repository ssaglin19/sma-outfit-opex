"""
Vision Queue — background OCR for gap era (2025-08-21 → 2026-08-21)

Priority queue: B/C tiers at 76% precision (1,921 matched+charted) per signature_summary.md
Reads archive/media/*/0.jpg, OCRs MA ladders (MA\\d+) and outfit phrases, writes
archive/analysis/gap_findings_vision.jsonl and enriches gap_index via horizon+inverse.

Usage:
  python engine/src/vision_queue.py              # foreground, 10 samples
  python engine/src/vision_queue.py --all        # all 661 media gap rows
  python engine/src/vision_queue.py --background # fire-and-forget (setsid)

Stdlib + Pillow + pytesseract + tesseract 5.5.3
"""
import os, sys, json, re, pathlib, argparse
from collections import Counter

# Tesseract path for Windows (chocolatey)
TESS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESS_PATH):
    try:
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = TESS_PATH
    except: pass

REPO = pathlib.Path(__file__).resolve().parents[2]
MEDIA_ROOT = REPO / "archive" / "media"
GAP_PATH = REPO / "archive" / "analysis" / "gap_findings.jsonl"
SIG_PATH = REPO / "archive" / "analysis" / "signature_matches.jsonl"
OUT_PATH = REPO / "archive" / "analysis" / "gap_findings_vision.jsonl"

def load_gap():
    with open(GAP_PATH, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def load_signature():
    with open(SIG_PATH, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def priority_queue():
    """1,921 matched+charted ordered by tier B/C first per signature_summary.md"""
    sigs = load_signature()
    # keep only has_media and tighter tier B/C (highest precision) then rest
    scored=[]
    for s in sigs:
        if not s.get("has_media"): continue
        tier=s.get("tightest_tier","")
        prio=0 if tier in ("B_bracket","C_bare_MA") else 1 if tier.startswith("B") or tier.startswith("C") else 2
        scored.append((prio, s))
    scored.sort(key=lambda x: x[0])
    return [s[1] for s in scored]

def ocr_image(path: pathlib.Path) -> str:
    try:
        from PIL import Image
        import pytesseract
        img = Image.open(path)
        # Speed: downscale if huge, grayscale
        if max(img.size) > 1600:
            img.thumbnail((1600,1600))
        return pytesseract.image_to_string(img, config="--psm 6")
    except Exception as e:
        return f"OCR_ERROR: {e}"

MA_RE = re.compile(r"MA\s*(\d+)", re.I)
OUTFIT_RE = re.compile(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+outfit)", re.I)

def extract_fields(text: str) -> dict:
    mas = MA_RE.findall(text)
    outfit = ""
    m = OUTFIT_RE.search(text)
    if m: outfit = m.group(1).strip()
    return {"raw": text[:800], "mas": mas, "outfit_snippet": outfit}

def run(limit: int = 10, all_media: bool = False):
    gaps = load_gap()
    # Filter to gap rows with media
    gap_media = [g for g in gaps if g.get("has_media")]
    if not all_media:
        # Priority by signature, but gap_media is already filtered; take 10 with media and needs_vision
        sample = [g for g in gap_media if g.get("needs_vision")][:limit]
    else:
        sample = gap_media[:limit] if limit else gap_media
    print(f"Vision queue: {len(gap_media)} gap rows with media, processing {len(sample)} (all_media={all_media})")
    out=[]
    for g in sample:
        pid = g.get("post_id")
        media_dir = MEDIA_ROOT / str(pid)
        img = media_dir / "0.jpg"
        if not img.exists():
            out.append({**g, "_vision": {"status":"no_image", "path": str(img)}})
            continue
        txt = ocr_image(img)
        fields = extract_fields(txt)
        # Attach horizon+inverse like gap_index does
        try:
            sys.path.insert(0, str(REPO / "engine" / "src"))
            from adapters.opex import OPEXCalendar
            from adapters.inverse_map import get_inverse_pair
            cal = OPEXCalendar()
            horizon = cal.resolve_event_horizon(g.get("date","")) if g.get("date") else None
            pair = get_inverse_pair(g.get("ticker","")) if g.get("ticker") else None
        except Exception as e:
            horizon = {"error": str(e)}
            pair = None
        out.append({**g, "_vision": {"status":"ocr", "text": fields["raw"][:500], "mas": fields["mas"], "outfit_snippet": fields["outfit_snippet"]}, "_horizon": horizon, "_inverse": pair.__dict__ if pair else None})
        print(f"  {pid} {g.get('ticker')} {g.get('date')} -> mas {fields['mas'][:4]} outfit '{fields['outfit_snippet'][:40]}' -> horizon {horizon.get('event_horizon') if horizon else 'none'}")
    # Append to vision file
    with open(OUT_PATH, "a", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r) + "\n")
    print(f"Wrote {len(out)} rows to {OUT_PATH} (append)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="All 661 media gap rows")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--background", action="store_true", help="Run in background (Windows Start-Process)")
    args = ap.parse_args()
    if args.background:
        import subprocess, sys as sys2
        # Fire-and-forget: re-launch with --all
        subprocess.Popen([sys2.executable, __file__, "--all"], creationflags=0x00000008 if os.name=="nt" else 0)
        print("Vision queue started in background (--all)")
    else:
        run(limit=args.limit, all_media=args.all)

