#from bson import ObjectId
import pymongo


#import project.models.config as config


class Database(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)  # configure db url
        self.db = self.client['db_sad']  # configure db name
    def insert(self, element, collection_name):
        #inserted = self.db[collection_name].insert_one(element)  # insert data to db
        inserted = self.db[collection_name].update( {'iTOW': element['iTOW']} ,element, upsert= True)
        return str(inserted)

    
    def query1(self, element, collection_name):
        q1 = self.db[collection_name].aggregate([
    {
        '$lookup': {
            'from': 'NAV_STATUS', 
            'localField': 'iTOW', 
            'foreignField': 'iTOW', 
            'as': 'NAV_STATUS'
        }
    }, {
        '$project': {
            '_id': 0,
            'iTOW': 1,
            'lon': 1,
            'lat': 1,
            'height': 1,
            'NAV_STATUS.gpsFix': 1
            }
        },{
        '$sort': {
            'iTOW': -1
             }
        },
    ])
        result_list = list(q1)
        return result_list
    
    
    def query2(self, element, collection_name):
        q2 = self.db[collection_name].aggregate([
    {
        '$project': {
            '_id': 0,
            'iTOW': 1,
            'lon': 1,
            'lat': 1
            }
        },{
        '$sort': {
            'iTOW': -1
             }
        },{ '$limit' : 3 }
    ])
        result_list = list(q2)
        return result_list


    
    
    
    
