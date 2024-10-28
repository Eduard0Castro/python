from universidade import Universidade
from aluno import Aluno
from lista import Lista

class App:
    LISTA = Lista(Universidade)
    
    @classmethod
    def insere_universidade(cls) -> None:
        nome = input("Digite o nome da universidade: ")
        cond, _ = cls.__verifica_universidade(nome)
        App.LISTA.insere(nome) if cond else print(f"{nome} já está na lista")

    @classmethod
    def insere_aluno(cls) -> None:
        universidade = input("Digite o nome da universidade para adicionar o aluno: ")
        cond, uni = cls.__verifica_universidade(universidade)

        if not cond:
            matricula = int(input("Digite a matricula do aluno: "))
            cond, _ = cls.__verifica_aluno(matricula, uni)

            if cond:
                nome = input("Digite o nome do aluno: ")
                idade = int(input("Digite a idade do aluno: "))
                nro_disciplinas = int(input("Digite o numero de disciplinas do aluno: "))
                uni.insere(nome, matricula, idade, nro_disciplinas)
            else:
                print("Aluno já cadastrado na universidade")
        

    @classmethod
    def busca_universidade(cls) -> bool:
        nome = input("Digite o nome da universidade a buscar: ")
        exist, _ = cls.__verifica_universidade(nome)
        if not exist: print(f"{nome.capitalize()} existe na lista")
        else: print(f"{nome.capitalize()} NÃO existe na lista")
        return not exist
    
    @classmethod
    def busca_aluno(cls) -> tuple[Aluno, Universidade]:
        matricula = int(input("Digite o numero de matricula do aluno: "))
        if App.LISTA.ini:
            aux = App.LISTA.ini
            aux_aluno = aux.ini

            while True:
                
                while True:

                    if aux_aluno == None:
                        if aux.prox: 
                            aux = aux.prox
                            aux_aluno = aux.ini 
                        else: return None, None

                    else: break

                while True:

                    if aux_aluno.prox == None and aux_aluno.matricula != matricula: 
                        break

                    if aux_aluno.matricula == matricula: 
                        print("Matricula na universidade {}" .format(aux.nome))
                        return aux_aluno, aux
                    
                    aux_aluno = aux_aluno.prox

                if aux.prox == None: return None, None
                
        else: 
            raise "Nenhuma universidade cadastrada"
                

    @classmethod
    def __verifica_universidade(cls, nome: str) -> tuple[bool, Universidade | None]:
        nome = nome.capitalize()
        if cls.LISTA.ini is not None:
        
            aux = cls.LISTA.ini

            while aux.nome != nome:
                

                if aux.prox == None and aux.nome != nome: return True, None
                aux = aux.prox

                
            return False, aux
        
        return True, None
    
    @classmethod
    def __verifica_aluno(cls, matricula: int, universidade: Universidade) -> tuple [bool, Aluno | None]:
        
        aux  = universidade.ini

        if aux is not None:
            while aux.matricula != matricula:
                

                if aux.prox == None and aux.matricula != matricula: return True, None

                aux = aux.prox


        else:
            return True, None
                
        return False, aux

    @classmethod
    def remove_universidade(cls) -> None:
        nome = input("Digite o nome da universidade: ")
        App.LISTA.remover(nome)

    @classmethod
    def remove_aluno(cls):
        aluno, universidade = cls.busca_aluno()
        universidade.remover(aluno.matricula) if aluno else print("Aluno não encontrado")


def main():

    funcoes = {1: App.insere_universidade, 
               2: App.insere_aluno, 
               3: App.busca_universidade, 
               4: App.busca_aluno, 
               5: App.remove_universidade, 
               6: App.remove_aluno, 
               7: App.LISTA.imprime,}
    while True:
        print("Digite a opção requisitada: \n1) Insere universidade")
        print("2) Insere aluno\n3) Busca Universidade\n4) Busca Aluno")
        print("5) Remove Universidade\n6) Remove Aluno")
        print("7) Imprimir lista de universidades\n0) Fechar")
        opcao = int(input("Opção: "))

        if opcao == 0: break

        action = funcoes.get(opcao, None)
        action() if action else print("Opção inválida!")

if __name__ == "__main__":
    main()