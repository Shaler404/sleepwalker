"""Оригиналы записей сессий на YouTube (YouTube Data API v3).

Настройка один раз:
1. Google Cloud Console: проект, включить YouTube Data API v3, OAuth-клиент типа «Desktop app»,
   скачать JSON в путь youtube.client_secret из local.yaml.
2. pip install google-api-python-client google-auth-oauthlib
3. python harness/youtube.py auth — откроется браузер, войти в аккаунт канала.
4. В local.yaml поставить youtube.enabled: true.

Ограничения API: 100 загрузок в сутки. Пока проект не прошёл аудит Google, всё загруженное
через API становится private — смотреть сможет только владелец канала.

  python harness/youtube.py auth
  python harness/youtube.py upload-pending    догрузить оригиналы, которые не ушли сразу
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def credentials(cfg: dict, interactive: bool = False):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    token = Path(cfg["token"])
    creds = Credentials.from_authorized_user_file(str(token), SCOPES) if token.exists() else None
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token.write_text(creds.to_json(), encoding="utf-8")
    if not creds or not creds.valid:
        if not interactive:
            raise RuntimeError("нет токена YouTube: python harness/youtube.py auth")
        from google_auth_oauthlib.flow import InstalledAppFlow

        creds = InstalledAppFlow.from_client_secrets_file(cfg["client_secret"], SCOPES).run_local_server(port=0)
        token.parent.mkdir(parents=True, exist_ok=True)
        token.write_text(creds.to_json(), encoding="utf-8")
    return creds


def upload(path: Path, title: str, description: str, cfg: dict) -> str:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    yt = build("youtube", "v3", credentials=credentials(cfg))
    body = {
        "snippet": {"title": title[:100], "description": description[:4900], "categoryId": "20"},  # 20 = Gaming
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
    from sw import RAW, local_cfg

    cfg = local_cfg()["youtube"]
    if sys.argv[1:] == ["auth"]:
        credentials(cfg, interactive=True)
        print("ok")
    elif sys.argv[1:] == ["upload-pending"]:
        for meta_path in RAW.glob("*/*/session.json"):
            meta, original = json.loads(meta_path.read_text(encoding="utf-8")), meta_path.with_name("original.mkv")
            if meta.get("youtube") or not original.exists():
                continue
            meta["youtube"] = upload(original, f"{meta['game']} · {meta['kind']} · {meta['id'][:8]}",
                                     f"sleepwalker session {meta['id']}\n{meta.get('summary', '')}", cfg)
            meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
            original.unlink()
            print(meta["id"], "->", meta["youtube"])
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
