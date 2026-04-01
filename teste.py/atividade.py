nota_prova = float(input("qual e sua nota da prova?"))
nota_projeto = float(input("qual e a nota do seu projeto?"))
frequencia = float(input(" qual e sua frequencia?"))
if (nota_prova >= 6 or nota_projeto >= 6) and frequencia >= 60:
    print("voce ta aprovado")
elif frequencia < 60:
    print("voce ta reprovado")
else:
    media = (nota_prova + nota_projeto) / 2  
    if media >= 7 and frequencia >= 60:
        print("aprovado")
    elif 5 <= media <= 6.9 and frequencia >= 60:
        print("recuperacao")
    else:
        print("reprovado por nota")

idade = int(input("Digite sua idade: "))
possui_premium = input("Possui assinatura premium? (sim/não): ")
if idade<=12:
    print("voce pode assitir conteudo de criança")
elif idade<17:
    print("voce pode assitir conteudo de adolecente")
elif idade>18:
    print("voce pode assitir conteudo de aduto e 18+")
elif possui_premium =="sim":
    print("voce pode assitir conteudo premium") 

distancia = float(input("qual e a distancia"))
chovendo = input("esta chovendo?")
pico = input("ta em horario de pico?")
if distancia > 20 and chovendo:
    risco = "o risco e alto"
elif (distancia > 20 or chovendo) or pico:
    risco = "o risco e médio"
else:
    risco = "o risco e baixo"
print(risco)

idade4=int(input("qual e a sua idade"))
peso=float(input("qual e seu peso "))
atestado=input("vc tem atestado seu gordo/magro")
if atestado =="nao":
  print("voce nao pode ")
elif atestado == "sim" and (idade4 >=18 and idade4 <= 40) and peso<= 120:
    print("voce tem permisao")
else:
    print("nao pode entrar")