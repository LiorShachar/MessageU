import struct

HEADER_SIZE = 22
REQ_CODE_REGISTER = 100
REQ_CODE_USER_LIST = 101
REQ_CODE_PUBLIC_KEY = 102
REQ_CODE_SEND_MESSAGE = 103


class RequestHeader:
    def __init__(self):
        self.clientId = []
        self.version = 0
        self.code = 0
        self.payloadSize = 0

    def deserialize(self, payload_bytes):
        header_tuples = struct.unpack('!16sBBI', payload_bytes)
        self.clientId = header_tuples[0]
        self.version = header_tuples[1]
        self.code = header_tuples[2]
        self.payloadSize = header_tuples[3]


class RegisterRequestContent:

    def __init__(self):
        self.name = ''
        self.public_key = []

    def deserialize(self, payload_bytes):
        req_tuples = struct.unpack('!255s32s', payload_bytes)
        self.name = req_tuples[0]
        self.public_key = req_tuples[1]


class PublicKeyRequestContent:

    def __init__(self):
        self.other_client_id = []

    def deserialize(self, payload_bytes):
        req_tuples = struct.unpack('!16s', payload_bytes)
        self.other_client_id = req_tuples[0]


class SendMsgRequestContent:

    def __init__(self):
        self.dest_client_id = []
        self.message_type = 0x0
        self.content_size = 0

    def deserialize(self, payload_bytes):
        req_tuples = struct.unpack('!16sBI', payload_bytes)
        self.dest_client_id = req_tuples[0]
        self.message_type = req_tuples[1]
        self.content_size = req_tuples[2]
