peso = float(input("Qual o seu peso?"))
idade = float(input("Qual a sua idade?"))
condicao = input("Você está doente? (Resfriado, gripado ou outros) ")

if peso > 50 and idade > 16 < 69 and condicao == "Não":
    print ("Você pode doar sangue.")
else:
    print ("Você não pode doar sangue.")