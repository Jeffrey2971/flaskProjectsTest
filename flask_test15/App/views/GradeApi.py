from flask import request
from flask_restful import Resource, reqparse

# 请求参数转换器
parse = reqparse.RequestParser()
parse.add_argument('gradeid', type=int, required=True, action='append', help='班级id必须是数字')
parse.add_argument('host', location='headers')

class GradeResource(Resource):
    def get(self):
        #  获取参数
        # gradeid = request.args.get('gradeid')
        # print(gradeid)
        # print(type(gradeid))
        parser = parse.parse_args()
        gradeid = parser.get('gradeid')
        print(gradeid)
        print(type(gradeid))
        host = parser.get('host')
        print(host)
        print(type(host))

        return {'msg': 'ok'}

    def post(self):
        parser = parse.parse_args()
        gradeid = parser.get('gradeid')
        print(gradeid)
        print(type(gradeid))
        return {'msg': 'post ok'}