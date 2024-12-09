
class Node:

    def __init__(self, num: int) -> None:
        self.num = num
        self.right: Node = None
        self.left: Node = None
        self.height = 0

class Tree:

    def __init__(self) -> None:
        self.root: Node = None
        self.iteracoes: int = 0
        self.spaces: int = 0
        self.cont: int = 1

    def insert(self, root: Node, num: int) -> None:

        if root is None:
            new_node = Node(num)
            root = new_node
            new_node.height = 1
            return root
        
        if num < root.num: root.left = self.insert(root.left, num)
        elif num > root.num: root.right = self.insert(root.right, num) 
        else: return root


        root.height = max(self.calculate_height(root.left), 
                          self.calculate_height(root.right)) + 1

        balance = self.balance_tree(root)

        if balance > 1 and num < root.left.num: return self.right_rotation(root)
        elif balance > 1 and num > root.left.num:
            root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)

        elif balance < -1 and num > root.right.num: root = self.left_rotation()
        elif balance < -1 and num < root.right.num:
            root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)

        return root

    def print_(self, root: Node) -> None:
        if root == None: return

        self.spaces += self.cont
        
        self.print_(root.left)
        for i in range(self.spaces): print("\t", end="")
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
                
        root.height = max(self.calculate_height(root.left), 
                          self.calculate_height(root.right)) + 1

        balance = self.balance_tree(root)

        if balance > 1 and num < root.left.num: return self.right_rotation(root)
        elif balance > 1 and num > root.left.num:
            root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)

        elif balance < -1 and num > root.right.num: root = self.left_rotation()
        elif balance < -1 and num < root.right.num:
            root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)

        return root
    
    def calculate_height(self, node: Node) -> int:
        if node is None: return 0
        return node.height

    def balance_tree(self, node: Node) -> int:

        if node is None: return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)
    
    def right_rotation(self, root: Node) -> Node:
        
        lef = root.left
        rig = lef.right

        lef.right = root
        root.left = rig

        root.height = max(self.calculate_height(root.left), 
                          self.calculate_height(root.right)) + 1
        lef.height = max(self.calculate_height(lef.left) ,
                          self.calculate_height(lef.right)) + 1 

        return lef
    
    def left_rotation(self, node: Node) -> Node:
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

    tree.root = tree.insert(tree.root, 3)
    tree.root = tree.insert(tree.root, 2)
    tree.root = tree.insert(tree.root, 4)
    tree.root = tree.insert(tree.root, 8)
    tree.root = tree.insert(tree.root, 6)
    tree.root = tree.insert(tree.root, 5)

    tree.print_(tree.root)

    print()
    tree.root = tree.remove(tree.root, 6)
    tree.print_(tree.root)

    print(tree.search(tree.root, 5).num)


            