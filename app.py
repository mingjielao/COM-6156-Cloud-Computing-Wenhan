from flask import Flask, Response,request
from flask_cors import CORS
import json
import logging

from database_services.RDBService import RDBService as RDBService
from application_services.GroupResource.group_resource import GroupResource

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/groups', methods=['GET', 'POST'])
def get_or_insert_group():
    if request.method == 'POST':
        create_data = request.get_json()
        res = GroupResource.create(create_data)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
    else:
        res = GroupResource.get_by_template(None, request.args.get("limit") or "100",
                                            request.args.get("offset") or "0")
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/groups/<group_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_group_by_id(group_id):
    if request.method == 'GET':
        res = GroupResource.get_by_id(group_id)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
    elif request.method == 'PUT':
        update_data = request.get_json()
        res = GroupResource.put(update_data, group_id)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")
    else:
        res = GroupResource.delete_by_id(group_id)
        rsp = Response(json.dumps(res), status=200, content_type="application/json")

    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
