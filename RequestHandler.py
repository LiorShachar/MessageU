import socket
from Functions import *
from Exceptions import ServerError
from concurrent.futures import ThreadPoolExecutor
from Request import *

# A threaded task manager to handle all the requests and assign them to threads
class RequestHandler:

    def __init__(self):
        self.executor = ThreadPoolExecutor(5)

    def handle_client(self, client_socket: socket, client_end_point):
        header = self.read_header(client_socket)
        if type(header) is RequestHeader:
            #print("Valid Header!")
            self.executor.submit(self.handle_request, header, client_socket)


    def handle_request(self, header : RequestHeader, client_socket: socket):
        print(f"Handling Request Code: {header.code}")
        try:
            if header.code == REQ_CODE_REGISTER:
                print(f"registering New User")
                register_user()
            if header.code == REQ_CODE_USER_LIST:
                print(f"fetching user list For client:")
                get_public_key()
            if header.code == REQ_CODE_PUBLIC_KEY:
                print(f"fetching public key For client:")
                pull_messages()
            if header.code == REQ_CODE_SEND_MESSAGE:
                print(f"sending msg to client:")
                send_message()
        except ServerError:
            self.RespondWithError(code,client_socket)


    def read_header(self, client_socket: socket) -> RequestHeader:
        try:
            print("reading header")
            header_buff = client_socket.recv(HEADER_SIZE)
            print(f"recieved {len(header_buff)} bytes")
            req = RequestHeader()
            req.deserialize(header_buff)
            print(f'Incoming Request: client id:{req.clientId} version: {req.version} code: {req.code} file size: {req.payloadSize}')
            return req
        except Exception:
            return None





