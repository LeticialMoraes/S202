from biblioteca import Biblioteca

class BibliotecaCLI:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.comandos = {}
        self.adicionar_comandos()

    def adicionar_comandos(self):
        self.adicionar_comando("adicionar", self.adicionar_livro)
        self.adicionar_comando("listar", self.listar_livros)
        self.adicionar_comando("buscar", self.buscar_livro)
        self.adicionar_comando("atualizar", self.atualizar_livro)
        self.adicionar_comando("remover", self.remover_livro)
        self.adicionar_comando("sair", self.sair)

    def adicionar_comando(self, nome, funcao):
        self.comandos[nome] = funcao

    def adicionar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação: "))
        livro_id = self.biblioteca.adicionar_livro(titulo, autor, ano_publicacao)
        print(f"Livro adicionado com sucesso! ID: {livro_id}")

    def listar_livros(self):
        print("\nLista de livros na biblioteca:")
        livros = self.biblioteca.listar_livros()
        for livro in livros:
            print(f"ID: {livro['_id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano de Publicação: {livro['ano_publicacao']}")

    def buscar_livro(self):
        livro_id = input("Digite o ID do livro: ")
        livro = self.biblioteca.buscar_livro(livro_id)
        if livro:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}")
        else:
            print("Livro não encontrado.")

    def atualizar_livro(self):
        # Primeiro, listar todos os livros para que o usuário possa ver os IDs
        self.listar_livros()
        livro_id = input("Digite o ID do livro que deseja atualizar: ")
        campo = input("Digite o campo a ser atualizado (titulo, autor, ano_publicacao): ")
        novo_valor = input(f"Digite o novo valor para {campo}: ")
        update_data = {campo: novo_valor}
        if self.biblioteca.atualizar_livro(livro_id, update_data):
            print("Livro atualizado com sucesso.")
        else:
            print("Livro não encontrado.")

    def remover_livro(self):
        # Primeiro, listar todos os livros para que o usuário possa ver os IDs
        self.listar_livros()
        livro_id = input("Digite o ID do livro que deseja remover: ")
        if self.biblioteca.remover_livro(livro_id):
            print("Livro removido com sucesso.")
        else:
            print("Livro não encontrado.")

    def sair(self):
        print("Saindo do CLI da Biblioteca. Até logo!")
        exit()

    def executar(self):
        print("Bem-vindo ao CLI da Biblioteca!")
        print("Comandos disponíveis: adicionar, listar, buscar, atualizar, remover, sair")

        while True:
            comando = input("Digite um comando: ").strip().lower()

            if comando in self.comandos:
                self.comandos[comando]()
            else:
                print("Comando inválido. Tente novamente.")