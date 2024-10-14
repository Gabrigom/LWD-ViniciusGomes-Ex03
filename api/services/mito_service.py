from api import mongo
from ..models import mito_model
from bson import ObjectId

class MitologiaService:
    def add_mito(mito):
        result = mongo.db.mitos.insert_one({
            'name' : mito.name,
            'deities' : mito.deities
        })
        return mongo.db.mitos.find_one({
            '_id': ObjectId(result.inserted_id)
        })
        
    @staticmethod
    def get_mitos():
        return list(mongo.db.mitos.find())
    
    @staticmethod
    def get_single_mito(id):
        return mongo.db.mitos.find_one({'_id': ObjectId(id)})
    
    def update_mito(self, id):
        updated_mito = mongo.db.mitos.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set' : {
                'name': self.name,
                'deities': self.deities
            }},
            return_document=True
        )
        return updated_mito
    
    @staticmethod
    def delete_mito(id):
        mongo.db.mitos.delete_one({'_id': ObjectId(id)})