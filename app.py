#!test_first_venv/bin/python
import flask
import chain
import kudo_jsonencoder

app = flask.Flask(__name__)
blockchain = chain.Chain()

@app.route("/")
def index():
    return "Hello! World!"

@app.route("/test_first/api/v1.0/kudos", methods = ["POST"])
def add_kudo():
    json = flask.request.json
    if (not json or not "recipient" in json or not "nominator" in json or not "date" in json):
        flask.abort(400)

    result = blockchain.add_block(json["recipient"], json["nominator"], json["date"])

    return flask.jsonify({"index": result})

@app.route("/test_first/api/v1.0/kudos", methods = ["GET"])
def get_list():
    kudo_list = blockchain.get_list()
    encoder = kudo_jsonencoder.KudoJSONEncoder()
    response = flask.Response(encoder.encode(kudo_list), mimetype="application/json")
    return response

if (__name__ == "__main__"):
    app.run(port = 5002, debug=True)