import random
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$♠️   jogo de adivinhação    ♥️ $")
print("$♠️           do             ♥️ $")
print("$♠️          Rick            ♥️ $")
print("$⚜️                          〽️$")
print("$⚜️       31/07/2025         〽️$")
print("$⚜️                          〽️$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

numeroSecreto= random.randrange(0,100)
ToltalTentativas = 0
pontos = 100

print(" Qual níveis de dificuldade?")
print("(1)- Fácil (2)- Médio (3)- Dificil")

nivel  = int(input(" Escolha um nível:"))
if nivel == 1: 
    print("você está fraco 😂")
    ToltalTentativas = 20
elif nivel == 2:
    print("tá ficando bom, mas continua fraco 🙃")
    ToltalTentativas = 10
elif nivel == 3:
    print("uau você é fera!😱")
    ToltalTentativas = 5
else:
    print("esse nível não existe 😞")
for rodada in range (1,ToltalTentativas +1):
    print("tentativa {} de {}".format(rodada,ToltalTentativas) )
    chute_str =  input("digite um número entre 1 e 100: ")
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("Número invalido")
        continue
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto
    if(acertou):
        print(f"você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o numero secreto")
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos = pontosPerdidos
print("fim de jogo! o numero era ",numeroSecreto)