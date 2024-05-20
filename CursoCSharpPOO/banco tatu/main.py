from bancotatu import cliente
from contas import conta




pedro = cliente('pedrinho noiado', 9090190)
joao = cliente('joao do gas', 40028922)
maria = cliente('maria quenga', 15926357 )


cont_pedro = conta(pedro, 157, 33)
cont_joao = conta(joao, 123, 10000)
cont_maria = conta(maria, 190, 1000000)
print('-----------------------------------------------')
print('Contas disponiveis no banco TATU')
print(f'Conta titular://{cont_pedro.cliente.nome}// N°{cont_pedro.numero}//saldo R$ {cont_pedro.saldo} //')
print(f'Conta titular://{cont_joao.cliente.nome}// N°{cont_joao.numero}//saldo R$ {cont_joao.saldo} //')
print(f'Conta titular://{cont_maria.cliente.nome}// N°{cont_maria.numero}//saldo R$ {cont_maria.saldo} //')
print('-----------------------------------------------')
print('Pedro fez um deposito de procedencia duvidosa ')
cont_pedro.deposito(60), cont_pedro.resumo()
print('joao do gas recebeu um golpe do valor de 60 reais')
cont_joao.saque(60), cont_joao.resumo()
print('maria tem mais dinheiro a cada noite')
cont_maria.deposito(100),cont_maria.resumo
print('-----------------------------------------------')
print(cont_pedro.cliente.nome, 'tenta sacar 100$')
cont_pedro.saque(100),cont_pedro.resumo()
print('-----------------------------------------------')
