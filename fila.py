import heapq

class ProntoSocorro:
    def __init__(self):
        self.fila_prioridade = []
        self.contador_pacientes = 0

    def agendar_atendimento(self, nome, prioridade):
        self.contador_pacientes += 1
        paciente = (prioridade, self.contador_pacientes, nome)
        heapq.heappush(self.fila_prioridade, paciente)
        print(f"Paciente {nome} agendado com prioridade {prioridade}.")

    def chamar_proximo_paciente(self):
        if not self.fila_prioridade:
            print("Não tem pacientes na fila.")
            return
        prioridade, _, nome = heapq.heappop(self.fila_prioridade)
        print(f"Chamando o próximo paciente: {nome} (prioridade {prioridade}).")

    def excluir_agendamentos(self):
        self.fila_prioridade.clear()
        print("Foi eliminado todos os agendamentos.")

if __name__ == "__main__":
    pronto_socorro = ProntoSocorro()

    while True:
        print("\nMenu:")
        print("1 - Agendar atendimento")
        print("2 - Chamar próximo paciente")
        print("3 - Excluir agendamentos")
        print("4 - Sair do programa")

        opcao = int(input("Digite a opção:"))

        if opcao == 1:
            nome = input("Digite o nome do paciente: ")
            prioridade = int(input("Digite a prioridade (1 - Crítico, 2 - Grave, 3 - Leve): "))
            pronto_socorro.agendar_atendimento(nome, prioridade)
        elif opcao == 2:
            pronto_socorro.chamar_proximo_paciente()
        elif opcao == 3:
            pronto_socorro.excluir_agendamentos()
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")