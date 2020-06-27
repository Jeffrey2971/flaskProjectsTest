from App.ext import db as model


class Student(model.Model):
    id = model.Column(model.Integer, primary_key=True, autoincrement=True)
    s_name = model.Column(model.String(16))

class Teacher(model.Model):
    id = model.Column(model.Integer, primary_key=True, autoincrement=True)
    t_name = model.Column(model.String(16))

class Animal(model.Model):
    id = model.Column(model.Integer, primary_key=True, autoincrement=True)
    a_name = model.Column(model.String(16))