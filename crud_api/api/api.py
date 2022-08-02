from flask import Blueprint, request, jsonify
from .methods import GetUser, post, delete

crud_api = Blueprint('crud_api', __name__)


@crud_api.route('/crud', methods=['GET'])
def get_operations():
    id = request.args.get('id', type=int)
    if id:
        return GetUser().get_by_id(id)

    email = request.args.get('email', type=str)
    if email:
        return GetUser().get_by_email(email)

    return jsonify(message=("You are maybe passing the wrong parameters in the request, please use the parameter 'id' to search for a user"), status=400)


@crud_api.route('/crud', methods=['POST'])
def post_operations():
    name = request.args.get('name', type=str)
    email = request.args.get('email', type=str)

    return post(name, email)


@crud_api.route('/crud', methods=['DELETE'])
def delete_operations():
    id = request.args.get('id', type=int)
    return delete(id)
