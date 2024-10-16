from api import mm
from marshmallow import Schema, fields

class MitologiaSchema(mm.Schema):
    class Meta:
        fields = ('_id', 'name', 'deities')
        
    _id = fields.Str()
    name = fields.Str(required=True)
    deities = fields.Dict(required=True)