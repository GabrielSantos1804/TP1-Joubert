from RAM import RAM
from Instrucao import Instrucao

class CPU:
    def __init__(self):
        self.registrador1 = 0
        self.registrador2 = 0
        self.PC = 0
        self.programa : list[Instrucao] = [None]
        self.opcode = 0

    def getRegistrador1(self):
        return self.registrador1

    def setRegistrador1(self, registrador1):
        self.registrador1 = registrador1

    def getRegistrador2(self):
        return self.registrador2

    def setRegistrador2(self, registrador2):
        self.registrador2 = registrador2

    def setPrograma(self, programaAux):
        self.programa = programaAux

    def iniciar(self, ram):
        self.opcode = 10
        self.PC = 0

        while (self.opcode != -1):

            inst = self.programa[self.PC]

            self.opcode = inst.opcode

            match self.opcode:
                # halt
                case -1:
                    print("Programa terminou!!")
                    ram.imprimir()

                # soma
                case 0:
                    self.registrador1 = ram.getDado(inst.add1)
                    self.registrador2 = ram.getDado(inst.add2)
                    self.registrador1 += self.registrador2

                    ram.setDado(inst.add3, self.registrador1)
                    print("Inst sum -> RAM posicao", inst.add3, "com conteúdo", self.registrador1)

                # subtrai
                case 1:
                    self.registrador1 = ram.getDado(inst.add1)
                    self.registrador2 = ram.getDado(inst.add2)
                    self.registrador1 -= self.registrador2

                    ram.setDado(inst.add3, self.registrador1)
                    print("Inst sub -> RAM posição", inst.add3, "com conteúdo", self.registrador1)

                # copia do registrador para ram
                # formato da instrucao [opcode,qual_registrador,end_ram,-1]
                case 2:
                    if (inst.add1 == 1):
                        ram.setDado(inst.add2, self.registrador1)
                        print("Inst copy_reg_ram -> RAM posição", inst.add2, "com conteúdo", self.registrador1)

                    elif (inst.add1 == 2):
                        ram.setDado(inst.add2, self.registrador2)
                        print("Inst copy_reg_ram -> RAM posição", inst.add2, "com conteúdo", self.registrador2)

                # copia da RAM para o registrador
                # formato da instrucao [opcode,qual_registrador,end_ram,-1]
                case 3:
                    if (inst.add1 == 1):
                        self.registrador1 = ram.getDado(inst.add2)
                        print("Inst copy_ram_reg -> Registrador1 com conteúdo", self.registrador1)

                    elif (inst.add1 == 2):
                        self.registrador2 = ram.getDado(inst.add2)
                        print("Inst copy_ram_reg -> Registrador2 com conteudo", self.registrador2)

            self.PC += 1