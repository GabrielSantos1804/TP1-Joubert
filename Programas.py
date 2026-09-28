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
        #self.programaPoten(ram, cpu, 2, 6)
        #self.programaBhaskara(ram, cpu, 1, 2, -3)
        #self.programaRaiz(ram, cpu, 4)
        #self.programaDistancia2Pontos(ram, cpu, 1, 4, 2, 6)
        #self.programaVerticeParabola(ram, cpu, 1, -4, 3)


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

        negativo = multiplicador < 0
        vezes = abs(multiplicador)

        lan.salvarValor(cpu, ram, multiplicando, 1)
        for i in range(vezes):
            lan.somar(cpu,ram,0,1)

        mult = lan.obterValor(cpu,ram,0)

        if negativo:
            mult = -mult
            cpu.setRegistrador1(mult)

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

        if divisor == 0:
            print("Erro: divisão por zero não eh permitida.")
            return None

        resultado_negativo = (dividendo < 0) != (divisor < 0)  # XOR de sinais
        dividendo_abs = abs(dividendo)
        divisor_abs = abs(divisor)

        ram.criarRAM_vazia(4)
        lan = LingAltoNivel()
        lan.salvarValor(cpu, ram, dividendo_abs, 0)  # <- precisa ser dividendo_abs, não dividendo
        lan.salvarValor(cpu, ram, divisor_abs, 1)
        lan.salvarValor(cpu, ram, 1, 2)

        while dividendo_abs >= divisor_abs:
            lan.subtrair(cpu, ram, 0, 1)
            lan.somar(cpu, ram, 3, 2)
            dividendo_abs = lan.obterValor(cpu, ram, 0)

        div = lan.obterValor(cpu, ram, 3)

        if resultado_negativo:
            div = -div
            cpu.setRegistrador1(div)

        print(f"O resultado da divisao eh: {div}")

    def programaPoten(self, ram, cpu, base, expoente):
        resultado = 1
        expoente_abs = abs(expoente)
        for i in range(expoente_abs):
            self.programaMultII(ram,cpu,resultado, base)
            resultado = cpu.getRegistrador1()
            print(f"O Resultado da potenciação eh: {resultado}")

    def programaRaiz(self, ram, cpu, base):

        if (base < 0):
            print("Não é permitido bases menores que 0")
            return 0

        ram.criarRAM_vazia(3)
        lan = LingAltoNivel()

        resultado = 0
        incremento = 1
        while (base > 0):
            lan.salvarValor(cpu, ram, base, 0)
            lan.salvarValor(cpu, ram, incremento, 1)
            lan.subtrair(cpu, ram, 0, 1)
            base = cpu.getRegistrador1()
            lan.salvarValor(cpu, ram, 2, 2)
            lan.somar(cpu, ram, 1, 2)
            incremento = cpu.getRegistrador1()
            lan.salvarValor(cpu, ram, resultado, 0)
            lan.salvarValor(cpu, ram, 1, 1)
            lan.somar(cpu, ram, 0, 1)
            resultado = cpu.getRegistrador1()

        if (base < 0):
            lan.subtrair(cpu, ram, 0, 1)
            resultado = cpu.getRegistrador1()

        print(f"O resultado inteiro da raíz quadrada eh: {resultado}")

    def programaBhaskara(self, ram, cpu, a, b ,c):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        self.programaPoten(ram , cpu, b, 2)
        baoquadrado = cpu.getRegistrador1()

        self.programaMultII(ram, cpu, a, c)
        a_vezes_c = cpu.getRegistrador1()

        self.programaMultII(ram,cpu, a_vezes_c, 4)
        quatro_vezes_ac = cpu.getRegistrador1()

        lan.salvarValor(cpu, ram, baoquadrado, 0)
        lan.salvarValor(cpu,ram, quatro_vezes_ac, 1)
        lan.subtrair(cpu, ram, 0, 1)
        delta = lan.obterValor(cpu, ram, 0)

        print(f"O delta é {delta}")

        if delta < 0:
            print(f"Não existem raizes reais")
        elif delta == 0:
            self.programaMultII(ram, cpu, a, 2)
            dois_vezes_a = cpu.getRegistrador1()

            escala = 1000

            self.programaMultII(ram, cpu, -b, escala)
            menos_b_escalado = cpu.getRegistrador1()

            self.programaDivII(ram, cpu, menos_b_escalado, dois_vezes_a)
            quociente_escalado = cpu.getRegistrador1()

            x = quociente_escalado / escala
            print(f"Uma raiz real: x = {x}")
        else:
            self.programaRaiz(ram, cpu, delta)
            raiz_delta = cpu.getRegistrador1()

            self.programaMultII(ram, cpu, a, 2)
            dois_vezes_a = cpu.getRegistrador1()

            lan.salvarValor(cpu,ram, -b, 0)
            lan.salvarValor(cpu,ram, raiz_delta, 1)
            lan.somar(cpu, ram , 0, 1)
            x1 = cpu.getRegistrador1()
            self.programaDivII(ram, cpu, x1, dois_vezes_a)
            x1 = cpu.getRegistrador1()

            lan.salvarValor(cpu,ram, -b, 0)
            lan.salvarValor(cpu,ram, raiz_delta, 1)
            lan.subtrair(cpu, ram, 0, 1)
            x2 = cpu.getRegistrador1()
            self.programaDivII(ram, cpu, x2, dois_vezes_a)
            x2 = cpu.getRegistrador1()

            print(f"As raizes sao respectivamente : {x1} e {x2}")

    def programaDistancia2Pontos(self, ram, cpu, x1, y1, x2, y2):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        lan.salvarValor(cpu, ram, x1, 0)
        lan.salvarValor(cpu, ram, x2, 1)
        lan.subtrair(cpu, ram, 1, 0)
        x = cpu.getRegistrador1()

        lan.salvarValor(cpu, ram, y1, 0)
        lan.salvarValor(cpu, ram, y2, 1)
        lan.subtrair(cpu, ram, 1, 0)
        y = cpu.getRegistrador1()

        self.programaPoten(ram, cpu, x,2)
        x = cpu.getRegistrador1()

        self.programaPoten(ram, cpu, y, 2)
        y = cpu.getRegistrador1()

        lan.salvarValor(cpu, ram, x, 0)
        lan.salvarValor(cpu, ram, y, 1)
        lan.somar(cpu, ram , 1, 0)
        d = cpu.getRegistrador1()

        self.programaRaiz(ram, cpu, d)
        d = cpu.getRegistrador1()
        print(f"A distancia entre esses pontos é {d}")

    def programaVerticeParabola(self, ram , cpu, a, b, c):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        self.programaPoten(ram, cpu, b, 2)
        baoquadrado = cpu.getRegistrador1()

        self.programaMultII(ram, cpu, a, c)
        a_vezes_c = cpu.getRegistrador1()

        self.programaMultII(ram, cpu, a_vezes_c, 4)
        quatro_vezes_ac = cpu.getRegistrador1()

        lan.salvarValor(cpu, ram, baoquadrado, 0)
        lan.salvarValor(cpu, ram, quatro_vezes_ac, 1)
        lan.subtrair(cpu, ram, 0, 1)
        delta = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, 2, a)
        dois_vezes_a = cpu.getRegistrador1()
        self.programaDivII(ram, cpu, -b, dois_vezes_a)
        xv = cpu.getRegistrador1()

        self.programaMultII(ram, cpu, 4, a)
        quatro_vezes_a = cpu.getRegistrador1()
        self.programaDivII(ram, cpu, -delta, quatro_vezes_a)
        yv = cpu.getRegistrador1()

        print(f"O vertice da parabola é {xv, yv}")



if __name__ == "__main__":
    Programas()




