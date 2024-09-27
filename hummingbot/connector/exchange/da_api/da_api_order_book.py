class DAAPIOrderBook:
    def __init__(self, bids, asks):
        self.bids = bids
        self.asks = asks

    def update_order_book(self, new_bids, new_asks):
        self.bids = new_bids
        self.asks = new_asks

    def print_order_book(self):
        print(f"Bids: {self.bids}")
        print(f"Asks: {self.asks}")
