import ctypes

class DAAPIUserStreamDataSource:
    def __init__(self, auth):
        self.auth = auth
        self.da_api_lib = ctypes.CDLL("/home/ubuntu/hummingbot/libDAApi.so")

    def listen_for_user_stream(self):
        # Connect to DA API to listen for order updates
        self.da_api_lib.ListenUserStream.argtypes = []
        self.da_api_lib.ListenUserStream.restype = None
        self.da_api_lib.ListenUserStream()
