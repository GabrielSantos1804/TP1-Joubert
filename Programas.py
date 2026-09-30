import random as rdm
from RAM import RAM
from CPU import CPU
from Instrucao import Instrucao
from LingAltoNivel import LingAltoNivel

class Programas:
    def __init__(self):
        ram = RAM()
        cpu = CPU()
        #PROGRAMAS JOUBERT
        #self.programaAleatorio(ram, cpu, 2000000)
        #self.programaMultII(ram,cpu,15, 150)
        #self.programaFat(ram, cpu, 10)
        #self.programaDivII(ram, cpu, 175, 4)
        #PROGRAMAS AUTORAIS
        #self.programaPoten(ram, cpu, 2, 5)
        #self.programaBhaskara(ram, cpu, 1, 2, -3)
        #self.programaRaiz(ram, cpu, 4)
        #self.programaDistancia2Pontos(ram, cpu, 1, 4, 2, 6)
        #self.programaVerticeParabola(ram, cpu, 1, -4, 3)
        #self.programaModulo(ram, cpu, -17, -5)
        #self.programaMUVEspaco(ram, cpu, 0, 0, 2, 3)
        #self.programaMDC(ram,cpu,48,18)
        #self.programaMMC(ram,cpu,12,18)
        #self.programaFibonacci(cpu, ram, 11)
        #self.palindromoNumerico(cpu, ram, 121)
        #self.programaPrimo(ram,cpu,29)
        #self.programaFibonacci(cpu, ram, 11)
        #self.programaCombinacao(cpu, ram, 3, 0)
        #self.programaEquacao2grauSomaProduto(cpu,ram,1,2,-3)


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
            lan.salvarValor(cpu, ram, mult, 0)

        print(f"O resultado da multiplicação eh: {mult}")

    def programaFat(self,ram, cpu, fat):
        if fat == 0:
            lan = LingAltoNivel()
            lan.salvarValor(cpu, ram, 1, 0)
            print("O resultado do fatorial eh: 1")
            return

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
        lan.salvarValor(cpu, ram, div, 0)

        print(f"O resultado da divisao eh: {div}")

    def programaPoten(self, ram, cpu, base, expoente):
        lan = LingAltoNivel()

        resultado = 1
        expoente_abs = abs(expoente)
        for i in range(expoente_abs):
            self.programaMultII(ram,cpu,resultado, base)
            resultado = lan.obterValor(cpu, ram, 0)
            print(f"O Resultado da potenciação eh: {resultado}")

    def programaRaiz(self, ram, cpu, base):

        if (base < 0):
            print("Não são permitidas bases menores que 0")
            return 0

        ram.criarRAM_vazia(3)
        lan = LingAltoNivel()

        resultado = 0
        incremento = 1
        while (base > 0):
            lan.salvarValor(cpu, ram, base, 0)
            lan.salvarValor(cpu, ram, incremento, 1)
            lan.subtrair(cpu, ram, 0, 1)
            base = lan.obterValor(cpu, ram, 0)
            lan.salvarValor(cpu, ram, 2, 2)
            lan.somar(cpu, ram, 1, 2)
            incremento = lan.obterValor(cpu, ram, 1)
            lan.salvarValor(cpu, ram, resultado, 0)
            lan.salvarValor(cpu, ram, 1, 1)
            lan.somar(cpu, ram, 0, 1)
            resultado = lan.obterValor(cpu, ram, 0)
        if (base < 0):
            lan.subtrair(cpu, ram, 0, 1)
            resultado = lan.obterValor(cpu, ram, 0)

        print(f"O resultado inteiro da raíz quadrada eh: {resultado}")

    def programaBhaskara(self, ram, cpu, a, b ,c):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        self.programaPoten(ram , cpu, b, 2)
        baoquadrado = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, a, c)
        a_vezes_c = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram,cpu, a_vezes_c, 4)
        quatro_vezes_ac = lan.obterValor(cpu, ram, 0)

        lan.salvarValor(cpu, ram, baoquadrado, 0)
        lan.salvarValor(cpu,ram, quatro_vezes_ac, 1)
        lan.subtrair(cpu, ram, 0, 1)
        delta = lan.obterValor(cpu, ram, 0)

        print(f"O delta é {delta}")

        if delta < 0:
            print(f"Não existem raizes reais")
        elif delta == 0:
            self.programaMultII(ram, cpu, a, 2)
            dois_vezes_a = lan.obterValor(cpu, ram, 0)

            escala = 1000

            self.programaMultII(ram, cpu, -b, escala)
            menos_b_escalado = lan.obterValor(cpu, ram, 0)

            self.programaDivII(ram, cpu, menos_b_escalado, dois_vezes_a)
            quociente_escalado = lan.obterValor(cpu, ram, 0)

            self.programaDivII(ram,cpu,quociente_escalado,escala)
            x = lan.obterValor(cpu, ram, 0)
            print(f"Uma raiz real: x = {x}")
        else:
            self.programaRaiz(ram, cpu, delta)
            raiz_delta = lan.obterValor(cpu, ram, 0)

            self.programaMultII(ram, cpu, a, 2)
            dois_vezes_a = lan.obterValor(cpu, ram, 0)

            lan.salvarValor(cpu,ram, -b, 0)
            lan.salvarValor(cpu,ram, raiz_delta, 1)
            lan.somar(cpu, ram , 0, 1)
            x1 = lan.obterValor(cpu, ram, 0)
            self.programaDivII(ram, cpu, x1, dois_vezes_a)
            x1 = lan.obterValor(cpu,ram, 0)

            lan.salvarValor(cpu,ram, -b, 0)
            lan.salvarValor(cpu,ram, raiz_delta, 1)
            lan.subtrair(cpu, ram, 0, 1)
            x2 = lan.obterValor(cpu, ram, 0)
            self.programaDivII(ram, cpu, x2, dois_vezes_a)
            x2 = lan.obterValor(cpu, ram, 0)

            print(f"As raizes sao respectivamente : {x1} e {x2}")

    def programaDistancia2Pontos(self, ram, cpu, x1, y1, x2, y2):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        lan.salvarValor(cpu, ram, x1, 0)
        lan.salvarValor(cpu, ram, x2, 1)
        lan.subtrair(cpu, ram, 1, 0)
        x = lan.obterValor(cpu, ram, 1)

        lan.salvarValor(cpu, ram, y1, 0)
        lan.salvarValor(cpu, ram, y2, 1)
        lan.subtrair(cpu, ram, 1, 0)
        y = lan.obterValor(cpu, ram, 1)

        self.programaPoten(ram, cpu, x,2)
        x = lan.obterValor(cpu, ram, 0)

        self.programaPoten(ram, cpu, y, 2)
        y = lan.obterValor(cpu, ram, 0)

        lan.salvarValor(cpu, ram, x, 0)
        lan.salvarValor(cpu, ram, y, 1)
        lan.somar(cpu, ram , 1, 0)
        d = lan.obterValor(cpu, ram, 1)

        self.programaRaiz(ram, cpu, d)
        d = lan.obterValor(cpu, ram, 0)
        print(f"A distancia entre esses pontos é {d}")

    def programaVerticeParabola(self, ram , cpu, a, b, c):
        ram.criarRAM_vazia(2)

        lan = LingAltoNivel()

        self.programaPoten(ram, cpu, b, 2)
        baoquadrado = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, a, c)
        a_vezes_c = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, a_vezes_c, 4)
        quatro_vezes_ac = lan.obterValor(cpu, ram, 0)

        lan.salvarValor(cpu, ram, baoquadrado, 0)
        lan.salvarValor(cpu, ram, quatro_vezes_ac, 1)
        lan.subtrair(cpu, ram, 0, 1)
        delta = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, 2, a)
        dois_vezes_a = lan.obterValor(cpu, ram, 0)
        self.programaDivII(ram, cpu, -b, dois_vezes_a)
        xv = lan.obterValor(cpu,ram, 0)

        self.programaMultII(ram, cpu, 4, a)
        quatro_vezes_a = lan.obterValor(cpu,ram, 0)
        self.programaDivII(ram, cpu, -delta, quatro_vezes_a)
        yv = lan.obterValor(cpu,ram, 0)

        print(f"O vertice da parabola é {xv, yv}")

    def programaModulo(self, ram, cpu, dividendo, divisor, criar_ram = True):
        #não podemos executar divisao com o divisor 0
        if divisor == 0:
            print("Erro: divisão por zero não é permitida.")
            return None
        #transformamos os valores em positivos
        dividendo_abs = abs(dividendo)
        divisor_abs = abs(divisor)
        if criar_ram:
            ram.criarRAM_vazia(2)#criando o espaço na RAM para executar a conta
        lan = LingAltoNivel()#criando um objeto com as funções da linguagem de alto nivel
        #salvando na RAM os valores positivos
        lan.salvarValor(cpu,ram,dividendo_abs,0)
        lan.salvarValor(cpu,ram,divisor_abs,1)

        while dividendo_abs >= divisor_abs:#enquanto o dividendo for maior que o divisor, continue subtraindo, quando o dividendo for menor, quer dizer que chegamos no resto
            lan.subtrair(cpu,ram,0,1)#subtrair dividendo por divisor
            dividendo_abs = lan.obterValor(cpu,ram,0)#atualizar dividendo

        resto = dividendo_abs
        if resto != 0:
            if divisor > 0:
                if dividendo < 0:
                    lan.salvarValor(cpu,ram,divisor_abs,1)
                    lan.salvarValor(cpu,ram,resto,0)
                    lan.subtrair(cpu,ram,1,0)
                    resto = lan.obterValor(cpu,ram,1)
            else:
                if dividendo >= 0:
                    lan.salvarValor(cpu,ram,divisor_abs,1)
                    lan.salvarValor(cpu,ram,resto,0)
                    lan.subtrair(cpu,ram,1,0)
                    resto = lan.obterValor(cpu,ram,1)

                lan.salvarValor(cpu,ram,0,1)
                lan.salvarValor(cpu,ram,resto,0)
                lan.subtrair(cpu,ram,1,0)
                resto = lan.obterValor(cpu,ram,1)
        
        lan.salvarValor(cpu, ram, resto, 0)
        print(f"O resultado do modulo é: {resto:d}")

    def programaMUVEspaco(self, ram , cpu,S0, v0, a, t):
        ram.criarRAM_vazia(2)
        lan = LingAltoNivel()

        self.programaMultII(ram, cpu, v0, t)
        v0 = lan.obterValor(cpu,ram, 0)

        self.programaPoten(ram, cpu, t, 2)
        t = lan.obterValor(cpu,ram, 0)

        self.programaMultII(ram , cpu, a, t)
        t = lan.obterValor(cpu,ram, 0)

        self.programaDivII(ram, cpu, t, 2)
        t = lan.obterValor(cpu,ram, 0)

        lan.salvarValor(cpu, ram, S0, 0)
        lan.salvarValor(cpu, ram, v0, 1)
        lan.somar(cpu, ram, 0, 1)
        v0 = lan.obterValor(cpu,ram, 0)

        lan.salvarValor(cpu,ram, v0, 0)
        lan.salvarValor(cpu, ram, t, 1)
        lan.somar(cpu, ram, 0, 1)
        s = lan.obterValor(cpu,ram, 0)

        print(f"O espaço é: {s}")

    def programaMDC(self,ram,cpu,numero1,numero2):
        ram.criarRAM_vazia(1)

        lan = LingAltoNivel()

        while numero2 != 0:
            self.programaModulo(ram,cpu,numero1,numero2)
            numero1 = numero2
            numero2 = lan.obterValor(cpu,ram,0)
        mdc = numero1
        lan.salvarValor(cpu, ram, mdc, 0)
        print(f"O resultado do MDC é: {mdc}")

    def programaMMC(self,ram,cpu,numero1,numero2):
        ram.criarRAM_vazia(1)

        lan = LingAltoNivel()
        numero1_abs = abs(numero1)
        numero2_abs = abs(numero2)

        self.programaMultII(ram,cpu,numero1_abs,numero2_abs)
        denominador = lan.obterValor(cpu,ram,0)
        self.programaMDC(ram,cpu,numero1,numero2)
        divisor = lan.obterValor(cpu,ram,0)

        self.programaDivII(ram,cpu,denominador,divisor)
        mmc = lan.obterValor(cpu,ram,0)

        lan.salvarValor(cpu, ram, mmc, 0)
        print(f"O resultado do mmc é: {mmc}")

    def programaPrimo(self,ram,cpu,numero):
        ram.criarRAM_vazia(4)

        lan = LingAltoNivel()

        lan.salvarValor(cpu, ram, numero, 0)
        lan.salvarValor(cpu, ram, 1, 1)
        lan.somar(cpu, ram, 0, 1)
        limite = lan.obterValor(cpu, ram, 0)
        lan.salvarValor(cpu,ram,0,2)#salvar o contador
        lan.salvarValor(cpu,ram,1,3)#salvar o numero 1
        for i in range(1,limite):
            self.programaModulo(ram,cpu,numero,i,False)
            resto = lan.obterValor(cpu,ram,0)
            if resto == 0:
                lan.somar(cpu,ram,2,3)

        contador = lan.obterValor(cpu,ram,2)
        if contador > 2:
            primo = False
            print(f"O número não é primo!")
        else:
            primo = True
            print(f"O número é primo!")

    def programaFibonacci(self, cpu, ram, indice):
        if indice < 0:
            print("Índices menores que 0 não são aceitos")
            return None

        ram.criarRAM_vazia(3)
        lan = LingAltoNivel()

        lan.salvarValor(cpu, ram, 0, 0)
        lan.salvarValor(cpu, ram, 1, 1)

        for i in range(indice):
            b = lan.obterValor(cpu, ram, 1)
            lan.somar(cpu, ram, 1, 0)
            lan.salvarValor(cpu, ram, b, 0)

        resultado = lan.obterValor(cpu, ram, 0)
        print(f"O resultado do Fibonacci eh: {resultado}")

    def programaDivIII(self, ram, cpu, dividendo, divisor, criar_ram = True):
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

        if criar_ram:
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
        lan.salvarValor(cpu, ram, div, 3) #alterando o local de salvamento do quociente para end3

        print(f"O resultado da divisao eh: {div}")

    def programaMultIII(self, ram, cpu, multiplicando, multiplicador, criar_ram = True):
        if criar_ram:
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
            lan.salvarValor(cpu, ram, mult, 0)

        print(f"O resultado da multiplicação eh: {mult}")

    def palindromoNumerico(self, cpu, ram, numero):
        if numero < 0:
            print("Não são aceitos números negativos")
            return None

        ram.criarRAM_vazia(6)
        lan = LingAltoNivel()

        valor_antigo = numero
        quociente = numero
        invertido = 0

        for i in range(len(str(numero))):
            #limpando div anterior
            lan.salvarValor(cpu, ram, 0, 3)

            self.programaDivIII(ram, cpu, quociente, 10,False)
            quociente = lan.obterValor(cpu, ram, 3)
            resto = lan.obterValor(cpu, ram, 0)

            #limpando multiplicação anterior
            lan.salvarValor(cpu, ram, 0, 0)

            self.programaMultIII(ram, cpu, invertido, 10, False)
            invertido = lan.obterValor(cpu, ram, 0)
            lan.salvarValor(cpu, ram, invertido, 5)

            lan.salvarValor(cpu, ram, resto, 3)
            lan.somar(cpu, ram, 5, 3)
            invertido = lan.obterValor(cpu, ram, 5)

        if invertido == valor_antigo:
            print(f"O número {valor_antigo} eh um palíndromo")
            return None
        else:
            print(f"O número {valor_antigo} não eh um palíndromo")
            return None




    def programaCombinacao(self, cpu, ram, n, k):
        if n < 0 or k < 0:
            print("Erro: Os valores n e k não podem ser negativos")
            return

        if k > n:
            print(f"Erro: Não é possível agrupar {n} elementos em conjuntos de {k}.")
            return

        ram.criarRAM_vazia(2)
        lan = LingAltoNivel()

        lan.salvarValor(cpu, ram, n, 0)
        lan.salvarValor(cpu, ram, k, 1)
        lan.subtrair(cpu, ram, 0, 1)
        val_n_menos_k = lan.obterValor(cpu, ram, 0)

        self.programaFat(ram, cpu, val_n_menos_k)
        fat_n_menos_k = lan.obterValor(cpu, ram, 0)

        self.programaFat(ram, cpu, n)
        fat_n = lan.obterValor(cpu, ram, 0)

        self.programaFat(ram, cpu, k)
        fat_k = lan.obterValor(cpu, ram, 0)

        self.programaMultII(ram, cpu, fat_k, fat_n_menos_k)
        denominador = lan.obterValor(cpu, ram, 0)

        self.programaDivII(ram, cpu, fat_n, denominador)
        combinacao = lan.obterValor(cpu, ram, 0)

        print(f"A combinação C({n},{k}) = {combinacao}")

    def programaEquacao2grauSomaProduto(self, cpu, ram, a, b, c):
        ram.criarRAM_vazia(6)

        lan = LingAltoNivel()

        #RAM[0] = auxiliar
        #RAM[1] = auxiliar
        #RAM[2] = Soma
        #RAM[3] = Produto
        #RAM[4] = x1
        #RAM[5] = x2
        #Calculando -b
        lan.salvarValor(cpu, ram, 0, 0)
        lan.salvarValor(cpu, ram, b, 1)
        lan.subtrair(cpu, ram, 0, 1)
        menosb = lan.obterValor(cpu, ram, 0)
        #Calculando Soma = -b / a
        lan.salvarValor(cpu, ram, 0, 3)
        self.programaDivIII(ram, cpu, menosb, a, False)
        Soma = lan.obterValor(cpu, ram, 3)
        #Calculando Produto = c / a
        lan.salvarValor(cpu, ram, 0, 3)
        self.programaDivIII(ram, cpu, c, a, False)
        Produto = lan.obterValor(cpu, ram, 3)
        #Salvando Soma e Produto
        lan.salvarValor(cpu, ram, Soma, 2)
        lan.salvarValor(cpu, ram, Produto, 3)
        #calculando os limites para o for, que seriam o produto + 1, negativo e positivo
        if Produto < 0:
            lan.salvarValor(cpu, ram, 0, 0)
            lan.salvarValor(cpu, ram, Produto, 1)
            lan.subtrair(cpu, ram, 0, 1)
            produtoPositivo = lan.obterValor(cpu, ram, 0)
        else:
            produtoPositivo = Produto

        lan.salvarValor(cpu, ram, produtoPositivo, 0)
        lan.salvarValor(cpu, ram, 1, 1)

        lan.somar(cpu, ram, 0, 1)
        limiteP = lan.obterValor(cpu, ram, 0)

        lan.salvarValor(cpu, ram, 0, 1)
        lan.salvarValor(cpu, ram, limiteP, 0)
        lan.subtrair(cpu, ram, 1, 0)
        limiteN = lan.obterValor(cpu, ram, 1)
        #for para encontrar as raízes
        for x1 in range(limiteN, limiteP):
            lan.salvarValor(cpu, ram, x1, 4)
            #Calculando x2 = Soma - x1
            lan.salvarValor(cpu, ram, Soma, 5)
            lan.subtrair(cpu, ram, 5, 4)
            x2 = lan.obterValor(cpu, ram, 5)
            #Zerando RAM[0] para executar a multiplicação sem erro
            lan.salvarValor(cpu, ram, 0, 0)
            # Calculando x1 * x2
            self.programaMultIII(ram, cpu, x1, x2, False)
            testeProduto = lan.obterValor(cpu, ram, 0)
            #Verificando se o produto encontrado é igual ao produto esperado
            if testeProduto == Produto:
                print(f"As raízes da função do segundo grau são {x1} e {x2}")
                return

        print("Raízes não encontradas")






if __name__ == "__main__":
    Programas()




