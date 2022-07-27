from flask import Blueprint, request
from .methods import get, post, delete

crud_api = Blueprint('crud_api', __name__)


@crud_api.route('/crud', methods=['GET', 'POST', 'DELETE'])
def operations():
    if request.method == 'GET':
        id = request.args.get('id', type=int)
        return get(id)

    if request.method == 'POST':
        name = request.args.get('name', type=str)
        email = request.args.get('email', type=str)

        return post(name, email)

    if request.method == 'DELETE':
        id = request.args.get('id', type=int)
        return delete(id)
