import hashlib


class HashHelper:
    @staticmethod
    def hash_string(string: str) -> str:
        hash = hashlib.sha512(str(string).encode("utf-8")).hexdigest()
        return hash
