import flask
import chain
import kudo_jsonencoder
import request_validator
from flask_swagger_ui import get_swaggerui_blueprint

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

    blockchain.add_block(json["recipient"], json["nominator"], json["date"])

    return flask.Response(status=201)

@app.route("/test_first/api/v1.0/kudos", methods = ["GET"])
def get_list():
    kudo_list = blockchain.get_list()
    encoder = kudo_jsonencoder.KudoJSONEncoder()
    response = flask.Response(encoder.encode(kudo_list), mimetype="application/json")
    return response

@app.route("/test_first/api/v1.0/validate", methods = ["GET"])
def validate():
    isvalid = blockchain.verify()
    return flask.jsonify(isvalid)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "test_first"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

if (__name__ == "__main__"):
    app.run()
