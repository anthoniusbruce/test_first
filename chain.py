import block
import datetime
import kudo
import threading

class Chain(object):
    def __init__(self):
        timestamp = datetime.datetime.utcnow()
        initial_hash = "inital_hash"
        date = datetime.date(timestamp.year, timestamp.month, timestamp.day)
        self.blocks = [self.get_genesis_block(timestamp, initial_hash, date)]
        self.lock = threading.Lock()

    def add_block(self, recipient, nominator, date):
        self.lock.acquire()
        try:
            index = len(self.blocks)
            timestamp = datetime.datetime.utcnow()
            previous_hash = self.blocks[index - 1].hash
            kudo_rec = kudo.Kudo(recipient, nominator, date)
            self.blocks.append(block.Block(index, timestamp, previous_hash, kudo_rec))
        finally:
            self.lock.release()

    def verify(self):
        ret_val = True

        for i in range(1, len(self.blocks)):
            current = self.blocks[i]
            if (current.index != i):
                ret_val = False
            elif (current.previous_hash != self.blocks[i-1].hash):
                ret_val = False
            elif (current.hash != current.hashing(current.index, current.timestamp, current.previous_hash, current.kudo)):
                ret_val = False

        return ret_val

    def get(self, index):
        ret_val = None

        if (index > 0 and index < len(self.blocks)):
            ret_val = self.blocks[index].kudo

        return ret_val

    def count(self):
        return len(self.blocks) - 1

    def get_list(self):
        kudos = []
        for i in range(1, len(self.blocks)):
            kudos.append(self.blocks[i].kudo)
        return kudos

    @staticmethod
    def get_genesis_block(timestamp, initial_hash, kudo_date):
        return block.Block(0, timestamp, initial_hash, kudo.Kudo("", "", kudo_date))