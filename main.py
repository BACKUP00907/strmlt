import subprocess
import sys
import streamlit as st
k=open("nohup.out","r") 
st.write("tan da tan",k.read())
subprocess.Popen(["nohup",f"{sys.executable}","mo.py"])
