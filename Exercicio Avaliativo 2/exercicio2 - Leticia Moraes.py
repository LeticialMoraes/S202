from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# Classe para o Client de consulta ao Neo4j
class Neo4jClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=True)

    def close(self):
        self._driver.close()

    def execute_query(self, query):
        with self._driver.session() as session:
            result = session.run(query)
            return result.data()

# Configurações de conexão ao seu banco de dados Neo4j
uri = "neo4j+s://96b60228.databases.neo4j.io"  # URI do seu banco de dados Neo4j
user = "neo4j"  # Usuário do seu banco de dados Neo4j
password = "6n57xnHrvUccE5Q8N-UE_gvLdXxHxha1K-8tbOarP5Y"  # Senha do seu banco de dados Neo4j

# Inicializa o cliente de consulta ao Neo4j
client = Neo4jClient(uri, user, password)

try:
    # Exemplo de perguntas e consultas
    perguntas_consultas = [
        ("Quem são os membros da família?", "MATCH (p:Pessoa:Familiar) RETURN p.nome"),
        ("Qual é a idade de cada membro da família?", "MATCH (p:Pessoa:Familiar) RETURN p.nome, p.idade"),
        ("Quem são os pais de Leticia?", "MATCH (p1)-[:PAI_DE]->(p2 {nome: 'Leticia'}) RETURN p1.nome"),
        ("Quem é o irmão de Leticia?", "MATCH (p1 {nome: 'Leticia'})-[:IRMAO_DE]->(p2) RETURN p2.nome"),
        ("Quem é o tio de Leticia?", "MATCH (tio)-[:TIO_DE]->(:Pessoa {nome: 'Leticia'}) RETURN tio.nome"),
        ("Quais são os animais de estimação da Leticia?", "MATCH (p:Pessoa {nome: 'Leticia'})-[:DONO_DE]->(pet:Pet:Animal) RETURN pet.nome"),
        ("Quem está casado na família?", "MATCH (p1)-[:CASADO_COM]->(p2) RETURN p1.nome, p2.nome"),
        ("Quem são os cônjuges na família?", "MATCH (p1)-[:CASADO_COM]->(p2) RETURN p1.nome, p2.nome")
    ]

    # Executa cada consulta e exibe os resultados
    for pergunta, consulta in perguntas_consultas:
        print(f"Pergunta: {pergunta}")
        resultado = client.execute_query(consulta)
        if resultado:
            print("Resultado:")
            for record in resultado:
                print(record)
        else:
            print("Nenhum resultado encontrado.")

except Exception as e:
    print(f"Erro ao executar consulta: {e}")

finally:
    # Fecha a conexão com o Neo4j ao finalizar
    client.close()
