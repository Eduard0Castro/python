from estrutura_dados.listas.universidade.disciplina import Disciplina
from estrutura_dados.listas.universidade.historico import Historico


from typing import List

class Aluno:
    
    DISCIPLINAS_DISPONIVEIS = [Disciplina("POO", "Andrew Bernardino", 64, "LEC I"),
                               Disciplina("Microcontroladores e microprocessadores", "Noel Maurilio", 32, "I1128"),
                               Disciplina("Circuitos e eletronica", "Egon", 32, "I111")]

    def __init__(self, nome: str, matricula: int, disciplinas: List[Disciplina]) -> None:
        self.nome = nome
        self.matricula = matricula

        self.disciplinas = []

        for disciplina in disciplinas:
            if self.__valida_disciplina(disciplina):
                self.disciplinas.append(disciplina)
            
        self.historico = Historico(self.disciplinas[:])


    def insere_disciplina(self, disciplina: Disciplina) -> None:
        if self.__valida_disciplina(disciplina):
            self.disciplinas.append(disciplina)
            self.historico.disciplinas_cursadas.append(disciplina)
            print(f"Disciplina {disciplina} inserida com sucesso")
        
        else:
            print("Disciplina já está na grade do semestre ou não está disponível")

    def remove_disciplina(self, disciplina: Disciplina) -> None:

        if disciplina in self.disciplinas:
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
        print(f"Nome: {self.nome}\nMatricula: {self.matricula}\nDisciplinas:\n")
        for disc in self.disciplinas: print(disc)
        print()


    def imprime_historico(self):
        print(f"Historico do aluno {self.nome}: ")
        self.historico.imprime()

    def __valida_disciplina(self, disciplina: Disciplina) -> bool:
        
        return True if disciplina in self.DISCIPLINAS_DISPONIVEIS and disciplina not in self.disciplinas else False