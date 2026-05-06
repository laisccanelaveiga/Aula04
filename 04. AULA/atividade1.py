salario = float(input("Informe seu salário: "))
vendas = float(input("Informe o valor de vendas do mês: "))

if vendas > 1000:
    bonus = 100
    print("\nParabéns! Você bateu a meta!\n")
else:
    bonus = 20
    print("\nTente melhorar no próximo mês!\n")


print("-" * 30)
print("Resumo de Salário")
print(f'Salário inicial: R$ {salario:.2f}')
print(f'Valor do bônus: R$ {bonus:.2f}')
print(f'Salário Final: R$ {(salario + bonus):.2f}')
print("-" * 30)
