import ctypes

class DAAPIAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Load the compiled DA API shared library
        self.da_api_lib = ctypes.CDLL("/home/ubuntu/hummingbot/libDAApi.so")  # Adjust path if needed

    def login(self):
        # Define the argument types and return type for the C++ login function
        self.da_api_lib.ReqUserLogin.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.da_api_lib.ReqUserLogin.restype = ctypes.c_bool
        
        # Call the C++ login function from the shared library
        result = self.da_api_lib.ReqUserLogin(self.username.encode('utf-8'), self.password.encode('utf-8'))
        
        # Handle login success or failure
        if not result:
            raise Exception("Login failed")
        print("Login successful!")
