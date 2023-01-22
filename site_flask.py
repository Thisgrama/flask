from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    with open('nomes.txt') as f:
        moedas = f.read().splitlines()
    f.close()
    return render_template('index.html', moedas=moedas)

if __name__ == '__main__':
    app.run(debug=True)