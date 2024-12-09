from random import randint
from estrutura_dados.listas.duplamente_encadeada import Lista

class Node:

    def __init__(self, num: int) -> None:
        self.num = num
        self.right = None
        self.left = None

class Tree:

    def __init__(self) -> None:
        self.root: Node = None
        self.iteracoes = 0

    def insert(self, root: Node, num: int) -> None:

        if root is None:
            new_node = Node(num)
            root = new_node
            return root
        
        if num < root.num: root.left = self.insert(root.left, num)
        else: root.right = self.insert(root.right, num) 

        return root

    def print_(self, root: Node) -> None:
        if root == None: return
        
        self.print_(root.left)
        print(root.num)
        self.print_(root.right)

    def search(self, root: Node, num: int) -> Node:

        resultado = None
        self.iteracoes += 1

        if root is None: return

        if num <= root.num:
            if (node:=self.search(root.left, num)) is not None:
                if node.num == num: resultado = node
            elif root.num == num: resultado = root
        else:
            if (node:=self.search(root.right, num)) is not None:
                if node.num == num: resultado = node

        return resultado
    
    def teste(self, root: Node, num: int) -> Node:
        result = self.search(root, num)

    
    def remove(self, root: Node, num: int):
        if num < root.num:
            root.left = self.remove(root.left, num)
        elif num > root.num:
            root.right = self.remove(root.right, num)
        else:
            if root.left == None and root.right == None:
                del root
                return None
            elif root.left != None and root.right == None:
                return root.left
            elif root.left == None and root.right != None:
                return root.right
            else:
                aux = root.left
                while(aux.right != None):
                    aux = aux.right
 
                root.num = aux.num
                root.left = self.remove(root.left, aux.num)

        return root



if __name__ == "__main__":
    tree = Tree()
    lista = Lista()

    insercoes = 0

    while insercoes != 5000:
        num = randint(0, 100000)
        lista.search(num)

        found = tree.search(tree.root, num)
        if found is None:
            insercoes += 1
            tree.root = tree.insert(tree.root, num)
            lista.insere(num)

    print(lista.iteracoes)
    print(tree.iteracoes)


            