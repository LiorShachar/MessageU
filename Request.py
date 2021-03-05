import struct

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

