from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Each class is a database table
class Verb(db.Model):
    # Id's help keep data unique
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80)) 

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return '<Word %r>' % (self.word) 