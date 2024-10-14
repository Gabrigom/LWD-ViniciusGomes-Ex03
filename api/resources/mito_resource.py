from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..schemas import mito_schema
from ..models import mito_model
from ..services.mito_service import MitologiaService

class MitologiaList(Resource):
    def get(self):
        mitos = MitologiaService.get_mitos()
        mitoSch = mito_schema.MitologiaSchema(many=True)
        return make_response(mitoSch.jsonify(mitos), 200)
    
    def post(self):
        mitoschema = mito_schema.MitologiaSchema()
        validation = mitoschema.validate(request.json)
        if validation: # O validation sendo true indica que há erros no json de postagem (json_data)
            return make_response(jsonify(validation), 400)
        else:
            json_data = request.get_json()
            new_mito = mito_model.Mitologia(**json_data) 
            result = MitologiaService.add_mito(new_mito)
            pos = mitoschema.jsonify(result)
            return make_response(pos, 201)
        
class MitologiaDetails(Resource):
    def get(self, id):
        mito = MitologiaService.get_single_mito(id)
        if mito is None:
            return make_response(jsonify("Mitologia não encontrada"), 404)
        mitoschema = mito_schema.MitologiaSchema()
        return make_response(mitoschema.jsonify(mito), 200)
    
    def put(self, id):
        mito_ind = MitologiaService.get_single_mito(id)
        if mito_ind is None:
            return make_response(jsonify("Mitologia não encontrada"), 404)
        mitoschema = mito_schema.MitologiaSchema()
        validation = mitoschema.validate(request.json)
        if validation:
            return make_response(jsonify(validation), 400)
        else:
            for key, value in request.json.items():
                setattr(mito_ind, key, value)

            updated_mito = MitologiaService.update_mito(mito_ind)
            return make_response(mitoschema.jsonify(updated_mito), 201)
        
    def delete(self, id):
        mito_ind = MitologiaService.get_single_mito(id)
        if mito_ind is None:
            return make_response(jsonify("Mitologia não encontrada"), 404)
        MitologiaService.delete_mito(id)
        return make_response(jsonify("Mitologia excluída com sucesso"), 200)
        
api.add_resource(MitologiaList, '/mitologias')
api.add_resource(MitologiaDetails, '/mitologia/<id>')