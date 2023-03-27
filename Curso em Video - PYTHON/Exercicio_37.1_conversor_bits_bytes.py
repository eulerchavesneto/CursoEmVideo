opcao = int(input('''ESCOLHA A OPÇÃO QUE DESEJA:
[ 1 ] Quero converter de BIT para BYTE
[ 2 ] Quero converter de BYTE para BIT

'''))

num = int(input("Digite o numero que você quer converter"))


if opcao == 1:
    bytes = num / 8
    print("Você digitou {} bits, que equivale a {} bytes".format(num, bytes))

elif opcao == 2:
    bits = num * 8
    print("Você digitou {} bytes, que equivale a {} bits".format(num,bits))

else:
    print("Você não digitou nenhuma das opções, SEU MONSTRO")