import json

import pymysql

"""
此脚本用于将城市数据插入数据库中
"""


def load_data():
    with open('./data/cities.json', mode='r') as cities_json_file:
        cities_json_str = cities_json_file.read()
        cities_json = json.loads(cities_json_str)
        return cities_json


def insert_json(cities_json):
    cities = cities_json.get("returnValue")
    keys = cities.keys()

    db = pymysql.Connect(host="localhost", port=3306, user="root", password="664490254", database="PythonObject_TPP_2",
                         charset='utf8')

    cursor = db.cursor()
    for key in keys:
        cursor.execute("INSERT INTO letter(letter) VALUES ('%s');" % key)
        db.commit()
        cursor.execute("SELECT letter.id FROM letter WHERE letter='%s'" % key)
        letter_id = cursor.fetchone()[0]
        cities_letter = cities.get(key)
        for city in cities_letter:

            c_id = city.get('id')
            c_parent_id = city.get('parentId')
            c_region_name = city.get('regionName')
            c_city_code = city.get('cityCode')
            c_pinyin = city.get('pinYin')

            # print(letter_id,c_id,c_parent_id, c_region_name, c_city_code, c_pinyin)
            cursor.execute(
                "INSERT INTO city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) VALUES (%d, %d, %d, '%s', %d, '%s');" % (
                    letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))
            db.commit()


if __name__ == '__main__':
    cities_json = load_data()
    insert_json(cities_json)
