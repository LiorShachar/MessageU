class ServerError(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(self.code)

    def __str__(self):
        return f'Server Error Code : {self.code}'
