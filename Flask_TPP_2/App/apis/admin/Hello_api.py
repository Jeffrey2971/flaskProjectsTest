from flask_restful import Resource


class TestAdminResource(Resource):
    def get(self):
        return {"msg": "ok"}