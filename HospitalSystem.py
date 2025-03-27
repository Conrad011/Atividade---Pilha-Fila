import sys 
sys.stdout.reconfigure(encoding='utf-8') # Essa importação foi para que o texto fique no padrão utf-8 e reconheça a acentuação quando for impresso no terminal
class HospitalSystem:
    def __init__(self): # Inicializando uma fila de pacientes, o contador de senhas e o histórico de chamada
        self.queue = []
        self.passwordCounter = 1
        self.callHistory = []

    def generatePassword(self, patientName): #Essa def gera uma senha para o paciente e adiciona a fila
        password = self.passwordCounter
        patient = {'name': patientName, 'password': password}
        self.queue.append(patient)
        self.passwordCounter += 1
        print(f"senha gerada para {patientName}: {password}")
    def callNextPatient(self): #Essa def chama o próximo paciente da fila para o atendimento
        if self.queue:
            patient = self.queue.pop(0)  # Remove o primeiro da fila
            self.callHistory.append(patient)  # Adiciona ao histórico
            print(f"chamando paciente {patient['name']} - Password: {patient['password']}")
        else:
            print("Nenhum paciente na fila")
    
    def resetPasswordSequence(self):#Essa def reinicia a sequência de senhas    
        self.passwordCounter = 1
        print("A sequência de senha foi redefinida")

    def showCallHistory(self):#Essa def exibe o histórico de chamadas
        if self.callHistory:
            print("Histórico de chamadas:")
            for call in self.callHistory:
                print(f"Paciente: {call['name']} - Password: {call['password']}")
        else:
            print("Nenhuma chamada foi feita ainda")
    def execute(self):
        hospitalSystem = HospitalSystem()

        # Gerando senhas para pacientes
        hospitalSystem.generatePassword("Julia")
        hospitalSystem.generatePassword("Fabricio")
        hospitalSystem.generatePassword("Carlos")

        # Chamando pacientes
        hospitalSystem.callNextPatient()
        hospitalSystem.callNextPatient()

        # Exibindo histórico de chamadas
        hospitalSystem.showCallHistory()

        # Reiniciando a sequência de senhas
        hospitalSystem.resetPasswordSequence()

        # Gerando novas senhas após reinicio
        hospitalSystem.generatePassword("Maria Eduarda")
        hospitalSystem.generatePassword("Luiza")
if __name__ == '__main__':
    start = HospitalSystem()
    start.execute()

