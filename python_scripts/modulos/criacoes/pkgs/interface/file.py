def fileexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except (FileNotFoundError):
        print("Arquivo non exist")
        return False
    else:
        return True
    
def createfile(name):
    try:
        a = open(name, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")

    else:
        print("Arquivo criado com sucesso!")

def readfile(name):
    dado = []
    try:
        arq = open(name, 'rt')
    except:
        print('Erro ao abrir o arquivo')

    else:
        print("")
        for linha in arq:
            dado += linha.split(';')
        
        for i in range(0, len(dado)):
            if i%2 == 0:
                print("{:<30} {:>3} anos" .format(dado[i], dado[i+1].replace("\n", "")))
        print("")

    finally:
        arq.close()

def writefile(name, pessoa, idade):
    try:
        arq = open(name, "at")
    except:
        print("Houve algum problema ao abrir o arquivo para escrita")

    else:
        try:
            arq.write(f"\n{pessoa};{idade}")
        except:
            print("Houve um problema ao adicionar ao arquivo {}" . format(name))
        else:
            print(f"\033[32mRegistro de {pessoa} feito com sucesso!\033[m")
        finally:
            arq.close()
    
