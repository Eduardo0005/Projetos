#Calculadora

while True:
    number1 = input('Digite um valor: ')
    number2 = input('Digite um valor: ')
    print('1. Somar')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')
    operador = input('Digite um operador: ')

    numerosValidos = None
    number1_float = 0
    number2_float = 0

    try:
        number1_float = float(number1)
        number2_float = float(number2)
        numerosValidos = True
    except:
        numerosValidos = None

    if numerosValidos is None:
        print('Um ou ambos dos números são inválidos')
        continue


    operadoresValidos = '1,2,3,4,5'

    if operador not in operadoresValidos:
        print('Digite um operador valido!')
        continue

    # if len(operador) > 1:
    #     print('Digite apenas um operador')
    #     continue

    if operador == '5':
        print('Calculadora encerrada!')
        break

    if operador == '1':
        print(number1_float + number2_float)

    elif operador == '2':
        print(number1_float - number2_float)

    elif operador == '3':
        print(number1_float * number2_float)

    elif operador == '4':
        print(number1_float / number2_float)

    else:
        print('Você não deveria ter chegado aqui')


