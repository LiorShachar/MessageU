import socket
import sys




class Server:
    def __init__(self):
        print("Server init")

    def listen(self,ip:str,port:int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"{ip} Listening on port {port}")
            s.
            while 1:



    def close():
        pass






def main():
    server = Server()
    server.listen('127.0.0.1',50500);

if __name__ == "__main__":
    main()