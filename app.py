from flask import Flask, render_template, request
from persistence.database.database_objects import create_user
from App.gateway.user_controller import create_user_controller

# Criando a instância dessa classe
# Necessário para que o Flask saiba onde procurar modelos, arquivos estáticos
app = Flask(__name__)


# Informar qual URL deve acionar a função
@app.route('/')
# A função recebe um nome que também é usado para gerar URLs
def index():
    # O Flask procurará na pasta templates
    return render_template('index.html')

    
@app.route('/calculator', methods=['POST', 'GET'])
def calculator():
    create_user_controller()
    return render_template('calculator/calculator.html')

    
# Garante que o servidor seja executado apenas se o script for executado diretamente do interpretador Python
if __name__ == '__main__':
    # Faz com que o servidor recarregue automaticamente nas alterações de código
    app.debug = True
    app.run()
