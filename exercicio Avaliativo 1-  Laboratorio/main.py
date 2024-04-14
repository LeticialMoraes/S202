# main.py
import pymongo
from database import Database
from MotoristaCLI import MotoristaCLI
from MotoristaDAO import MotoristaDAO
from writeAJson import writeAJson
from classes import Motorista, Corrida, Passageiro

def main():
    nome_banco = "atlas-cluster"
    nome_colecao = "Motorista"

    try:
        # Conectar ao servidor MongoDB
        connectionString = "mongodb+srv://root:root@cluster0.hcb8ghs.mongodb.net/"
        client = pymongo.MongoClient(connectionString, tlsAllowInvalidCertificates=True)
    

        db = client['atlas-cluster']
        motorista_dao = MotoristaDAO(db)
        motorista_cli = MotoristaCLI(motorista_dao)
        motorista_cli.executar()

        # Após interagir com os dados, exportar para JSON (exemplo)
        json_writer = writeAJson()
        json_writer.export_to_json(db.collection, "motorista.json")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    main()

    
