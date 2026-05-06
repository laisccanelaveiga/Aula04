# anos_casa = float(input("Quantos anos de empresa você tem: "))

# if anos_casa >= 5:
#     print("Você receberá o bônus")

# else:
#     print("Não ganhará o bônus")

#--------------------------------------------------------------

#consumo maior que 12km/l menor / acima economico

distacia = float(input("Informe a distância percorrida (km): "))
combustivel = float(input("Quanto foi gasto (litros): "))

consumo = distacia / combustivel

if consumo >= 12:
    print(f'Carro econômico | {consumo:.1f} km/l')
else:
    print(f'Carro não econômico | {consumo:.1f} km/l') 

