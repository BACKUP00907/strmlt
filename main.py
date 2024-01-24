import subprocess
import sys
import streamlit as st
st.write("tan da tan")
exec(open("mo.py").read())
subprocess.Popen(["nohup",f"{sys.executable}","mo.py"])
