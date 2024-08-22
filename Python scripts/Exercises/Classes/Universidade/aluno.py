from disciplina import Disciplina
from historico import Historico

class Aluno:
    
    def __init__(self, nome: str, matricula: int, disciplinas: list[Disciplina]) -> None:
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = disciplinas
        self.historico = Historico(disciplinas[:])

    def insere_disciplina(self, disciplina: Disciplina) -> None:
        if not self.__valida_disciplina(disciplina):
            self.disciplinas.append(disciplina)
            self.historico.disciplinas_cursadas.append(disciplina)
            print(f"Disciplina {disciplina} inserida com sucesso")
        
        else:
            print("Disciplina já está na grade do semestre")

    def remove_disciplina(self, disciplina: Disciplina) -> None:

        if self.__valida_disciplina(disciplina):
            self.disciplinas.remove(disciplina)
            self.historico.disciplinas_cursadas.remove(disciplina)
            print("Disciplina removida com sucesso")

        else:
            print("Disciplina não pode ser removida porque não está na grade do semestre")



    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, value: str) -> None:
        self._nome = value

    def imprime_aluno(self) -> None:
        print(f"Nome: {self.nome}\nMatricula: {self.matricula}\nDisciplinas: {self.disciplinas}\n")

    def __valida_disciplina(self, disciplina: Disciplina) -> bool:
        
        return True if disciplina in self.disciplinas else False




    