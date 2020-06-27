from flask_restful import Api
from App.views.GradeApi import GradeResource
from App.views.HelloApi import Hello
from App.views.StudentApi import StudentResource, StudentsResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(Hello, '/', methods=['GET', 'POST', 'PUT', 'DELETE'])
api.add_resource(StudentsResource, '/students/', methods=['GET', 'POST'])
api.add_resource(StudentResource, '/students/<int:id>/', methods=['GET', 'POST', 'DELETE'])
api.add_resource(GradeResource, '/grades/', methods=['GET', 'POST'])
