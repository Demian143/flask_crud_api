from flask import jsonify, Response
from db.models import User, db


def get(id: int) -> Response:
    user = User.query.filter_by(id=id).first()

    if user:
        return jsonify(id=user.id,
                       username=user.name,
                       email=user.email)

    return jsonify(message="user don't exists", status=400)


def post(name: str, email: str) -> Response:
    exists = User.query.filter_by(email=email).first()

    if exists:
        return jsonify(message="user already exists", status=400)

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="Success", status=200)


def delete(id: int) -> Response:
    user = User.query.filter_by(id=id).first()

    if user:
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify(message="User deleted", status=200)

    return jsonify(message="Bad request", status=400)
