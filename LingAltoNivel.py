from CPU import CPU
from RAM import RAM
from Instrucao import Instrucao

class LingAltoNivel:

    @staticmethod
    def somar(cpu, ram, end1, end2):
        trecho2 = [None, None]
        inst3 = Instrucao()
        inst3.opcode = 0
        inst3.add1 = end1
        inst3.add2 = end2
        inst3.add3 = end1
        trecho2[0] = inst3

        inst4 = Instrucao()
        inst4.opcode = -1
        trecho2[1] = inst4

        cpu.setPrograma(trecho2)
        cpu.iniciar(ram)

    @staticmethod
    def subtrair(cpu, ram, end1, end2):
        trecho2 = [None, None]
        inst3 = Instrucao()
        inst3.opcode = 1
        inst3.add1 = end1
        inst3.add2 = end2
        inst3.add3 = end1
        trecho2[0] = inst3

        inst4 = Instrucao()
        inst4.opcode = -1
        trecho2[1] = inst4

        cpu.setPrograma(trecho2)
        cpu.iniciar(ram)

    @staticmethod
    def salvarValor(cpu, ram, valor, end1):
        trecho1 = [None, None]
        cpu.setRegistrador1(valor)

        inst1 = Instrucao()
        inst1.opcode = 2
        inst1.add1 = 1
        inst1.add2 = end1
        trecho1[0] = inst1

        inst2 = Instrucao()
        inst2.opcode = -1
        trecho1[1] = inst2

        cpu.setPrograma(trecho1)
        cpu.iniciar(ram)

    @staticmethod
    def obterValor(cpu, ram, end1):
        trecho3 = [None, None]
        inst5 = Instrucao()

        inst5.opcode = 3
        inst5.add1 = 1
        inst5.add2 = end1
        inst5.add3 = -1
        trecho3[0] = inst5

        inst6 = Instrucao()
        inst6.opcode = -1
        trecho3[1] = inst6

        cpu.setPrograma(trecho3)
        cpu.iniciar(ram)

        return cpu.getRegistrador1()




