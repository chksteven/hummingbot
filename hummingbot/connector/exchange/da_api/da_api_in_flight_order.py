class DAAPIInFlightOrder:
    def __init__(self, order_id, symbol, quantity, price, order_type):
        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.order_type = order_type
        self.status = "OPEN"

    def update_status(self, status):
        self.status = status
