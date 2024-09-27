def format_price(price):
    return f"{price:.2f}"

def handle_api_error(error_id, error_msg):
    if error_id != 0:
        raise Exception(f"API Error {error_id}: {error_msg}")
