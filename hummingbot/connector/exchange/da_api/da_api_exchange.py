from .da_api_auth import DAAPIAuth
from .da_api_constants import DAAPIConstants
import ctypes

class DAAPIExchange:
    def __init__(self, username, password):
        self.auth = DAAPIAuth(username, password)
        self.auth.login()

    def place_order(self, symbol, quantity, price, order_type):
        self.auth.da_api_lib.ReqOrderInsert.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int]
        self.auth.da_api_lib.ReqOrderInsert.restype = ctypes.c_bool
        result = self.auth.da_api_lib.ReqOrderInsert(
            symbol.encode('utf-8'),
            ctypes.c_double(quantity),
            ctypes.c_double(price),
            ctypes.c_int(DAAPIConstants.ORDER_TYPES[order_type])
        )
        if not result:
            raise Exception("Order placement failed")
        return result

    def cancel_order(self, order_id):
        self.auth.da_api_lib.ReqOrderCancel.argtypes = [ctypes.c_char_p]
        result = self.auth.da_api_lib.ReqOrderCancel(order_id.encode('utf-8'))
        return result
