import random
from flask import render_template
from flask import Blueprint
from App.ext import db as model
from App.models import Student

blue = Blueprint('first_blue', __name__)
def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello Flask'

@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.s_name = '洪泽飞%d' % random.randrange(100)

    model.session.add(student)
    model.session.commit()

    return 'Student Create Success'

@blue.route('/addstudents/')
def add_students():
    students = []
    for i in range(20):
        student = Student()
        student.s_name = 'jm%d' % random.randrange(1000)
        students.append(student)
    model.session.add_all(students)
    model.session.commit()
    return 'Students Add Success'

@blue.route('/deletestudent/')
def del_student():
    # 先查询再删除
    student = Student.query.first()

    # 删除数据
    model.session.delete(student)
    model.session.commit()
    return 'Student Delete Sucess'

@blue.route('/modifystudent/')
def modify_student():
    student = Student.query.first()
    student.s_name = 'mablechong%d' % random.randrange(18)
    model.session.add(student)
    model.session.commit()
    return 'Student Modify SUcess'

@blue.route('/getstudent/')
def get_student():
    # __eq__查询 students = Student.query.filter(Student.id.__eq__(10))
    # __le__查询 students = Student.query.filter(Student.id.__le__(10))
    students = Student.query.filter(Student.s_name.contains('jm'))


    for student in students:
        print(student.s_name)
    # print(type(students))
    # print(students)
    return render_template('StudentList.html', students=students)