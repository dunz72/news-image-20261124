#!/usr/bin/env python3
"""Deliver the finished front page to the grader's output directory.

entry.png already lives in this repository, fully drawn. This script
only moves those exact bytes into the directory the grader reads.

Standard library only. No third-party packages, no fonts, no network
access, no clock, no randomness: the grader's sandbox has no Pillow,
so every import below must stay inside the standard library.
"""

import hashlib
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
BYTE_LIMIT = 1_048_576
IMAGE_NAME = "entry.png"
EXPECTED_SIZE = (1024, 1024)


def digest_hex(blob):
    return hashlib.sha256(blob).hexdigest()


def _candidate_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yield os.path.join(script_dir, IMAGE_NAME)
    bot_home = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_home:
        yield os.path.join(bot_home, IMAGE_NAME)


def locate_image():
    for path in _candidate_paths():
        if os.path.isfile(path):
            return path
    searched = ", ".join(_candidate_paths())
    raise FileNotFoundError("could not find %s in: %s" % (IMAGE_NAME, searched))


def _check_signature(blob, path):
    if blob[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise ValueError("%s: bad PNG signature" % path)


def _check_ihdr(blob, path):
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        raise ValueError("%s: missing IHDR chunk" % path)
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if (width, height) != EXPECTED_SIZE:
        raise ValueError(
            "%s: expected %dx%d, got %dx%d"
            % (path, EXPECTED_SIZE[0], EXPECTED_SIZE[1], width, height)
        )


def _check_size(blob, path):
    if len(blob) > BYTE_LIMIT:
        raise ValueError(
            "%s: %d bytes over the %d-byte limit" % (path, len(blob), BYTE_LIMIT)
        )


def _check_trailer(blob, path):
    if len(blob) < 12 or blob[-8:-4] != b"IEND":
        raise ValueError("%s: missing IEND chunk" % path)


def load_image(path):
    with open(path, "rb") as stream:
        blob = stream.read()
    for check in (_check_signature, _check_ihdr, _check_size, _check_trailer):
        check(blob, path)
    return blob


def place_image(blob):
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, IMAGE_NAME)
    with open(target, "wb") as stream:
        stream.write(blob)
    with open(target, "rb") as stream:
        placed = stream.read()
    if digest_hex(placed) != digest_hex(blob):
        raise ValueError("%s: copy differs from source" % target)
    return target


def run():
    source = locate_image()
    blob = load_image(source)
    target = place_image(blob)
    print(
        "wrote %s (%d bytes, sha256 %s)"
        % (target, len(blob), digest_hex(blob)[:16])
    )
    return 0


if __name__ == "__main__":
    sys.exit(run())
