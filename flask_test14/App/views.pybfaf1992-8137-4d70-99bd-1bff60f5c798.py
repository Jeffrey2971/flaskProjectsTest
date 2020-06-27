from flask import Blueprint, request, jsonify

from App.ext import db
from App.models import Student

blue = Blueprint("first_blue", __name__, url_prefix="/api/") # 统一前缀

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route("/index/")
def index():

    return "Flask index"

@blue.route("/students/", methods=["GET", "POST"])
@blue.route("/students/<int:id>/", methods=["GET", "POST", "DELETE", "PUT"])
def students(id=None):

    if request.method == "POST":
        username = request.form.get("username")
        age = request.form.get("age")
        student = Student()
        student.s_name = username
        student.s_age = age
        db.session.add(student)
        db.session.commit()

        return jsonify(student.model_to_dict()), 201

    elif request.method == "GET":
        students = Student.query.all()
        data = []
        for student in students:
            data.append(student.model_to_dict())
        return jsonify(data=data)
    elif request.method == "DELETE":
        data = {}
        if id:
            student = Student.query.get(id)
            if student:
                db.session.delete(student)
                db.session.commit()
                data["msg"] = "Delete Success"
                return jsonify(data)
            else:
                data["msg"] = "invilidate"
                return jsonify(data)
        else:
            data["msg"] = "not exist"
            return jsonify(data)
    elif request.method == "PUT":
        if id:
            username = request.form.get("username")
            age = request.form.get("age")
            
            student = Student.query.get(id)
            student.s_name = username
            student.s_age = age
            
            db.session.add(student)
            db.session.commit()
            
            return jsonify(student.model_to_dict())
        else:
            return None