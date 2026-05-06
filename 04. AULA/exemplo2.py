
tempo = float(input("Tempo de casa: "))
setor = input("Setor: ").upper()
salario = float(input("Salário: "))

if setor == "A" and tempo >= 3:
    aumento = salario * 0.18
    reajuste = "18%"

else:
    aumento = salario * 0.09
    reajuste = "9%"

novo_salario = salario + aumento

print("\n=== Resultado ===")
print(f'Aumento: {aumento}')
print(f'Reajuste: {reajuste} ')
print(f'Salário Reajustado: {novo_salario}')
