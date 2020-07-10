from flask_restful import Resource


class TestMovieAdmin(Resource):
    def get(self):
        return {"msg": "ok"}