class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 5:
            print('Número máximo diário de transações atingido.')
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)