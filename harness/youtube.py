"""Originals of session recordings on YouTube (YouTube Data API v3).

One-time setup:
1. Google Cloud Console: a project, enable YouTube Data API v3, an OAuth client of type "Desktop app";
   download the JSON to the youtube.client_secret path from local.yaml.
2. pip install google-api-python-client google-auth-oauthlib
3. python harness/youtube.py auth opens a browser. Pick the account that owns the channel
   (Google always asks for the account, so you cannot sign in with another one by accident). At the end
   the command shows the channel the videos will go to.
4. Set youtube.enabled: true in local.yaml.

Videos go to the channel of the signed-in account, not of the account where the Google Cloud project
was created. API limits: 100 uploads a day. Until the project passes Google's audit, everything
uploaded through the API becomes private: only the channel owner can watch it.

  python harness/youtube.py auth              sign in again (e.g. with another account)
  python harness/youtube.py whoami            which channel the videos go to now
  python harness/youtube.py upload-pending    upload the originals that did not go up right away
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# upload: uploading; readonly: only to show which channel the sign-in is tied to
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.readonly"]


def credentials(cfg: dict, interactive: bool = False):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    token = Path(cfg["token"])
    creds = None
    if token.exists() and not interactive:
        granted = json.loads(token.read_text(encoding="utf-8")).get("scopes") or SCOPES[:1]
        creds = Credentials.from_authorized_user_file(str(token), granted)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token.write_text(creds.to_json(), encoding="utf-8")
    if not creds or not creds.valid:
        if not interactive:
            raise RuntimeError("no YouTube token: python harness/youtube.py auth")
        from google_auth_oauthlib.flow import InstalledAppFlow

        flow = InstalledAppFlow.from_client_secrets_file(cfg["client_secret"], SCOPES)
        creds = flow.run_local_server(port=0, prompt="select_account consent")
        token.parent.mkdir(parents=True, exist_ok=True)
        token.write_text(creds.to_json(), encoding="utf-8")
    return creds


def channel(cfg: dict) -> dict | None:
    """The channel the videos currently go to (needs the youtube.readonly scope, granted by auth)."""
    from googleapiclient.discovery import build

    items = build("youtube", "v3", credentials=credentials(cfg)).channels().list(
        part="snippet", mine=True).execute().get("items", [])
    return {"title": items[0]["snippet"]["title"], "id": items[0]["id"],
            "url": f"https://www.youtube.com/channel/{items[0]['id']}"} if items else None


def clean(text: str, limit: int) -> str:
    """YouTube rejects < and > in titles and descriptions ("invalid video description"): session summaries
    write "Out of space -> Revive"."""
    return text.replace("->", "→").replace("<-", "←").replace("<", "‹").replace(">", "›")[:limit]


def upload_pending(cfg: dict, max_n: int = 99) -> list[dict]:
    """Upload the originals that did not go up at the end of their session. Stops at the daily quota.
    `sw.py gc` uploads youtube.uploads_per_gc of them a run and links the pages' footnotes to them."""
    from sw import RAW

    res = []
    for meta_path in sorted(RAW().glob("*/*/session.json")):
        if len([r for r in res if r.get("youtube")]) >= max_n:
            break
        meta, original = json.loads(meta_path.read_text(encoding="utf-8")), meta_path.with_name("original.mkv")
        if meta.get("youtube") or not original.exists():
            continue
        try:
            meta["youtube"] = upload(original, f"{meta['game']} · {meta['id'][:15]}",
                                     f"sleepwalker session {meta['id']}\n{meta.get('summary', '')}", cfg)
        except Exception as ex:
            res.append({"session": meta["id"], "error": str(ex)[:200]})
            if "exceeded" in str(ex) or "uploadLimitExceeded" in str(ex) or "quota" in str(ex).lower():
                break  # the daily limit: try again on a later run
            continue
        st = meta_path.stat()
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
        # still dated at the session's end (gc counts keep_originals_days from it); the original stays for the
        # documenter's clips until gc sees the session documented
        os.utime(meta_path, (st.st_atime, st.st_mtime))
        res.append({"session": meta["id"], "game": meta.get("game"), "youtube": meta["youtube"]})
    return res


def upload(path: Path, title: str, description: str, cfg: dict) -> str:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    yt = build("youtube", "v3", credentials=credentials(cfg))
    body = {
        "snippet": {"title": clean(title, 100), "description": clean(description, 4900), "categoryId": "20"},  # Gaming
        "status": {"privacyStatus": cfg.get("privacy", "private"), "selfDeclaredMadeForKids": False},
    }
    req = yt.videos().insert(part="snippet,status", body=body,
                             media_body=MediaFileUpload(str(path), chunksize=-1, resumable=True))
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    return resp["id"]


def main() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.stdout.reconfigure(encoding="utf-8")
    from sw import RAW, L

    cfg = L()["youtube"]
    if sys.argv[1:] in (["auth"], ["whoami"]):
        if sys.argv[1] == "auth":
            credentials(cfg, interactive=True)
        ch = channel(cfg)
        print(f"Videos go to the channel: {ch['title']} — {ch['url']}" if ch else "This account has no YouTube channel")
    elif sys.argv[1:2] == ["upload-pending"]:
        for r in upload_pending(cfg, int(sys.argv[2]) if len(sys.argv) > 2 else 99):
            print(r)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
