"""Red Panda Hug in the Flower Garden - make.fun cutest-picture-01 entry.

Copies the bundled artwork (entry.png, a JPEG by magic bytes as the
rules allow) to the output directory. Standard library only, no network,
fully deterministic: every run writes the same bytes.
Run locally with: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The artwork is original, generated for this entry.
"""

import os
import shutil

ENTRY = "entry.png"
JPEG_MAGIC = b"\xff\xd8\xff"
# The program copies exactly one file and verifies it; nothing else runs.


def output_dir():
    """Return the writable output directory for this run."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def source_path():
    """Return the path of the bundled artwork next to this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ENTRY)


def verify_jpeg(path):
    """Check the file is a non-empty JPEG by its magic bytes."""
    size = os.path.getsize(path)
    assert size > 0, "output is empty"
    with open(path, "rb") as handle:
        magic = handle.read(3)
    assert magic == JPEG_MAGIC, "output is not a JPEG"
    return size


def main():
    """Copy the bundled artwork to the output directory and verify it."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    dest = os.path.join(out, ENTRY)
    shutil.copyfile(source_path(), dest)
    size = verify_jpeg(dest)
    assert os.path.getsize(dest) == os.path.getsize(source_path())
    print("wrote {} ({} bytes)".format(dest, size))


if __name__ == "__main__":
    main()
