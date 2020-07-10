from flask_restful import Resource

from App.tasks import add


class HelloResource(Resource):

    def get(self):
        add.delay(4, 5)
        return {'msg': 'hello'}
