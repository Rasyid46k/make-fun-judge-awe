import os

TEXT = "Far above the sleeping town, the Milky Way spilled across the sky, and the night went so quiet I could hear my own heartbeat slow down."

assert 1 <= len(TEXT) <= 280, "text must be 1-280 characters"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, "entry.txt")
tmp = path + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    f.write(TEXT)
os.replace(tmp, path)
with open(path, encoding="utf-8") as f:
    assert f.read() == TEXT, "entry.txt does not match TEXT"
