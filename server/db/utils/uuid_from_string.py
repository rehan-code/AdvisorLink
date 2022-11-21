import uuid
import hashlib
import random

# Generates a random uuid based on the input string.


def uuid_from_str(string):
    rd = random.Random()
    rd.seed(int(hashlib.sha256(string.encode('utf-8')).hexdigest(), 16) * (10 ** 16 + 1))
    return uuid.UUID(int=rd.getrandbits(128))
