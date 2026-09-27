import random as rdm

class RAM:
    def __init__(self):
        self.memoria = []

    def criarRAM(self, tamanho):
        self.memoria = [0] * tamanho

    def criarRAM_vazia(self, tamanho):
        self.criarRAM(tamanho)
        for i in range(tamanho):
            self.memoria[i] = 0

    def criarRAM_aleatoria(self, tamanho):
        r = rdm.Random()
        self.criarRAM(tamanho)
        for i in range(tamanho):
            self.memoria[i] = r.randint(-2**31, 2**31 - 1) #gera inteiro no mesmo range de um int de 32 bits do Java

    def setDado(self, endereco, conteudo):
        self.memoria[endereco] = conteudo

    def getDado(self, endereco):
        return self.memoria[endereco]

    def imprimir(self):
        print(f"Conteudo da RAM: ")
        for i in range(len(self.memoria)):
            print(f"{self.memoria[i]}, ", end="")
        print(f"")
