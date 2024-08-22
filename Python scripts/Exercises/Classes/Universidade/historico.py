import datetime
from disciplina import Disciplina
class Historico:
    def __init__(self, disciplinas_iniciais: list[Disciplina]):
        self.data_matricula = datetime.datetime.today()
        self.disciplinas_cursadas = disciplinas_iniciais


    def imprime(self):
        
        for disciplina in self.disciplinas_cursadas:
            print(f"Disciplina: {disciplina.nome} \nCarga horária: {disciplina.carga_horaria}\n")
            

    
    

