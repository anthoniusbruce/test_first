import json
import kudo
import datetime

class KudoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if (isinstance(o, kudo.Kudo)):
            return o.__dict__
        if (isinstance(o, datetime.date)):
            return str(o)
            
        return json.JSONEncoder.default(self, o)