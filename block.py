import datetime
import kudo

class Block(object):
    def __init__(self, index, timestamp, previous_hash, kudo):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.kudo = kudo
