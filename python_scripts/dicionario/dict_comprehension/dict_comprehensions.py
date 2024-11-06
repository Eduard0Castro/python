from collections import Counter


def cont_file(text:str) -> dict:
    caracteres = list()
    quantidade = list()
    dicio = dict()
    for c in text:
        if c not in caracteres:
            caracteres.append(c)
            quantidade.append(1)

        else:
            index = caracteres.index(c)
            quantidade[index] += 1
        
    for c in range(len(caracteres)):
        dicio[caracteres[c]] = quantidade[c]

    return dicio  

def set_dict(text: str) -> dict:

    dicio = dict()
    caracteres = list({c for c in text})
    quantidade = [text.count(c) for c in caracteres]

    for i in range(len(caracteres)):
        dicio[caracteres[i]] = quantidade[i]

    return dicio  

def very_simple(text:str) -> dict:
    return {c: text.count(c) for c in set(text)}

def ridiculous(text: str) -> dict:
    return Counter(text)

def main():
    
    with open('moura.txt', 'r') as file:
        text = file.read()
    print(cont_file(text))
    print(set_dict(text))
    print(very_simple(text))
    print(ridiculous(text))



if __name__ == "__main__":
    main()

    