from api import app, mongo
from api.models.mito_model import Mitologia
from api.services.mito_service import MitologiaService

if __name__ == "__main__":
    with app.app_context():
        if 'mitos' not in mongo.db.list_collection_names():
            mitologia = Mitologia(
                name='',
                deities=''
            )
            MitologiaService.add_mito(mitologia)
            
    app.run(port=4000, debug=True)