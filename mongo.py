import json

from pymongo import MongoClient


def sendMongo():
    cluster = MongoClient("url-mongo")

    db = cluster['test']

    collections = db['test']

    file = open('file_final_extracao2.json', 'r', encoding='utf-8')
    json_object = json.load(file)
    file.close()

    collections.insert_many(json_object)

    results = collections.find({})

    for i in results:
        print(i)

if __name__ == '__main__':
    sendMongo()
