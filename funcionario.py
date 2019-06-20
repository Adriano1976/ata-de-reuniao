from ata import Ata


class Funcionario(Ata):
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.nascimento = ""
        self.sexo = ""
        self.email = ""
        self.funcionarios = {}
        self.listfuncionarios = []
        self.conf = 0
        self.nomes = []
        super().__init__()

    def incluir(self):

        self.nome = str(input("NOME: "))
        self.matricula = str(input("MATRICULA: "))
        self.sexo = str(input("SEXO: "))
        self.nascimento = str(input("Nascimento: "))
        self.email = str(input("EMAIL: "))
        self.listfuncionarios = [f"NOME: {self.nome}", f"MATRICULA: {self.matricula}",
                                 f"SEXO: {self.sexo}", f"NASCIMENTO: {self.nascimento}",
                                 f"EMAIL: {self.email}"]
        self.nomes = [f"NOME: {self.nome}"]

        for i in self.listfuncionarios:
            print(i)

    def selecionar(self):
        busca = str(input("NOME DO FUNCIONARIO: "))
        self.selecionado = f"NOME: {busca}"
        if self.selecionado in self.listfuncionarios:
            print(F"FUNCIONARIO: {busca} SELECIONADO")
            self.selecionado = busca
            self.conf = 1
        else:
            print("FUNCIONARIO NAO ENCONTRADO")

    def emitir(self):
        print()
        if self.conf == 1:
            super().emitirAta(self.selecionado)
        else:
            print("EMISSOR DE ATA NAO SELECIONADO")