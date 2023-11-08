import requests

try:
    response  = requests.get('http://pudim.com.br')
    if response.status_code == 200:
        print("\033[32mSite encontrado com sucesso!\033[m")

    else:
        print("\033[31mNão deu muito certo - else!\033[m")

except:
    
    print("\033[31mNão deu muito certo - except!\033[m")
