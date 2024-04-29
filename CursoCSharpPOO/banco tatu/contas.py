class conta:
    def __init__(self, cliente, numero, saldo = 0):
        self.saldo = saldo
        self.cliente = cliente
        self.numero = numero
        self.operaçoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f'CC numero: {self.numero} saldo: {self.saldo: .2f}')
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operaçoes.append(['SAQUE', valor])
        else:
            print('saldo insuficiente')    

    def deposito(self,valor):
        self.saldo += valor
        self.operaçoes.append(['DEPOSITO', valor])

    def extrato(self):
        print(f'Extrato CC N°{self.numero}\n')
        for o in self.operaçoes:
            print(f'{o[0]: 10s} {0[1]: .2f}')
        print(f'\n saldo: {self.saldo: .2f}\n')  

