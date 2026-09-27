import random as rdm
from RAM import RAM
from CPU import CPU
from Instrucao import Instrucao
from LingAltoNivel import LingAltoNivel

class Programas:
    def __init__(self):
        ram = RAM()
        cpu = CPU()
        #self.programaAleatorio(ram, cpu, 2000000)
        #self.programaMultII(ram,cpu,15, 150)
        #self.programaFat(ram, cpu, 10)
        #self.programaDivII(ram, cpu, 175, 4)
        self.programaPoten(ram, cpu, 2, 6)


    def programaAleatorio(self, ram, cpu, qdeInstrucoes):
        umPrograma : list[Instrucao]= [None] * qdeInstrucoes
        r = rdm.Random()
        tamanhoRAM = 1000
        ram.criarRAM_aleatoria(tamanhoRAM)
        for i in range(qdeInstrucoes-1):
            inst = Instrucao()
            inst.opcode = r.randint(0,1)
            inst.add1 = r.randint(0,tamanhoRAM-1)
            inst.add2 = r.randint(0,tamanhoRAM-1)
            inst.add3 = r.randint(0,tamanhoRAM-1)
            umPrograma[i] = inst
        ultima = Instrucao()
        ultima.opcode = -1
        umPrograma[qdeInstrucoes-1] = ultima

        cpu.setPrograma(umPrograma)
        cpu.iniciar(ram)

    def programaMultII(self, ram, cpu, multiplicando, multiplicador):
        ram.criarRAM_vazia(2)
        lan = LingAltoNivel()
        lan.salvarValor(cpu, ram, multiplicando, 1)

        for i in range(multiplicador):
            lan.somar(cpu,ram,0,1)

        mult = lan.obterValor(cpu,ram,0)
        print(f"O resultado da multiplicação eh: {mult}")

    def programaFat(self,ram, cpu, fat):
        j = 1
        for i in range(1, fat+1):
            self.programaMultII(ram, cpu, j,i)
            print(f"%%%%")

            trecho1: list[Instrucao] = [None] * 2
            inst1 = Instrucao()
            inst1.opcode = 3
            inst1.add1 = 1
            inst1.add2 = 0
            trecho1[0] = inst1

            inst2 = Instrucao()
            inst2.opcode = -1
            trecho1[1] = inst2

            cpu.setPrograma(trecho1)
            cpu.iniciar(ram)

            j = cpu.getRegistrador1()

        trecho2 : list[Instrucao] = [None] * 2
        inst3 = Instrucao()
        inst3.opcode = 3
        inst3.add1 = 1
        inst3.add2 = 0
        inst3.add3 = -1
        trecho2[0] = inst3

        inst4 = Instrucao()
        inst4.opcode = -1
        trecho2[1] = inst4

        cpu.setPrograma(trecho2)
        cpu.iniciar(ram)
        print(f"O resultado do fatorial eh: {cpu.getRegistrador1()}")

    def programaDivII(self, ram, cpu, dividendo, divisor):
        # zerar ram
        ram.criarRAM_vazia(4)
        # Ex. dividir 14 / 3:
        # 14-3=11 (1 sub)
        # 11-3=8 (2 subs)
        # 8-3=5 (3 subs)
        # 5-3=2 (4 subs)
        # 2-3 < 0 (halt)
        # resultado 4

        # executar instrucao
        # -1 -> halt
        # 0 -> soma
        # 1 -> subtrai
        # 2 -> copia do registrador para RAM
        # 3 -> copia da RAM para o registrador

        lan = LingAltoNivel()
        lan.salvarValor(cpu, ram, dividendo, 0)
        lan.salvarValor(cpu, ram, divisor, 1)
        lan.salvarValor(cpu, ram, 1, 2)

        while (dividendo >= divisor):
            lan.subtrair(cpu, ram, 0, 1)
            lan.somar(cpu, ram, 3, 2)

            dividendo = lan.obterValor(cpu, ram, 0)

        div = lan.obterValor(cpu, ram, 3)

        print(f"O resultado da divisão é: {div}")

    def programaPoten(self, ram, cpu, base, expoente):
        resultado = 1
        for i in range(expoente):
            self.programaMultII(ram,cpu,resultado, base)
            resultado = cpu.getRegistrador1()
        print(f"O Resultado da potenciação eh: {resultado}")

    def programaPalindromo(self, ram, cpu, numero):
        print(f"Teste git1")




if __name__ == "__main__":
    Programas()




