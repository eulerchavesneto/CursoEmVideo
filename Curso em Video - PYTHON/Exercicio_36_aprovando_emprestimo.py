valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
duracao = int(input("Em quantos anos você vai pagar?"))

maximo_prestacao = salario * 30/100

parcela = valor_casa / (duracao * 12)
parcela = float(parcela)


if parcela <= maximo_prestacao:
    print("EMPRESTIMO CONCEDIDO!")
    print("O valor da prestação mensal é de {:.2f}".format(parcela))

else:
    print("EMPRESTIMO NEGADO!")

print("O maximo que você pode pagar é R${:.2f}".format(maximo_prestacao))
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor_casa, duracao, parcela))