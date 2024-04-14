from classes import Motorista, Corrida, Passageiro
from MotoristaDAO import MotoristaDAO

class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao
        self.comandos = {}
        self.adicionar_comandos()

    def adicionar_comandos(self):
        self.adicionar_comando("criar", self.criar_motorista)
        self.adicionar_comando("listar", self.listar_motoristas)
        self.adicionar_comando("atualizar", self.atualizar_motorista)
        self.adicionar_comando("deletar", self.deletar_motorista)
        self.adicionar_comando("sair", self.sair)

    def adicionar_comando(self, nome, funcao):
        self.comandos[nome] = funcao

    def criar_motorista(self):
        nome = input("Digite o nome do motorista: ")
        nota = float(input("Digite a nota do motorista: "))

        # Criar o motorista
        motorista_id = self.motorista_dao.create_motorista(nome, nota)
        print(f"Motorista criado com ID: {motorista_id}")

        while True:
            corrida_nota = float(input("Digite a nota da corrida: "))
            corrida_distancia = float(input("Digite a distância da corrida: "))
            corrida_valor = float(input("Digite o valor da corrida: "))
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")

            corrida_data = {
                "nota": corrida_nota,
                "distancia": corrida_distancia,
                "valor": corrida_valor,
                "passageiro": {
                    "nome": nome_passageiro,
                    "documento": documento_passageiro
                }
            }

            # Adicionar a corrida ao motorista
            if self.motorista_dao.add_corrida_to_motorista(motorista_id, corrida_data):
                print("Corrida associada ao motorista.")
            else:
                print("Erro ao associar corrida ao motorista.")

            continuar = input("Deseja adicionar outra corrida? (s/n): ").lower()
            if continuar != 's':
                break

    def listar_motoristas(self):
        motoristas = self.motorista_dao.listar_motoristas()
        if motoristas:
            print("\n=== Lista de Motoristas ===")
            for motorista in motoristas:
                print(f"ID: {motorista['_id']}, Nome: {motorista['nome']}, Nota: {motorista['nota']}")
                if motorista.get('corridas'):
                    print("Corridas:")
                    for corrida in motorista['corridas']:
                        print(f"Nota: {corrida['nota']}, Distância: {corrida['distancia']}, Valor: {corrida['valor']}")
                        if corrida.get('passageiro'):
                            print(f"Passageiro: {corrida['passageiro']['nome']} ({corrida['passageiro']['documento']})")
                else:
                    print("Nenhuma corrida associada a este motorista.")
        else:
            print("Nenhum motorista encontrado.")

    def atualizar_motorista(self):
        motorista_id = input("Digite o ID do motorista que deseja atualizar: ")
        nome = input("Digite o novo nome do motorista: ")
        nota = float(input("Digite a nova nota do motorista: "))
        update_data = {"nome": nome, "nota": nota}
        if self.motorista_dao.update_motorista(motorista_id, update_data):
            print("Motorista atualizado com sucesso!")
        else:
            print("Falha ao atualizar o motorista. ID não encontrado.")

    def deletar_motorista(self):
        motorista_id = input("Digite o ID do motorista que deseja deletar: ")
        if self.motorista_dao.delete_motorista(motorista_id):
            print("Motorista deletado com sucesso!")
        else:
            print("Falha ao deletar o motorista. ID não encontrado.")

    def sair(self):
        print("Saindo do CLI de Motoristas. Até logo!")

    def executar(self):
        print("Bem-vindo ao CLI de Motoristas!")
        print("Comandos disponíveis: criar, listar, atualizar, deletar, sair")

        while True:
            comando = input("Digite um comando: ").strip().lower()

            if comando in self.comandos:
                self.comandos[comando]()
            else:
                print("Comando inválido. Tente novamente.")