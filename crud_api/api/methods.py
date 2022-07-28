from flask import Response
from db.models import User, db


def get(id: int) -> Response:
    user = User.query.filter_by(id=id).first()

    if user is not None:
        return Response(f'{user.id, user.name, user.email}', status=200)

    return Response("user don't exists", status=400)


def post(name: str, email: str) -> Response:
    email = User.query.filter_by(email=email).first()
    if email:
        return Response("user already exists", status=400)
    else:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return Response("success", status=200)


def delete(id: int) -> Response:
    user = User.objects.filter_by(id=id).first()
    if user:
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return Response('user deleted', status=200)

    return Response('bad request', status=400)
