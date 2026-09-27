import dataclasses as data

@data.dataclass
class Instrucao:
    add1 : int = 0
    add2: int = 0
    add3: int = 0
    opcode : int = 0