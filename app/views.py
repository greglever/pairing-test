import flask
from flask import request
from app import app

from store.get_query_result import get_query_results


@app.route('/')
def index():
    return "Pairing Application"


@app.route('/get-name-from-userid', methods=['GET'])
def get_name_from_user_id():
    userId = int(request.args.get('userId', 0))
    query = "SELECT name FROM users WHERE id = {userId}".format(userId=userId)
    result = get_query_results(query)
    return flask.jsonify({"name": result})
