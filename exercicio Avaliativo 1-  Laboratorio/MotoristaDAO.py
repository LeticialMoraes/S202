from bson import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.collection = database['Motorista']

    def create_motorista(self, nome, nota):
        motorista_data = {
            "nome": nome,
            "nota": nota,
            "corridas": []  # Inicialmente vazio
        }
        result = self.collection.insert_one(motorista_data)
        return str(result.inserted_id)

    def add_corrida_to_motorista(self, motorista_id, corrida_data):
        result = self.collection.update_one(
            {'_id': ObjectId(motorista_id)},
            {'$push': {'corridas': corrida_data}}
        )
        return result.modified_count > 0

    def listar_motoristas(self):
        motoristas = list(self.collection.find())
        return motoristas

    def update_motorista(self, motorista_id, update_data):
        result = self.collection.update_one({'_id': ObjectId(motorista_id)}, {'$set': update_data})
        return result.modified_count > 0

    def delete_motorista(self, motorista_id):
        result = self.collection.delete_one({'_id': ObjectId(motorista_id)})
        return result.deleted_count > 0
