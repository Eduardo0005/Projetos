class Funcionario:
    def __init__(self,nome, idade, cargo, cpf, matricula, nascimento):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.cpf = cpf
        self.matricula = matricula
        self.nascimento = nascimento

def cadastrar_funcionario():
    nome = input('Digite o seu nome: ')
    idade = input('Digite a sua idade: ')
    cargo = input('Digite o seu cargo: ')
    cpf = input('Digite o seu CPF: ')
    matricula = input('Digite sua matricula: ')
    nascimento = input('Digite a data do seu nascimento: ')

    novo_funcionario = Funcionario(nome, idade,cargo, cpf, matricula, nascimento)
    return novo_funcionario

def listar_funcionario(funcionarios):
    print("\nLista de Funcionários: ")
    for i, funcionario in enumerate(funcionarios, start=1):
        print(f'{i}. Nome {funcionario.nome}, Idade: {funcionario.idade}, Cargo: {funcionario.cargo}, CPF: {funcionario.cpf},'
              f'Matricula: {funcionario.matricula}, Nascimento: {funcionario.nascimento}')

def main():
    funcionarios =[]


    while True:
        print("\nOpções: ")
        print('1. Cadastrar novo funcionário')
        print('2. Listar funcionário')
        print('3. Sair')

        opcao = int(input("Esolha uma opção: "))

        if opcao == 1:
            novo_funcionario = cadastrar_funcionario()
            funcionarios.append(novo_funcionario)
            print('Funcionário cadastrado com sucesso!')
        elif opcao == 2:
            if funcionarios:
                listar_funcionario(funcionarios)
            else:
                print('Nenhum funcionário cadastrado')

        elif opcao == 3:
            print('Saindo....')
            break

        else:
            print('Opção invalida...')


if __name__ =="__main__":
    main()