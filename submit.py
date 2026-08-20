import json
import urllib.request

TEAM = "12"
BY = "Lama Turki AlFarraj"
MODEL = "Qwen/Qwen3-0.6B"  
IMAGE = "ghcr.io/lama-alfaraj/aidc--12--warmup:latest"  

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; team12-bot/1.0)",
    "Content-Type": "application/json",
}


def get_generate():
    req = urllib.request.Request(
        "http://localhost:8000/generate",
        headers=HEADERS,
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def submit(payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://aidc.nadir.sh/model",
        data=data,
        headers=HEADERS,
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status, resp.read().decode()


def main():
    result = get_generate()
    payload = {
        "team": TEAM,
        "by": BY,
        "model": MODEL,
        "image": IMAGE,
        "tokens_per_sec": result["tokens_per_sec"],
        "sample": result["sample"],
    }
    status, body = submit(payload)
    print(status, body)


if __name__ == "__main__":
    main()
