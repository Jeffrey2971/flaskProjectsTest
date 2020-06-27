from App.ext import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=15)




