import datetime
import kudo
import hashlib

class Block(object):
    def __init__(self, index, timestamp, previous_hash, kudo):
        if (index < 0):
            raise IndexError
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.kudo = kudo
        self.hash = self.hashing(self.index, self.timestamp, self.previous_hash, self.kudo)

    @staticmethod
    def hashing(index, timestamp, previous_hash, kudo):
        key = hashlib.sha256()
        key.update(str(index).encode('utf-8'))
        key.update(str(timestamp).encode('utf-8'))
        key.update(str(previous_hash).encode('utf-8'))
        key.update(str(kudo.__dict__).encode('utf-8'))
        return key.hexdigest()
    