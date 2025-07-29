import os
import sys

windir = os.environ.get("WINDIR")
sys = sys.platform

_dir = os.path.join(windir, "fonts")

print(sys)
print(windir)
print(_dir)