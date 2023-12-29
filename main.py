import subprocess
import sys

subprocess.Popen(["ls"])
subprocess.Popen(["nohup",f"{sys.executable}","mo.py"])