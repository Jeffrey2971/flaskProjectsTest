from flask import g
from flask_restful import Resource, abort

from App.apis.movie_user.utils import login_required, required_permission
from App.models.movie_user.movie_user_model import VIP_USER, COMMON_USER


class MovieOrderResource(Resource):

    @login_required
    def post(self):
        user = g.user

        return {"msg": "post ok"}


class MovieOrdersResource(Resource):
    @required_permission(VIP_USER)
    def put(self, order_id):

            return {"msg": "change success"}
