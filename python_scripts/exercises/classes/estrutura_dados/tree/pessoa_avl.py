from random import randint


class Pessoa:

    def __init__(self, nome: str, cpf: str, endereco: str, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.left: Pessoa = None
        self.right: Pessoa = None
        self.height: int = 0


class Tree:

    def __init__(self) -> None:
        self.root: Pessoa = None
        self.iteracoes: int = 0
        self.spaces: int = 0
        self.cont: int = 1

    def insert(self, root: Pessoa, attr = tuple[str, str, str, str]) -> None:

        nome, cpf, endereco, telefone = attr
        pessoa = self.search(root, cpf)

        if pessoa: 
            print(f"Pessoa com cpf já existente na árvore!: {pessoa.cpf}")
            return root

        else:

            if root is None:
                new_node = Pessoa(nome, cpf, endereco, telefone)
                root = new_node
                new_node.height = 1
                return root
            
            if nome < root.nome: root.left = self.insert(root.left, attr)
            elif nome > root.nome: root.right = self.insert(root.right, attr) 
            else: return root


            root.height = max(self.calculate_height(root.left), 
                            self.calculate_height(root.right)) + 1

            balance = self.balance_tree(root)

            if balance > 1 and nome < root.left.nome: return self.right_rotation(root)
            elif balance > 1 and nome > root.left.nome:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)

            elif balance < -1 and nome > root.right.nome: root = self.left_rotation(root)
            elif balance < -1 and nome < root.right.nome:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)

            return root

    def print_(self, root: Pessoa, space: bool) -> None:
        if root == None: return
        if space:
            self.spaces += self.cont
        
        self.print_(root.left, space)
        if space:
            for i in range(self.spaces): print("\t", end="")
        print(root.nome)
        self.print_(root.right, space)

    def search(self, root: Pessoa, cpf: str) -> Pessoa:

        resultado = None
        self.iteracoes += 1

        if root is None: return

        if int(cpf) <= int(root.cpf):
            if (node:=self.search(root.left, cpf)) is not None:
                if node.cpf == cpf: resultado = node
            elif root.cpf == cpf: resultado = root
        else:
            if (node:=self.search(root.right, cpf)) is not None:
                if node.cpf == cpf: resultado = node

        return resultado
    
    
    def remove(self, root: Pessoa, nome: str):


        if nome < root.nome:
            root.left = self.remove(root.left, nome)
        elif nome > root.nome:
            root.right = self.remove(root.right, nome)
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

                root.nome = aux.nome
                root.left = self.remove(root.left, aux.nome)
                
        root.height = max(self.calculate_height(root.left), 
                        self.calculate_height(root.right)) + 1

        balance = self.balance_tree(root)

        if balance > 1 and nome < root.left.nome: return self.right_rotation(root)
        elif balance > 1 and nome > root.left.nome:
            root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)

        elif balance < -1 and nome > root.right.nome: root = self.left_rotation(root)
        elif balance < -1 and nome < root.right.nome:
            root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)

        return root
        

    def calculate_height(self, node: Pessoa) -> int:
        if node is None: return 0
        return node.height

    def balance_tree(self, node: Pessoa) -> int:

        if node is None: return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)
    
    def right_rotation(self, root: Pessoa) -> Pessoa:
        
        lef = root.left
        rig = lef.right

        lef.right = root
        root.left = rig

        root.height = max(self.calculate_height(root.left), 
                          self.calculate_height(root.right)) + 1
        lef.height = max(self.calculate_height(lef.left) ,
                          self.calculate_height(lef.right)) + 1 

        return lef
    
    def left_rotation(self, node: Pessoa) -> Pessoa:
        rig = node.right
        lef = rig.left

        rig.left = node
        node.right = lef

        node.height = max(self.calculate_height(node.left), 
                          self.calculate_height(node.right)) + 1
        rig.height = max (self.calculate_height(rig.right), 
                          self.calculate_height(node.left)) + 1

        return rig

if __name__ == "__main__":

    tree = Tree()
    lista = list()

    for i in range(10):
        lista.append([  f"Pessoa{i+1}",
                        f"12345678{i}", 
                        f"Rua Sem Nome, {randint(1,2000)}", 
                        f"12988647{randint(100, 900)}"])
        
    
    lista[5][1] = "99966688841"
    lista[6][1] = "99966688841"
    lista[2][1] = "33311122245"
    lista[9][1] = "33311122245"

    for i in lista: 
        tree.root = tree.insert(tree.root, tuple(i))

    tree.root = tree.remove(tree.root, "Pessoa1")
    tree.root = tree.remove(tree.root, "Pessoa4")
    tree.print_(tree.root, True)
    tree.print_(tree.root, False)
