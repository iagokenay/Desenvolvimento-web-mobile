#coleta de dados do usuario e logo apos usando com print

# nome = input("qual seu nome :") #input para fazer a coleta do usuario "nome" e variavel "=" siguinifica atribuido a .

# print(f"bem vindo {nome} seja feliz")# "print" e comando de emprimir oque estiver entre ( ) e "f" e formatação usamos para formata e incluir as variaveis dentro do print no caso sempre incluimos com {variavel} 

#agora uma coleta de duas informaçoes de diferentes tipos 

# idade =int(input("qual sua idade ?")) # usamos "int" para coleta uma tipo inteiro de variavel
# comida=input("qual sua comida favorita ?")

# print(f"voce tem {idade} e sua comida favorita e {comida} !!")

# senha = input("crie uma senha :")
# if len(senha) >= 6:
#     print("senha aceita !")
# else:
#    print("senha nao aceita digite novamente")

#agora vamos trabalhar com loops

# numero = 10 

# while numero >= 1 :      #while e um loop 
#     print(numero)
#     numero-=1            # para regredir e "-=" e para progreder "+=" 

#peça para o usuario o saldo de sua carteira e verifique que ele pode ou nao compra o produto x

# saldo = int(input("este produto custa 900$ \n qual seu saldo para adiquirir este produto?"))
# produto = 900
# if saldo >= produto:
#     print(f'compra de {produto}$ bem sucedida seu saldo atual e {saldo - produto}$')
# else:
#     print(f"saldo insuficiente peça um emprestimo com agiota")

#peça a idade do usuario e classifique em 3 classes

# idade = int(input('qual sua idade atual ?'))

# if idade < 13:
#     print(f"sua classe e mirim Criança!")
# elif idade <= 13 or idade <= 18:
#     print(f"aborrecenti padrao !")
# else:
#     print(f"tropa do ancião")

#  list []  tupla ()  dicionario {}
  
# crie uma lista e imprima ela
# list = ['morango','pera','uva','mamao','abacate']
# print(list)

#crie uma lista e imprima o segundo item da lista 

# list=["morango","uva","abacaxi"]
# print(list[1])

#crie uma lista de cores e subistitua uma delas 

# lista=['vermelho','verde','amarelo']
# print(lista)

# lista[1]="azul"

# print(lista)

# crie uma lista de animais e remova um 

# animais = ['cachorro','gato','peixe','dino']

# animais.remove('gato')

# print(animais)

# del animais[2]

# print(animais)

# animais.pop(1)

# print(animais)

#crie uma tupla e imprima um elemento

# frutas = ('uva','abacaxi','morango')

# print(frutas[1])

# prova pythom
# 1
# nome=input('quual seu nome ?')
# idade=int(input('qual sua idade ?'))
# altura=float(input('qual sua altuura ?'))


# print(f'bem vindo {nome} sua idade e {idade} e voce ja tem {altura} de altura!')

# 2

# n1=int(input('numero 1 :'))
# n2=int(input('numero 2 :'))
# mutiplica = n1 * n2
# print(f'a mutiplicaçao dos numeros e {mutiplica}' )

#3

# n1=int(input('numero  :'))

# if n1 % 2 == 0 :
#     print('par')
# else:
#     print('impar')

#4
# print('defina a base e altura de um triangulo') 
# n1=float(input('base :'))
# n2=float(input('altura :'))
# ba = n1*n2
# print(f'a area do triangulo e {ba}')

#5

# metro = float(input('digite um valor em metros:'))

# cent = metro*1000

# print(f'{metro} metros e igual a {cent} centimetros')

#6

# n1= int(input('digite um valor'))
# n2= int(input('digite um valor'))
# n3= int(input('digite um valor'))

# if n1 > n2 and n1 > n3:
#     print(f'{n1}e maior !')
# elif n2 > n1 and n2 > n3 :
#     print(f'{n2}e maior !')
# else:
#     print(f'{n3}e maior !')

#7
# numero = 1
# while numero <= 10 :
#     print(numero)
#     numero+=1

#8

# lista = ['azul','amarelo','verde']
# print(lista)

#9

#lista = [1,1,1,4,5,6,]

#print(lista.count(1))

#10

# lista = [1,2,3,4,5,6,]
# print(lista)