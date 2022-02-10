from flask import Flask
# from App.gateway.controller.catetos_controller import calc
from App.gateway.controller.user_controller import user

# Criando a instância dessa classe
# Necessário para que o Flask saiba onde procurar modelos, arquivos estáticos
app = Flask(__name__)

app.register_blueprint(user)
# app.register_blueprint(calc)


# # Informar qual URL deve acionar a função
# @app.route('/')
# # A função recebe um nome que também é usado para gerar URLs
# def index():
#     # O Flask procurará na pasta templates
#     return render_template('index.html')


# Garante que o servidor seja executado apenas se o script for executado diretamente do interpretador Python
if __name__ == '__main__':
    # Faz com que o servidor recarregue automaticamente nas alterações de código
    app.debug = True
    app.run()
