#!/usr/bin/env python3
"""Deploy skunara-public to Vercel production via the vercel MCP CLI.
First deployment: uploads files, creates deployment with full file tree."""
import base64, hashlib, json, os, subprocess, sys

ROOT = os.path.expanduser("~/workspace/skunara-public")
DEPLOY_FILES = ["index.html", "styles.css", "app.js", "robots.txt",
                "sitemap.xml", "vercel.json"]

def call_tool(name, args):
    p = subprocess.run(
        ["vercel", "call-tool", "--name", name,
         "--arguments-json", json.dumps(args)],
        capture_output=True, text=True, cwd=ROOT, timeout=300)
    if p.returncode != 0:
        print(f"TOOL {name} FAILED:\n{p.stdout[-2000:]}\n{p.stderr[-2000:]}")
        sys.exit(1)
    return json.loads(p.stdout)

files = []
for rel in DEPLOY_FILES:
    full = os.path.join(ROOT, rel)
    h = hashlib.sha1()
    with open(full, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    files.append({"file": rel, "sha": h.hexdigest(),
                  "size": os.path.getsize(full),
                  "full": full})
print(f"tree: {len(files)} files")

for f in files:
    with open(f["full"], "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    r = call_tool("upload_file", {
        "contentLength": f["size"],
        "xVercelDigest": f["sha"],
        "requestBody": b64,
    })
    print(f"uploaded {f['file']}: {json.dumps(r)[:160]}")

refs = [{"file": f["file"], "sha": f["sha"], "size": f["size"]} for f in files]
r = call_tool("create_deployment", {
    "requestBody": {
        "name": "skunara",
        "target": "production",
        "files": refs,
    },
})
dep = r.get("deployment") or r
print(json.dumps(dep, indent=1)[:1500])
print("URL:", dep.get("url"))
print("ID:", dep.get("id"))
