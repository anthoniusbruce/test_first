class RequestValidator(object):
    @staticmethod
    def validate_post(json):
        ret_val = True
        error = "missing "
        if (not json):
            ret_val = False
            error = error + "kudo"
            return ret_val, error

        comma = ""
        if (not "recipient" in json):
            ret_val = False
            error = error + "recipient"
            comma = ", "
        if (not "nominator" in json):
            ret_val = False
            error = error + comma + "nominator"
            comma = ", "
        if (not "date" in json):
            ret_val = False
            error = error + comma + "date"

        if (ret_val and json["recipient"] == json["nominator"]):
            ret_val = False
            error = "recipient cannot not match nominator"

        return ret_val, error