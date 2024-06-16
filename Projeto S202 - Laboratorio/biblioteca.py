from LivroDAO import LivrosDAO

class Biblioteca:
    def __init__(self, database):
        self.livro_dao = LivrosDAO(database)

    def adicionar_livro(self, titulo, autor, ano_publicacao):
        return self.livro_dao.create_livro(titulo, autor, ano_publicacao)

    def listar_livros(self):
        return self.livro_dao.listar_livros()

    def buscar_livro(self, livro_id):
        return self.livro_dao.get_livro(livro_id)

    def atualizar_livro(self, livro_id, update_data):
        return self.livro_dao.update_livro(livro_id, update_data)

    def remover_livro(self, livro_id):
        return self.livro_dao.delete_livro(livro_id)