from flask import Flask, render_template, request
from App.gateway.user_controller import create_user_controller
from App.gateway.catetos_controller import create_catetos_controller


# Criando a instância dessa classe
# Necessário para que o Flask saiba onde procurar modelos, arquivos estáticos
app = Flask(__name__)


# Informar qual URL deve acionar a função
@app.route('/')
# A função recebe um nome que também é usado para gerar URLs
def index():
    # O Flask procurará na pasta templates
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    create_user_controller()
    return calculator()


@app.route('/result', methods=['POST'])
def result():
    create_catetos_controller()
    return calculator()


@app.route('/calculator', methods=['GET'])
def calculator():
    return render_template('calculator/calculator.html')


# Garante que o servidor seja executado apenas se o script for executado diretamente do interpretador Python
if __name__ == '__main__':
    # Faz com que o servidor recarregue automaticamente nas alterações de código
    app.debug = True
    app.run()
