from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"msg": "ok"}

    def post(self):
        return {"msg": "post ok"}

    def put(self):
        return {'msg': 'put ok'}

    def delete(self):
        return {'msg': 'delete ok'}