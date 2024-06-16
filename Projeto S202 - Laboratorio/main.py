import pymongo
from pymongo import MongoClient
from database import Database
from BibliotecaCLI import BibliotecaCLI
from LivroDAO import LivrosDAO # Ajuste o nome do arquivo importado
from writeAJson import writeAJson

def main():
    nome_banco = "atlas-cluster"
    nome_colecao = "Biblioteca"

    try:
        # Conectar ao servidor MongoDB
        connectionString = "mongodb+srv://root:root@cluster0.hcb8ghs.mongodb.net/"
        client = pymongo.MongoClient(connectionString, tlsAllowInvalidCertificates=True)


        db = client['atlas-cluster']
        livro_dao = LivrosDAO(db)  # Instanciar a classe Biblioteca corretamente
        biblioteca_cli = BibliotecaCLI(livro_dao)  # Passar a instância da Biblioteca para o CLI
        biblioteca_cli.executar()  # Chamar o método executar

        # Após interagir com os dados, exportar para JSON (exemplo)
        json_writer = writeAJson()
        json_writer.export_to_json(db.get_collection, "biblioteca.json")  # Corrigido para usar a coleção correta

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    main()