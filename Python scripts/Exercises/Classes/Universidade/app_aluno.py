from disciplina import Disciplina
from aluno import Aluno

poo = Disciplina("POO", "Andrew Bernardino", 64, "LEC I")
micro = Disciplina("Microcontroladores e microprocessadores", "Noel Maurilio", 32, "I1128")
elta00 = Disciplina("Circuitos e eletronica", "Egon", 32, "I111")
elta01 = Disciplina("Analógica 1", "Egon", 32, "I2156")
aluno1 = Aluno("Eduardo", 2021009360, [poo, micro, elta00])
aluno2 = Aluno("Mateus", 10365, [micro, elta00])
#aluno3 = Aluno("Hugo", 2024005698, ["Tecnicas de programação", "Calculo A", "Circuitos e Eletrônica"])

aluno1.imprime_aluno()
aluno2.imprime_aluno()
aluno1.imprime_historico()

aluno2.insere_disciplina(Disciplina("Sei lá", "Não das quantas", 96, "LEC III"))

aluno1.remove_disciplina(elta00)
aluno1.remove_disciplina(elta01)