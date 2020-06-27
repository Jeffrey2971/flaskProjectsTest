from App.ext import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=16)

    def model_to_dict(self):
        return {"id": self.id, "name": self.s_name, "age": self.s_age}