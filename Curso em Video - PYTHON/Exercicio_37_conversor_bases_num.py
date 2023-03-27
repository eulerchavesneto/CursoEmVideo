num = int(input("Digite um numero inteiro qualquer: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")
opcao = int(input("Sua opção: "))

if opcao == 1:
    binario = format(num, "b")
    print("{} convertido para BINARIO É IGUAL a {}".format(num, binario))
# Também seria possível colocando no final do print o .format(num, bin(num)); nesse caso, não precisaria criar a var bin

elif opcao == 2:
    octal = format(num, "o")
    print("{} convertido para OCTAL É IGUAL a {}".format(num, octal))
# Também seria possível colocando no final do print o .format(num, oct(num)); nesse caso, não precisaria criar a var oct

elif opcao == 3:
    hex = format(num, "x")
    print("{} convertido para HEXADECIMAL É IGUAL a {}".format(num, hex))
# Também seria possível colocando no final do print o .format(num, hex(num)); nesse caso, não precisaria criar a var hex

else:
    print("OPÇÃO INVÁLIDA")