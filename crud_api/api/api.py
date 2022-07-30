from email.mime import message
from flask import Blueprint, request, jsonify
from .methods import get, post, delete

crud_api = Blueprint('crud_api', __name__)


@crud_api.route('/crud', methods=['GET', 'POST', 'DELETE'])
def operations():
    if request.method == 'GET':
        not_none = request.args.get('id')
        if not_none:
            id = request.args.get('id', type=int)
            return get(id)
        return jsonify(message=("You are maybe passing the wrong parameters in the request, please use the parameter 'id' to search for a user"), status=400)

    if request.method == 'POST':
        name = request.args.get('name', type=str)
        email = request.args.get('email', type=str)

        return post(name, email)

    if request.method == 'DELETE':
        id = request.args.get('id', type=int)
        return delete(id)
