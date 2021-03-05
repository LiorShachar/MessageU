import socket
import sys
from threading import Thread
from time import sleep
from RequestHandler import RequestHandler

class Server:
    def __init__(self):
        print("Server init")
        self.isListening = False

    def load_config(self):
        pass

    def listen(self, ip: str, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            clients = []
            print(f"{ip} Listening on port {port}")
            s.bind((ip, port))
            s.listen()
            handler = RequestHandler()
            self.isListening = True
            while self.isListening:
                clientSocket, clientEndpoint = s.accept()
                print(f"new client joined")
                clients.append((clientSocket, clientEndpoint))
                handler.handle_client(clientSocket, clientEndpoint)

    def close():
        pass

def main():
    server = Server()
    server.listen('127.0.0.1',50500);

if __name__ == "__main__":
    main()