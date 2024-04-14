class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, nome, corridas=None, nota=0.0):
        self.nome = nome
        self.corridas = corridas if corridas is not None else []
        self.nota = nota

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)

    def remover_corrida(self, corrida):
        self.corridas.remove(corrida)