from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    from api.api import crud_api
    app.register_blueprint(crud_api)

    # it's no need to db.create_all(), it does by itself
    from db.models import db
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run()
