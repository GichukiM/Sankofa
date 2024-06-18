# utils.py
def validate_non_empty(value):
    return bool(value and value.strip())

def validate_quantity(value):
    try:
        quantity = int(value)
        return quantity >= 0
    except ValueError:
        return False
