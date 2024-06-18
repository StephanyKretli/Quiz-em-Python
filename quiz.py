print("SEJA MUITO BEM VINDO AO QUIZ DA STEPHANY :)")
answer_user = input("Deseja começar? (sim/não) ")
print(answer_user)

if answer_user != "sim":
    print ("Tudo bem, até a próxima!")
    quit()

score = 0

print("Então vamos lá...")

print("1. Quantas linhas tem no logo do serviço de streaming de música Spotify? \n A) 2 linhas \n B) 4 linhas \n C) 3 linhas \n D) 1 linha \n")
answer_1 = input ("Resposta: ")

if answer_1 == "C":
    print("Correto! :D")
    score = score + 1
else:
    print("Errou! :(")
    print("Vamos para a próxima")

print("2. Qual animal representa o símbolo da paz? \n A) Galinha \n B) Polvo \n C) Jumento \n D) Pomba \n")
answer_1 = input ("Resposta: ")

if answer_1 == "D":
    print("Correto! :D")
    score = score + 1
else:
    print("Errou! :(")
    print("Vamos para a próxima")

print("3. Qual é o animal que aparece no logotipo da Ferrari? \n A) Leão \n B) Cavalo \n C) Tigre \n D) Leopardo \n")
answer_1 = input ("Resposta: ")

if answer_1 == "B":
    print("Correto! :D")
    score = score + 1
else:
    print("Errou! :(")
    print("Vamos para a próxima")

print("4. Qual é o nome do inventor do telefone? \n A) Thomas Edison \n B) Alexander Graham Bell \n C) Nikola Tesla \n D) Guglielmo Marconi \n")
answer_1 = input ("Resposta: ")

if answer_1 == "A":
    print("Correto! :D")
    score = score + 1
else:
    print("Errou! :(")
    print("Vamos para a próxima")

print("5. Quantos dias tem um ano bissexto? \n A) 364 dias \n B) 365 dias \n C) 366 dias \n D) 367 dias \n")
answer_1 = input ("Resposta: ")

if answer_1 == "C":
    print("Correto! :D")
    score = score + 1
else:
    print("Errou! :(")
   
print (f"Acabou o quis! \n Sua pontuação foi: {score}/5")