from flask import request, g
from flask_restful import abort

from App.apis.movie_user.models_utils import get_movie_user
from App.ext import cache
from App.utils import MOVIE_USER


def _verify():
    token = request.args.get("token")
    if not token:
        abort(401, msg="NOT LOGIN")

    if not token.startwith(MOVIE_USER):
        abort(403, msg="no access")
    user_id = cache.get(token)



    if not user_id:
        abort(401, msg="USER NOT AVAILABLE")
    user = get_movie_user(user_id)

    if not user:
        abort(401, msg="USER NOT AVAILABLE")

    g.user = user
    g.auth = token


def login_required(fun):
    def wrapper(*args, **kwargs):
        _verify()

        return fun(*args, **kwargs)

    return wrapper


def required_permission(permission):
    def required_permission_wrapper(fun):
        def wrapper(*args, **kwargs):
            _verify()

            if not g.user.check_permission(permission):
                abort(403, msg="user can't access")
            return fun(*args, **kwargs)

        return wrapper

    return required_permission_wrapper
