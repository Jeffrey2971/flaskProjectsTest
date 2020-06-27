import random
from _operator import or_
from operator import and_
from flask import Blueprint, render_template, request, current_app, g, abort
from sqlalchemy import not_
from App.ext import db
from App.models import Person, Grade, Student

blue = Blueprint('first_blue', __name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'Hello Flask'

@blue.route('/addperson/')
def add_person():
    person = Person()
    person.p_name = '我喜欢的人%d' % random.randrange(100)
    person.p_age = random.randrange(100)
    db.session.add(person)
    db.session.commit()
    return 'Add Sucess'

@blue.route('/getpersons/')
def get_persons():
    # filter 模型.属性.运算符（值）
    # filter_by
    # persons = Person.query.filter_by(id = 5)
    # persons = Person.query.filter(Person.p_age.__ge__(18))
    # order_by 需要最先调用
    # persons = Person.query.order_by('p_age').offset(2).limit(6)
    # limit 和 offset 书写顺序没关系，都是先调用offset
    # persons = Person.query.order_by('p_age').limit(6).offset(2)
    # persons = Person.query.filter(and_(Person.id > 2, Person.id < 7))  # 大于二或小于七的id
    # persons = Person.query.filter(or_(Person.id < 2, Person.id > 7))  # 小于二或大于七的id
    persons = Person.query.filter(not_(Person.p_age.__eq__(69)))  # 不等于十七

    return render_template('PersonList.html', persons=persons)

@blue.route('/getperson/')
def get_person():
    # person = Person.query.get(40)
    person = Person.query.order_by("-id").first()
    print(person.p_name)
    return 'Get Success'

@blue.route('/get_with_page/')
def get_persons_with_page():
    # 核心点 需要获取那一页的数据 每一个有多少数据
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # 偏移跳过多少条，限制结果集是多少条
    persons = Person.query.offset(per_page*(page-1)).limit(per_page)

    return render_template('PersonList.html', persons=persons)

@blue.route('/getpersonsbypagination/')
def get_persons_by_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 6, type=int)
    paginaton = Person.query.paginate(page, per_page, False)
    persons = paginaton.items
    return render_template('PersonListWithPagination.html', persons=persons, pagination=paginaton)

@blue.route('/addgrade/')
def add_grade():
    grade = Grade()
    grade.g_name = 'python%d' % random.randrange(2000)
    db.session.add(grade)
    db.session.commit()
    return 'Grade Add Success'

@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.s_name = '爱学习的飞飞%d' % random.randrange(200)

    # grade = Grade.query.order_by('-id').first()
    grade = Grade.query.order_by('-id').first()
    student.s_grade_id = grade.id
    db.session.add(student)
    db.session.commit()
    return 'Student add Success'


@blue.route('/getgradebystudent/')
def get_grade_by_student():

    student = Student.query.order_by('id').first()

    # grade = Grade.query.get(student.s_grade_id)

    grade = student.grade
    return grade.g_name

@blue.route('/getstudentbygrade/')
def get_student_by_grade():
    grade = Grade.query.order_by('id').first()
    # students = Student.query.filter(Student.s_grade_id == grade.id)
    students = grade.g_student
    print(grade.g_student)
    print(type(grade.g_student))

    return render_template('StudentList.html', students=students)

@blue.route('/innerObject/')
def inner_object():
    print('请求进来了')
    config = current_app.config
    # print(config)
    # print(type(config))
    #
    # for key in config.keys():
    #     print(key, config.get(key))
    print(g.content)
    return render_template('InnerObject.html')

@blue.before_request
def process_request():
    print('请求进来之前')

    if request.path == '/innerObject/':
        g.content = '警告：不可访问'
        # return '暂时不可访问数据'
    elif request.path == '/addgrade/':
        abort(403)

@blue.errorhandler(403)
def process_exception(e):
    print(e)
    return '异常403'

