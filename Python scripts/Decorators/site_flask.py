"""
Um decorator atribui uma nova funcionalidade para a função abaixo dele.
Geralmente, esses decorators são encontrados em frameworks para fazer com que uma função atenda a uma 
determinada funcionalidade previamente construída

"""

from flask import Flask

app = Flask(__name__)

#Nesse caso, atribui a funcionalidade de designar o link para cada página
@app.route("/home")
def homepage():
    return "This is my homepage"


@app.route("/contacts")
def contacts():
    return "These are my contacts"


app.run()