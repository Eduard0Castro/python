from disciplina import Disciplina
from aluno import Aluno

poo = Disciplina("POO", "Andrew Bernardino", 64, "LECI")
micro = Disciplina("Microcontroladores e microprocessadores", "Noel Maurilio", 32, "I1128")
elta00 = Disciplina("Circuitos e eletronica", "Egon", 32, "I111")

aluno1 = Aluno("Eduardo", 2021009360, [poo, micro, elta00])
aluno2 = Aluno("Mateus", 10365, [micro, elta00])
#aluno3 = Aluno("Hugo", 2024005698, ["Tecnicas de programação", "Calculo A", "Circuitos e Eletrônica"])

aluno1.imprime_aluno()
aluno2.imprime_aluno()

aluno1.historico.imprime()


