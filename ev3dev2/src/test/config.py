#!/usr/bin/env python3

import pickle

# Salva configurações em um arquivo para elas poderem existir entre execuções do programa
class Configuracao:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        self.nomeArquivo += ".pkl"
        try:
            self.carrega()
        except:
            self.config = []

    def limpa(self): 
        self.config = []
        self.salva()

    def salva(self):
        with open(self.nomeArquivo, 'wb') as f:
            pickle.dump(self.config, f)

    def carrega(self):
        with open(self.nomeArquivo, 'rb') as f:
            self.config = pickle.load(f)

    def obtem(self, chave): 
        for i in self.config:
            if i[0] == chave:
                return i[1]
        return None
    
    def insere(self, chave, valor):
        for i in self.config:
            if i[0] == chave:
                i[1] = valor
                self.salva()
                return
        self.config.append([chave, valor])
        self.salva()
        