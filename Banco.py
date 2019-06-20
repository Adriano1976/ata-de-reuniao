import pickle
import json
class BancoDeDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar(self, dados):
        json.dump(dados, open(self.arquivo, "a"))

    def listar(self):
        dados = (open(self.arquivo, "r"))
        dados2 = dados.readlines()
        return dados2

    def atualizar(self, dados):
        pickle.dump(dados, open(self.arquivo, "w"))