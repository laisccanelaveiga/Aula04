print('''
[1] - Marketing
[2] - Financeiro
[3 a 5] - Adm
[6 a 9] - TI
[10 a 20] - Serviços Gerais
''')

escolha = int(input("Escolha uma opção: "))

match escolha:
    
    case 1:
        print('Marketing')
    
    case 2:
        print("Financeiro")
    
    case 3 | 4 | 5:
        print("Adm")
    
    case numero if 6 <= numero <= 9:
        print("TI")
    
    case numero if 10 <= numero <= 20:
        print("Serviços Gerais")

    case _:
        print("Escolha inválida")