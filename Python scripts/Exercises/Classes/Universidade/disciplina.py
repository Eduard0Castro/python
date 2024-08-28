
class Disciplina:
    
    def __init__(self, nome: str, professor: str, carga_horaria: int, sala: str) -> None:
        self.nome = nome
        self.professor = professor
        self.carga_horaria = carga_horaria
        self.sala = sala

    def __eq__(self, __value: object) -> bool:
        return self.nome == __value.nome and self.professor == __value.professor and self.carga_horaria == __value.carga_horaria and self.sala == __value.sala
    
    def __str__(self) -> str:
        return f"{self.nome} com {self.professor}, de {self.carga_horaria} horas, na sala {self.sala}"