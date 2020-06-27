from App.ext import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(16))
    p_age = db.Column(db.Integer, default=18)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(16), unique=True)
    # 懒加载 懒获取
    g_student = db.relationship('Student', backref='Grade', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer, default=16)
    s_grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)

class Animal(db.Model):
    # __tablename__ = 'Cat'  # 改名
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(16))

class Cat(Animal):
    c_legs = db.Column(db.Integer, default=4)

class Dog(Animal):
    d_color = db.Column(db.String(8), default='ff0000')
