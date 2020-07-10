from flask_restful import Resource, fields, marshal_with, marshal
from App.models import Letter, City

city_fields = {
    "id": fields.Integer,
    'regionName': fields.String,
    'CityCode': fields.Integer,
    'pinYin': fields.String,
    'parentId': fields.Integer(default=0)
}
city_list_fields = {
    "A": fields.List(fields.Nested(city_fields)),

}
result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(city_list_fields)
}


class CityResource(Resource):

    def get(self):
        returnValue = {}
        letters = Letter.query.all()
        city_list_fields_dynamic = {}
        for letter in letters:
            cities = City.query.filter(City.c_letter == letter.id).all()

            returnValue[letter.letter] = cities
            city_list_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))
        result_fields_dynamic = {
            "returnCode": fields.String,
            "returnValue": fields.Nested(city_list_fields_dynamic)
        }
        print(returnValue)

        data = {
            "returnCode": "0",
            "returnValue": returnValue
        }
        result = marshal(data, result_fields_dynamic)
        return result

    @marshal_with(result_fields)
    def post(self):
        returnValue = {}
        letters = Letter.query.all()

        for letter in letters:
            cities = City.query.filter(City.c_letter == letter.id).all()

            returnValue[letter.letter] = cities

        data = {
            "returnCode": "0",
            "returnValue": returnValue
        }

        return data
