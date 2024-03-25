from database import Database
from helper.writeAJson import writeAJson
from pymongo import MongoClient

# Importando a classe LivrosCollection
from livrosCollection import LivrosCollection

def main():
    # Conectando ao banco de dados MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = Database(database="Biblioteca", collection="livros")

    # Instanciando a classe LivrosCollection
    livros_collection = LivrosCollection(db)

    # Exemplo de chamada das funções
    livro_id = livros_collection.create_livro(_id="1", titulo="Clean Code", autor="Robert C. Martin", ano=2008, preco=31.0)
    livro = livros_collection.read_livro_by_id("1")
    livros_collection.update_livro(_id="1", titulo="Clean Code: A Handbook of Agile Software Craftsmanship", autor="Robert C. Martin", ano=2008, preco=35.0)
    livros_collection.delete_livro("1")

    # Fechando a conexão com o banco de dados
    client.close()
