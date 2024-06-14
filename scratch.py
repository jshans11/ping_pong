import requests
import subprocess

# # Global variables to store the server statuses
server1_process = None
server2_process = None

def start_servers():
    global server1_process, server2_process
    server1_process = subprocess.Popen(["python3", "server1.py"])
    server2_process = subprocess.Popen(["python3", "server2.py"])

def stop_servers():
    global server1_process, server2_process
    if server1_process:
        server1_process.terminate()
        server1_process = None
    if server2_process:
        server2_process.terminate()
        server2_process = None