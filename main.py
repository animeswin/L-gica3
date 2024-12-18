numero_secreto = 7
tentativas_max = 3
tentativas = 0

while tentativas < tentativas_max:
    tentativa = int(input("Adivinhe o número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Parabéns! Você adivinhou o número!")
        break
    elif tentativa < numero_secreto:
        print("O número é maior do que sua tentativa.")
    else:
        print("O número é menor do que sua tentativa.")
else:
    print("Que pena! Você não conseguiu adivinhar o número. O número era:", numero_secreto)