from database import Database
from teacher_crud import TeacherCRUD

def main():

    
    crud = TeacherCRUD()
    
    while True:
        print("Escolha uma opcao:")
        print("1. Criar professor")
        print("2. Ler professor")
        print("3. Atualizar professor")
        print("4. Deletar professor")
        print("5. Sair")

        option = input("Opcao: ")

        if option.strip() == "1":
            name = input("Nome do Professor: ")
            ano_nasc = input("Ano de Nascimento: ")
            cpf = input("CPF: ")
            crud.create(name, int(ano_nasc), cpf)
            print("Professor criado com sucesso!")
        elif option.strip() == "2":
            name = input("Nome do Professor: ")
            professor = crud.read(name)
            if professor:
                print(f"Professor encontrado: {professor}")
            else:
                print("Professor nao encontrado.")
        elif option.strip() == "3":
            name = input("Nome do Professor: ")
            new_cpf = input("Novo CPF: ")
            crud.update(name, new_cpf)
            print("CPF do professor atualizado com sucesso!")
        elif option.strip() == "4":
            name = input("Nome do Professor: ")
            crud.delete(name)
            print("Professor deletado com sucesso!")
        elif option.strip() == "5":
            break
        else:
            print("Opcao inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()