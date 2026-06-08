import string
import random

def random_username():
    suffix = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=5)
    )
    return f"user_{suffix}"