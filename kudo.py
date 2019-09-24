import datetime

class Kudo(object):
    def __init__(self, recipient, nominator, date):
        self.recipient = recipient
        self.nominator = nominator
        self.date = date