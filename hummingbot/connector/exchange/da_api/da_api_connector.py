import ctypes

class DAAPIConnector:
    def __init__(self):
        # Load the DA API shared library (libDAApi.so)
        self.da_api_lib = ctypes.CDLL("/home/ubuntu/hummingbot/libDAApi.so")

    def login(self, username: str, password: str):
        # Call the login function from the DA API
        self.da_api_lib.ReqUserLogin.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.da_api_lib.ReqUserLogin.restype = ctypes.c_bool
        result = self.da_api_lib.ReqUserLogin(username.encode('utf-8'), password.encode('utf-8'))
        if not result:
            raise Exception("Login failed")
        print("Login successful!")
