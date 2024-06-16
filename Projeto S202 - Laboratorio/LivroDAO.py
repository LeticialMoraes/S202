from bson import ObjectId
from classes import Livro

class LivrosDAO:
    def __init__(self, database):
        self.collection = database['Biblioteca']

    def adicionar_livro(self, titulo, autor, ano_publicacao):
        livro_data = {
            "titulo": titulo,
            "autor": autor,
            "ano_publicacao": ano_publicacao
        }
        result = self.collection.insert_one(livro_data)
        return str(result.inserted_id)

    def buscar_livro(self, livro_id):
        data = self.collection.find_one({'_id': ObjectId(livro_id)})
        if data:
            return Livro(data['titulo'], data['autor'], data['ano_publicacao'])
        return None

    def listar_livros(self):
        livros = list(self.collection.find())
        return livros

    def atualizar_livro(self, livro_id, update_data):
        result = self.collection.update_one({'_id': ObjectId(livro_id)}, {'$set': update_data})
        return result.modified_count > 0

    def remover_livro(self, livro_id):
        result = self.collection.delete_one({'_id': ObjectId(livro_id)})
        return result.deleted_count > 0