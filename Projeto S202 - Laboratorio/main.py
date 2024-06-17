import pymongo
from pymongo import MongoClient
from database import Database
from BibliotecaCLI import BibliotecaCLI
from LivroDAO import LivrosDAO
from writeAJson import writeAJson

def main():
    nome_banco = "atlas-cluster"
    nome_colecao = "Biblioteca"

    try:
        # Conectar ao servidor MongoDB
        connectionString = "mongodb+srv://root:root@cluster0.hcb8ghs.mongodb.net/"
        client = pymongo.MongoClient(connectionString, tlsAllowInvalidCertificates=True)


        db = client['atlas-cluster']
        livro_dao = LivrosDAO(db) 
        biblioteca_cli = BibliotecaCLI(livro_dao) 
        biblioteca_cli.executar()  

    
        json_writer = writeAJson()
        json_writer.export_to_json(db.get_collection, "biblioteca.json")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    main()
