class Ata:
    def __init__(self):
        self.titulo = ""
        self.dataEmissao = ""
        self.inicio = ""
        self.termino = ""
        self.pauta= ""
        self.descricao= ""
        self.palavraChave = ""
        self.tipo = ""
        self.estatus = ""

    def emitirAta(self, emissor):
        self.titulo = str(input("TITULO DA ATA: "))
        self.dataEmissao = str(input("DATA DE EMICAO: "))
        self.inicio = str(input("INICIO: "))
        self.termino = str(input("TERMINO: "))
        self.pauta = str(input("PAUTA: "))
        self.descricao = str(input("DESCRICAO: "))
        self.palavraChave = str(input("PALAVRA(S) CHAVE: "))
        self.tipo = str(input("TIPO: "))
        self.estatus = str(input("ESTATUS: "))
        self.emissor = emissor
        self.ataEmitida = [f"EMISSOR: {self.emissor}"f"TITULO: {self.titulo}", f"DATAEMISSAO: {self.dataEmissao}",
                           f"INICIO: {self.inicio}", f"TERMINO: {self.termino}",
                           f"PAUTA: {self.pauta}", f"DESCRICAO: {self.descricao}",
                           f"PALAVRA CHAVE: {self.palavraChave}", f"TIPO: {self.tipo}",
                           f"ESTATUS: {self.estatus}", f"EMISSOR: {self.emissor}"]
        for i in self.ataEmitida:
            print(i)

    def exibirAta(self):
        pass

    def salvarAta(self):
        pass

    def atualizarAta(self):
        pass