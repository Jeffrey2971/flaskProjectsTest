from flask_restful import Resource, fields, marshal, marshal_with, reqparse

from App.models import Movie

movie_fields = {
    "id": fields.Integer,
    "showname": fields.String,
    "director": fields.String,
    "leadingRole": fields.String,
    "type": fields.String,
    "country": fields.String,
    "language": fields.String,
    "duration": fields.Integer,
    "openDay": fields.DateTime,
    "poster": fields.String,
    "orderCount": fields.Integer
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.List(fields.Nested(movie_fields))
}

parse = reqparse.RequestParser()
parse.add_argument("orderCount", type=int, required=True, help='请提供你要查询的类型')


class MovieResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parser = parse.parse_args()

        orderCount = parser.get('orderCount')

        movies = Movie.query.filter(Movie.orderCount == orderCount).all()

        data = {
            "returnCode": "0",
            "returnValue": movies
        }

        return data
