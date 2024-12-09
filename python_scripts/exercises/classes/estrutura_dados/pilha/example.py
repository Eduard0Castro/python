class EmptyStackError(Exception): ...

class Object:
    def __init__(self, value: str) -> None:
        self.value = value
        self.prox = None

class Stack:

    def __init__(self) -> None:
        self.topo :Object = None

    def push(self, value: str):
        obj = Object(value = value)

        if self.topo == None: self.topo = obj

        else: 
            obj.prox = self.topo
            self.topo = obj


    def pop(self) -> str:

        aux = self.topo

        if self.topo: self.topo = self.topo.prox
        else: raise EmptyStackError("Pilha vazia")
        
        return aux
    
    def verifica_equacao(self, equacao: str) -> None:
        for caractere in equacao: 
            if caractere == "(": self.push(caractere)
            elif caractere == ")": 
                try:
                    self.pop()
                except EmptyStackError:
                    print("Equacão incorreta: parenteses de fechamento a mais")
                    return

        if self.topo == None: print("Equação correta")
        else: print("Equação incorreta, parenteses não fechados")

    

def main():

    stack = Stack()
    equacao = ")(a+b)+c"
    stack.verifica_equacao(equacao)

if __name__ == "__main__":
    main()

