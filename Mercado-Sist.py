from datetime import datetime

class Transacao:
    def __init__(self, valor, data, descricao):
        self.valor = valor
        self.data = data
        self.descricao = descricao

class ContaPagar(Transacao):
    def __init__(self, valor, data, descricao):
        super().__init__(valor, data, descricao)
        
class ContaReceber(Transacao):
    def __init__(self, valor, data, descricao):
        super().__init__(valor, data, descricao)

class SistemaFinanceiro:
    def __init__(self):
        self.contas_pagar = []
        self.contas_receber = []
        
    def registrar_conta_pagar(self, valor, data, descricao):
        if not self.validar_data(data):
            print("Formato de data incorreto. Por favor, insira a data no formato DD/MM/AAAA.")
            return
        conta_pagar = ContaPagar(valor, data, descricao)
        self.contas_pagar.append(conta_pagar)
        
    def registrar_conta_receber(self, valor, data, descricao):
        if not self.validar_data(data):
            print("Formato de data incorreto. Por favor, insira a data no formato DD/MM/AAAA.")
            return
        conta_receber = ContaReceber(valor, data, descricao)
        self.contas_receber.append(conta_receber)
        
    def visualizar_contas_pagar(self):
        print("Contas a Pagar:")
        for conta in self.contas_pagar:
            print(f"Valor: R${conta.valor}, Data de Vencimento: {conta.data}, Descrição: {conta.descricao}")
            
    def visualizar_contas_receber(self):
        print("Contas a Receber:")
        for conta in self.contas_receber:
            print(f"Valor: R${conta.valor}, Data Prevista de Recebimento: {conta.data}, Descrição: {conta.descricao}")
    
    def calcular_saldo_atual(self):
        saldo_pagar = sum(conta.valor for conta in self.contas_pagar)
        saldo_receber = sum(conta.valor for conta in self.contas_receber)
        saldo_atual = saldo_receber - saldo_pagar
        print(f"Saldo Atual: R${saldo_atual}")
        
    def validar_data(self, data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

# Função para exibir o menu
def exibir_menu():
    print("\n=== Menu ===")
    print("1. Registrar Conta a Pagar")
    print("2. Registrar Conta a Receber")
    print("3. Visualizar Contas a Pagar")
    print("4. Visualizar Contas a Receber")
    print("5. Calcular Saldo Atual")
    print("6. Sair")

# Função principal
def main():
    sistema_financeiro = SistemaFinanceiro()
    
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            valor = float(input("Digite o valor da conta a pagar: "))
            data = input("Informe a data de vencimento, seguindo o exemplo, DD/MM/AAAA: ")
            descricao = input("Digite uma breve descrição: ")
            sistema_financeiro.registrar_conta_pagar(valor, data, descricao)
        elif escolha == "2":
            valor = float(input("Digite o valor da conta a receber: "))
            data = input("Informe a data prevista de recebimento, seguindo o exemplo, DD/MM/AAAA: ")
            descricao = input("Digite uma breve descrição: ")
            sistema_financeiro.registrar_conta_receber(valor, data, descricao)
        elif escolha == "3":
            sistema_financeiro.visualizar_contas_pagar()
        elif escolha == "4":
            sistema_financeiro.visualizar_contas_receber()
        elif escolha == "5":
            sistema_financeiro.calcular_saldo_atual()
        elif escolha == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
