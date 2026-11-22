#!/usr/bin/env python3
"""Download the A4 offline assets without importing the Modal helpers.

The official `scripts/download_data.py --offline-only` imports
`cs336_data.modal_utils`, which refuses to import until SUNET_ID is filled in.
For self-study we only need the local assets, so this small helper mirrors the
official download list and writes to the same `local-shared-data/` directory.
"""
from __future__ import annotations

import gzip
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) cs336-study/1.0"
A4 = Path(__file__).resolve().parent.parent / "assignments" / "a4-data" / "assignment4-data"
ROOT = A4 / "local-shared-data"


def fetch(url: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and out.stat().st_size > 0:
        print(f"[skip] {out.relative_to(ROOT)} ({out.stat().st_size / 2**20:.1f} MiB)")
        return
    print(f"[get ] {out.relative_to(ROOT)} <- {url}", flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    tmp = out.with_suffix(out.suffix + ".part")
    with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as f:
        total = int(r.headers.get("Content-Length") or 0)
        done = 0
        while chunk := r.read(1024 * 1024):
            f.write(chunk)
            done += len(chunk)
            if total and done % (64 * 1024 * 1024) < 1024 * 1024:
                print(f"       {done / 2**20:.0f}/{total / 2**20:.0f} MiB", flush=True)
    if total and tmp.stat().st_size != total:
        raise RuntimeError(f"incomplete download: {tmp.name} {tmp.stat().st_size} != {total}")
    tmp.replace(out)
    print(f"[ok  ] {out.relative_to(ROOT)} ({out.stat().st_size / 2**20:.1f} MiB)", flush=True)


def first_cc_path(kind: str) -> str:
    url = f"https://data.commoncrawl.org/crawl-data/CC-MAIN-2026-12/{kind}.paths.gz"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return gzip.decompress(r.read()).decode().splitlines()[0]


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    fetch(
        "https://huggingface.co/datasets/brunborg/cs336-a4/resolve/main/tokenized_paloma_c4_100_domains_validation.bin",
        ROOT / "tokenized_paloma_c4_100_domains_validation.bin",
    )
    for kind, name in [("warc", "example.warc.gz"), ("wet", "example.warc.wet.gz")]:
        path = first_cc_path(kind)
        fetch(f"https://data.commoncrawl.org/{path}", ROOT / "CC" / name)
    for rel, url in [
        ("classifiers/lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"),
        (
            "classifiers/dolma_fasttext_hatespeech_jigsaw_model.bin",
            "https://huggingface.co/allenai/dolma-jigsaw-fasttext-bigrams-hatespeech/resolve/main/model.bin",
        ),
        (
            "classifiers/dolma_fasttext_nsfw_jigsaw_model.bin",
            "https://huggingface.co/allenai/dolma-jigsaw-fasttext-bigrams-nsfw/resolve/main/model.bin",
        ),
    ]:
        fetch(url, ROOT / rel)
    print(f"\nA4 offline assets ready: {ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
