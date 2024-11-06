
class Aluno():
    def __init__(self, 
                 nome: str, 
                 matricula: int, 
                 idade: int, 
                 nro_disciplinas: int) -> None:
        
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.nro_disciplinas = nro_disciplinas
        self.prox: Aluno = None
        self.anterior: Aluno = None
