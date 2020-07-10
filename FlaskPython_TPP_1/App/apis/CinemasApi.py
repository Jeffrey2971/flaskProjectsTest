from flask_restful import Resource, fields, marshal_with, reqparse

from App.models import Cinemas

cinemas_fields = {
    "name": fields.String,
    "city": fields.String,
    "district": fields.String,
    "address": fields.String,
    "phone": fields.String,
    "score": fields.Float,
    "hallnum": fields.Integer,
    "servicecharge": fields.Float,
    "astrict": fields.Integer,
    "flag": fields.Integer,
    "isdelete": fields.Boolean
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.List(fields.Nested(cinemas_fields))
}

parse = reqparse.RequestParser()
parse.add_argument('city', type=str, help='城市定位失败')
parse.add_argument('district', type=str)  # 区域筛选
parse.add_argument('sortrule', type=int)  # 评分筛选

SCORE_DESC = 1
SCORE_ASC = 1


class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        parser = parse.parse_args()
        city = parser.get('city')
        district = parser.get('district')
        score = parser.get('score')

        if district:

            cinemas_list = Cinemas.query.filter(Cinemas.city == city).filter(Cinemas.district == district).all()
        else:
            cinemas_list = Cinemas.query.filter(Cinemas.city == city).all()

        sort_rule = parser.get('sortrule')

        if sort_rule == SCORE_DESC:
            cinemas_list = cinemas_list.order_by('-score').all()
        elif sort_rule == SCORE_ASC:
            cinemas_list = cinemas_list.order_by('score').all()

        data = {
            "returnCode": "0",
            "returnValue": cinemas_list
        }
        return data
