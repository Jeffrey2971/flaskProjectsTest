"""
抓取地址信息

    使用脚本实现数据导入
        将抓取到的json放入自己的数据库中

        把json的内容读取出来
        把读取的数据写入到数据库中

"""

import json
import pymysql


def json_to_db():
    # 连接数据库
    client = pymysql.Connect(user='root', password='664490254', host='localhost', port=3306, db='PythonObject_TPP',
                             charset='utf8')
    cursor = client.cursor()
    with open('Cities.json', mode='r') as cities:
        """
        <_io.TextIOWrapper name='Cities.json' mode='r' encoding='UTF-8'>
        <class '_io.TextIOWrapper'>r
        """
        cities_info = cities.read()
        load_json = json.loads(cities_info)
        returnValue = load_json.get('returnValue')
        # print(returnValue)
        city_letters = returnValue.keys()
        # print(city_letters)

    for key in city_letters:
        # 存储字母
        cursor.execute("INSERT INTO letter(letter) VALUE ('%s');" % key)
        client.commit()
        cursor.execute('SELECT * FROM letter WHERE letter="%s";' % key)
        client.commit()
        letter_id = cursor.fetchone()[0]
        letter_cities = returnValue.get(key)
        # print(letter_cities)
        for letter_city in letter_cities:
            # print(letter_city)

            city_id = letter_city.get('id')
            city_regionName = letter_city.get('regionName')
            city_Code = letter_city.get('cityCode')
            city_pinYin = letter_city.get('pinYin')
            cursor.execute(
                "INSERT INTO city(id, regionName, cityCode, pinYin, c_letter) VALUE (%d, '%s', %d, '%s', %d);" % (
                city_id, city_regionName, city_Code, city_pinYin, letter_id))
            client.commit()
    cursor.close()
    client.close()


if __name__ == '__main__':
    json_to_db()
