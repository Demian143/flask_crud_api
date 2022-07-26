from flask import Blueprint, request
from .methods import get, post, delete

crud_api = Blueprint('crud_api', __name__)


@crud_api.route('/<args>', methods=['GET', 'POST', 'DELETE'])
def operations():
    if request.method == 'GET':
        return get(request.args.get('id'))

    if request.method == 'POST':
        name = request.args.get('name')
        email = request.args.get('email')
        return post(name, email)

    if request.method == 'DELETE':
        id = request.args.get('id')
        return delete(id)
