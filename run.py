from api import app, mongo
from api.models.mito_model import Mitologia
from api.services.mito_service import MitologiaService
import logging

if __name__ == "__main__":
    with app.app_context():
        if 'mitos' not in mongo.db.list_collection_names():
            mitologia = Mitologia(
                name='penis',
                deities=''
            )
            MitologiaService.add_mito(mitologia)
            
    app.run(port=4000, debug=False)