import flask
from flask import Flask
from flask import request

from store.get_query_result import get_query_results
from analytics import do_some_simple_analytics

app = Flask(__name__)


@app.route('/')
def index():
    return "Pairing Application"


@app.route('/get-name-from-userid', methods=['GET'])
def get_name_from_user_id():
    userId = int(request.args.get('userId', 0))
    return flask.jsonify({"name": userId})

app.run(debug=True)
