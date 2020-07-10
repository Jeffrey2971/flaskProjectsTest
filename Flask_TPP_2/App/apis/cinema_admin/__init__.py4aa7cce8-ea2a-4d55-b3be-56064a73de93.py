from flask_restful import Api

from App.apis.cinema_admin.Hello_api import TestMovieAdmin

movie_client_api = Api(prefix='/movieclient')

movie_client_api.add_resource(TestMovieAdmin, '/hello/')