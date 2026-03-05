import hashlib


def generate_hash(text):

    encoded_text = text.encode()

    hash_object = hashlib.sha256(encoded_text)

    return hash_object.hexdigest()