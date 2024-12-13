from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creating database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample_database.db"
db = SQLAlchemy(app)


# creating a table


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

    # create a new recod
    # new_record = Table(id=1, name='Dipesh')
    # db.session.add(new_record)
    # db.session.commit()
