from project.factory.database import Database

class TodoHPPOSLLH(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'NAV_HPPOSLLH'  # collection name
        
        self.fields = {
            "version": "string",
            "invalidLlh": "string",
            "iTOW": "string",
            "lon": "string",
            "lat": "string",
            "height": "string",
            "hMSL": "string",
            "hAcc": "string",
            "vAcc": "string"
        }
    def create(self, todo):
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res
    
    def query1(self, todo):
        res = self.db.query1(todo, self.collection_name)
        return res

    def query2(self, todo):
        res = self.db.query2(todo, self.collection_name)
        return res

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def update(self, id, todo):
        return self.db.update(id, todo,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
    

class TodoSTASUS(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'NAV_STATUS'  # collection name
        
        self.fields = {     
            "iTOW": "string",
            "gpsFix": "string",
            "flags": "string",
            "fixStat": "string",
            "flags2": "string",
            "ttff": "string",
            "msss": "string"    
        }
    def create(self, todo):
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def update(self, id, todo):
        return self.db.update(id, todo,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
    

class TodoHPPOSECEF(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'NAV_HPPOSECEF'  # collection name
        
        self.fields = {     
            "version": "string",
            "iTOW": "string",
            "ecefX": "string",
            "ecefY": "string",
            "ecefZ": "string",
            "ecefXHp": "string",
            "ecefYHp": "string",
            "ecefZHp": "string",
            "invalidEcef": "string",
            "pAcc": "string",  
        }
    def create(self, todo):
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def update(self, id, todo):
        return self.db.update(id, todo,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
        

