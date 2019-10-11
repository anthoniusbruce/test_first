import flask
import chain
import kudo_jsonencoder
import request_validator

app = flask.Flask(__name__)
blockchain = chain.Chain()

@app.route("/")
def index():
    return "Hello! World!"

@app.route("/test_first/api/v1.0/kudos", methods = ["POST"])
def add_kudo():
    json = flask.request.json
    valid = request_validator.RequestValidator.validate_post(json)
    if (not valid[0]):
        flask.abort(400, valid[1])

    result = blockchain.add_block(json["recipient"], json["nominator"], json["date"])

    return flask.jsonify({"index": result})

@app.route("/test_first/api/v1.0/kudos", methods = ["GET"])
def get_list():
    kudo_list = blockchain.get_list()
    encoder = kudo_jsonencoder.KudoJSONEncoder()
    response = flask.Response(encoder.encode(kudo_list), mimetype="application/json")
    return response

if (__name__ == "__main__"):
    app.run()
