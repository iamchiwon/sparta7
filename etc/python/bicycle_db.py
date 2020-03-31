import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta.bicycle


def scrap_and_insert():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
    rjson = r.json()

    rentBikeStatus = rjson['rentBikeStatus']
    rows = rentBikeStatus['row']

    for row in rows:
        station = row['stationName'].split('. ')[1]
        parked = row['parkingBikeTotCnt']
        total = row['rackTotCnt']

        # 망원역 1번출구 앞 ( 9/22 )
        print('{} ( {}/{} )'.format(station, parked, total))

        data = {'station': station, 'parked': parked, 'total': total}
        db.insert_one(data)


def read_and_print():
    all = list(db.find())
    for one in all:
        station = one['station']
        parked = one['parked']
        total = one['total']
        print('{} ( {}/{} )'.format(station, parked, total))


read_and_print()
