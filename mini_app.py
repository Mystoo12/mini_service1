from flask import Flask, render_template
import random
from waitress import serve

app = Flask(__name__)


@app.route('/')
def generer_nombre_aleatoire():
    nombre_aleatoire = random.randint(1,100)
    return render_template('index.html', nombre_aleatoire = nombre_aleatoire)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080,debug=True)
