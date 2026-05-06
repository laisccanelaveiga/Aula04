compra = float(input("Informe o valor da compra: "))
pgto = input("Forma de pagamento: ").strip().upper()
desconto = 0.16

if compra > 250 and pgto == "PIX":
    desconto = compra * desconto
    valor_final = compra - desconto
    print(f'Desconto Concedido: {desconto}')
    print(f'Valor após desconto: {valor_final}')

else:
    print(f'Valor à pagar: R$ {compra}')
    