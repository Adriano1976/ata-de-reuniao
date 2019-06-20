from participantereuniao import ParticipanteReuniao


class ParticipanteExterno:
    def __init__(self):
        self.nome = ""
        self.empresa = ""
        self.email = ""
        self.partr = ParticipanteReuniao()
    def incluir(self):
        self.nome = str(input("NOME: "))
        self.empresa = str(input("EMPRESA: "))
        self.email = str(input("EMAIL: "))
        self.partr.incluirParticipante()

    def selecionar(self):
        pass
