
"""
_dados: protegido, convenção para que não seja acessado fora da classe, mas ainda assim pode 
ser acessado e modificado, podendo quebrar a classe
__dados: privado, o python não permite que seja modificado, criando uma outra variável com o mesmo
nome para que ela sim seja modificada pela instância

Ou então pode-se criar a propriedade para retornar direto o valor de __dados, por exemplo
"""

class Client:
    def __init__(self):
        self.__dados = dict()

    @property
    def dados(self):
        return self.__dados
    
    def insert(self, name):

        if "clientes" not in self.__dados:
            self.__dados["clientes"] = [name]

        else:
            self.__dados["clientes"].append(name)

    def list_client(self):
        for index, value in enumerate(self.__dados["clientes"]):
            print(index, value)

    def remove_client(self, index):
        if index < len(self.__dados["clientes"]):
            del self.__dados["clientes"][index]

        else:
            print("Out of the range, impossible to remove")


    
dados = Client()
dados.insert("Eduardo")
dados.insert("José")
dados.insert("Wellington")
dados.insert("Sirlene")

# Tentando acessar __dados pela instância:
dados.__dados = "Modificando uma outra variável"
print(dados.__dados)

# Acessando a variável de classe que não foi modificada:
print(dados._Client__dados)
print(dados.dados)
