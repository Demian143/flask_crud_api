from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(20), unique=True)

    def __repr__(self) -> str:
        return '<User: %r>' % self.name
