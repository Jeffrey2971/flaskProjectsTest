from time import sleep

from flask_restful import Resource, fields, marshal_with, reqparse

from App.ext import db
from App.models import Student

"""
返回格式制定

    返回数据集

    {
        msg:"msg",
        status: "200",
        data: [
            {
                id:1,
                s_name: "jeffrey",
                s_age: "000"
            }
        ]
    }
    
    返回单一对象
    
    {
        msg:"msg",
        status: "200",
        data: {
            id:1,
            s_name:"jeffrey",
            s_age: 000
        }
    }
    
    @marshal_with 可以对输出格式进行定制 
    
"""
student_fields = {
    # 属性定制，可以让格式化后的数据和源数据名不一样，但是中间是通过人为方式设定的
    "id": fields.Integer,
    "name": fields.String(attribute="s_name"),
    "age": fields.Integer(attribute="s_age"),
    # default 设置默认值，当值不存在时默认使用默认值
    "hobby": fields.String(default="learn"),
    # 可以生成对应资源的表现层
    "url": fields.Url("studentresource", absolute=True)
}
result_student_files = {
    "msg": fields.String,
    "status": fields.String,
    # Nested 嵌套的，级联的
    "data": fields.Nested(student_fields)
}

# 请求参数
parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="must supply name")
parse.add_argument("age", required=True, type=int, help="must supply age")


class StudentResource(Resource):
    @marshal_with(result_student_files)
    def get(self, id=None):
        data = {
            "msg": "ok",
            "status": "200",
        }
        student = Student.query.get(id)
        data["data"] = student
        # student = Student.query.first()
        return data

    @marshal_with(result_student_files)
    def post(self, id=None):

        student = Student.query.get(id)
        parser = parse.parse_args()
        name = parser.get("name")
        age = parser.get("age")

        student.s_name = name
        student.s_age = age

        db.session.add(student)
        db.session.commit()

        data = {
            "msg": "ok",
            "status": "200",
            "data": student
        }

        return data

    def delete(self, id=None):
        student = Student.query.get(id)

        data = {

        }

        if student:
            db.session.delete(student)
            db.session.commit()

            data["status"] = "204"
            data["msg"] = "Delete success"

            return data

        else:
            # 请求成功但数据不存在
            data["status"] = "804"
            data["msg"] = "does not exist"

            return data

result_students_files = {
    "msg": fields.String,
    "status": fields.String,
    # Nested 嵌套的，级联的
    "data": fields.List(fields.Nested(student_fields))
}

class StudentsResource(Resource):

    @marshal_with(result_students_files)
    def get(self):
        data = {
            "msg": "ok",
            "status": "200",
        }
        students = Student.query.all()

        sleep(3)

        data["data"] = students
        # student = Student.query.first()
        return data


    @marshal_with(result_student_files)
    def post(self):
        parser = parse.parse_args()
        name = parser.get("name")
        age = parser.get("age")

        student = Student()
        student.s_name = name
        student.s_age = age

        db.session(student)
        db.session.commit()

        data = {
            "msg": "ok",
            "status": "200",
            "data": student
        }

        return data