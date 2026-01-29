from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Details(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


