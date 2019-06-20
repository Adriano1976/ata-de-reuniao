from ata import Ata
from sugestao import Sugestao
from funcionario import Funcionario

class ParticipanteReuniao(Sugestao, Ata):
    def __init__(self):
        super().__init__()
        self.funcionarios = Funcionario()
        self.listFuncPart = []
        self.listExtPart = []
    def incluirParticipante(self):
        self.escolha = int(input("DIGITE:\n- 1 PARA FUNCIONARIO \n- 2 PARA PARTICIPANTE EXTERNO"))
        if self.escolha  == 1:
            FuncPart = input("INFORME O FUNCIONARIO: ")
            self.listFuncPart.append(FuncPart)
            print(f"FUNCIONARIO: {FuncPart} INCLUIDO")
        elif self.escolha ==2:
            ExtPart = input("INFORME O PARTICIPANTE EXTERNO: ")
            self.listExtPart.append(ExtPart)
            print(f"PARTICIPANTE EXTERNO: {ExtPart} INCLUIDO")

    def selecionarParticipante(self):
        busca = str(input("NOME DO FUNCIONARIO OU PARTICIPANTE EXTERNO: "))
        self.selecionado = busca
        if self.selecionado in self.listFuncPart or self.listExtPart:
            print(F"{busca} SELECIONADO")
            self.selecionado = busca
            self.conf = 1
        else:
            print("PARTICIPANTE NAO ENCONTRADO")


obj = ParticipanteReuniao()


obj.incluirParticipante()

obj.selecionarParticipante()

