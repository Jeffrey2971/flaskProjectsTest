"""
处理电影信息

    使用脚本实现数据导入
        将抓取到的json放入自己的数据库中

        把json的内容读取出来
        把读取的数据写入到数据库中

"""
import json
import pymysql

client = pymysql.Connect(user='root', password='664490254', host='localhost', port=3306, db='PythonObject_TPP',
                         charset='utf8')
cursor = client.cursor()
with open('hot.json', mode='r') as movies:
    cities_info = movies.read()
    load_json = json.loads(cities_info)
    returnValue = load_json.get('returnValue')

    for key in returnValue:
        """
        {'id': 1320840, 'showName': '猎狐者', 'director': '林德禄', 'leadingRole': '姜武,余男', 'type': '剧情,动作,犯罪', 'country': '中国大陆', 'language': '汉语普通话', 'openDay': '2020-12-31 00:00:00', 'poster': 'i4/TB1RjwUduL2gK0jSZPhXXahvXXa_.jpg', 'orderCount': 0, 'trailer': ['i1/TB1IJ3WdET1gK0jSZFrXXcNCXXa_.jpg', 'i4/TB1p3cWdy_1gK0jSZFqXXcpaXXa_.jpg', 'i2/TB1Q.wVdrr1gK0jSZFDXXb9yVXa_.jpg', 'i4/TB1tW3WdET1gK0jSZFhXXaAtVXa_.jpg', 'i4/TB1S.AWdAL0gK0jSZFAXXcA9pXa_.jpg', 'i1/TB1rMcWdCf2gK0jSZFPXXXsopXa_.jpg', 'i1/TB1cgkYdBr0gK0jSZFnXXbRRXXa_.jpg', 'i2/TB1OKZWdxn1gK0jSZKPXXXvUXXa_.jpg', 'i1/TB1HbIUdpT7gK0jSZFpXXaTkpXa_.jpg'], 'orderBy': 10000, 'features': {'openCountry': '中国大陆', 'year': '2020', 'openTime': '2020', 'isReOpen': '0'}, 'fromSearch': False, 'openTime': '2020', 'fantastic': 0, 'userShowStatus': 0}
        'imdbid': 'tt7653254', 'orderBy': 10000, 'backgroundPicture': 'i4/TB12X6NsebviK0jSZFNXXaApXXa_.jpg', 'features': {'openCountry': '中国大陆', 'enableCustomShowTag': '1', 'customShowTag': '寡姐冲奥之作', 'year': '2019', 'topVideoPoster': 'i3/TB1b.9CsKL2gK0jSZPhXXahvXXa_.jpg', 'openTime': '2020', 'isReOpen': '0'}, 'fromSearch': False, 'openTime': '2020', 'fantastic': 0, 'userShowStatus': 0}
        {'id': 1322047, 'showName': '白狮奇缘', 'showNameEn': 'Mia et le Lion Blanc', 'director': '吉勒斯·戴·迈斯特', 'leadingRole': '兰利·柯克伍德,梅拉尼·罗兰,布兰登·奥雷,Tessa Jubber', 'type': '家庭,冒险', 'country': '法国', 'language': '法语', 'duration': 99, 'openDay': '2020-12-31 00:00:00', 'poster': 'i1/TB1rddXgCf2gK0jSZFPXXXsopXa_.jpg', 'orderCount': 0, 'trailer': ['i2/TB1aUWReeP2gK0jSZFoXXauIVXa_.jpg', 'i3/TB1tT5NeoY1gK0jSZFMXXaWcVXa_.jpg', 'i4/TB1kOWPekL0gK0jSZFAXXcA9pXa_.jpg', 'i4/TB1UAyKeaL7gK0jSZFBXXXZZpXa_.jpg', 'i4/TB1In5NeoY1gK0jSZFMXXaWcVXa_.jpg', 'i4/TB1U_WPeeH2gK0jSZFEXXcqMpXa_.jpg', 'i3/TB1_UGSea61gK0jSZFlXXXDKFXa_.jpg', 'i4/TB1zt1Tebj1gK0jSZFOXXc7GpXa_.jpg', 'i2/TB1NieQelr0gK0jSZFnXXbRRXXa_.jpg', 'i3/TB1DEWOehn1gK0jSZKPXXXvUXXa_.jpg', 'i1/TB1TFeQekY2gK0jSZFgXXc5OFXa_.jpg', 'i4/TB1MAyKeaL7gK0jSZFBXXXZZpXa_.jpg', 'i3/TB10EWSehD1gK0jSZFyXXciOVXa_.jpg', 'i1/TB1onWPeeH2gK0jSZFEXXcqMpXa_.jpg', 'i1/TB18.WOehn1gK0jSZKPXXXvUXXa_.jpg', 'i3/TB121bQekL0gK0jSZFtXXXQCXXa_.jpg', 'i4/TB1rm_QeoY1gK0jSZFMXXaWcVXa_.jpg', 'i1/TB1WMYQeeL2gK0jSZPhXXahvXXa_.jpg', 'i2/TB1wBbNeaL7gK0jSZFBXXXZZpXa_.jpg', 'i4/TB1SowYeYr1gK0jSZFDXXb9yVXa_.jpg', 'i2/TB1sWMZe4n1gK0jSZKPXXXvUXXa_.jpg', 'i3/TB1kp.WeVT7gK0jSZFpXXaTkpXa_.jpg', 'i2/TB1uMoWeW67gK0jSZFHXXa9jVXa_.jpg', 'i3/TB1H9k1eYj1gK0jSZFuXXcrHpXa_.jpg', 'i1/TB1aT.We.Y1gK0jSZFMXXaWcVXa_.jpg', 'i2/TB16VuCfND1gK0jSZFyXXciOVXa_.jpg', 'i3/TB1wC9xfUT1gK0jSZFrXXcNCXXa_.jpg', 'i4/TB1zlCxfNz1gK0jSZSgXXavwpXa_.jpg', 'i4/TB1R65AfKL2gK0jSZFmXXc7iXXa_.jpg', 'i3/TB15DCvfFY7gK0jSZKzXXaikpXa_.jpg', 'i4/TB1UgayfQL0gK0jSZFAXXcA9pXa_.jpg'], 'imdbid': 'tt4844148', 'orderBy': 10000, 'backgroundPicture': 'i4/TB1U_WPeeH2gK0jSZFEXXcqMpXa_.jpg', 'features': {'openCountry': '中国大陆', 'year': '2019', 'topVideoPoster': 'i4/TB1FP_zybj1gK0jSZFOXXc7GpXa_.jpg', 'openTime': '2020', 'isReOpen': '0', 'configShowCode': '075101572019'}, 'fromSearch': False, 'openTime': '2020', 'fantastic': 0, 'userShowStatus': 0}

        """
        id = key.get('id')
        showname = key.get('showName')
        director = key.get('director')
        leadingRole = key.get('leadingRole')
        type = key.get('type')
        country = key.get('country')
        language = key.get('language')
        duration = key.get('duration')
        openDay = key.get('openDay')
        poster = key.get('poster')
        orderCount = key.get('orderCount')
        print(id, showname, director, leadingRole, type, country, language, duration, openDay, poster, orderCount)
    #     cursor.execute("INSERT INTO movies(id, showname, director, leadingRole, type, country, language, duration, openDay, poster, orderCount) VALUE (id, showname, director, leadingRole, type, country, language, duration, openDay, poster, orderCount);")
    #     client.commit()
    #
    # cursor.close()
    # client.close()
