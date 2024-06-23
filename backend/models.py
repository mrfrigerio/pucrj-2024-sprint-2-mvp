from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Capture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String(50), nullable=False)
    capture_date = db.Column(db.String(10), nullable=False)
    pokemon_name = db.Column(db.String(50), nullable=False)
    pokemon_image = db.Column(db.String(200), nullable=False)
