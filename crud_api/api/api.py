from flask import Blueprint
from flask import request
from db.models import User, db

crud_api = Blueprint('crud_api', __name__)


@crud_api.route('/<kwargs>', methods=['GET', 'POST', 'DELETE'])
def operations(**kwargs):
    if request.method == 'GET':
        get(kwargs['id'])

    if request.method == 'POST':
        post(kwargs['name'], kwargs['email'])

    if request.method == 'DELETE':
        delete(kwargs['id'])


def get(id: int):
    _user = User.query.filter_by(id=id)
    return _user


def post(name, email):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()


def delete(id: int):
    User.query.filter_by(id=id).delete()
    db.session.commit()
