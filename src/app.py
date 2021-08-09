from flask import Flask, render_template, request, session, flash
import requests


api = 'https://economia.awesomeapi.com.br/json/last/' #Api utilziada para coletar a cotação 

with open('src/opcoes.txt', 'r') as opcoes: #Arquivo com as moedas existentes extraído da wikipédia com o programa scrap.py
    lista = []
    for i in opcoes.readlines():
        lista.append(i.strip())
    lista.sort()

app = Flask(__name__)
app.config['SECRET_KEY']='chave secreta'


@app.route('/', methods=('POST','GET'))
def cotacao():
    val_fin = None #Valor final convertido
    if request.method == 'POST':
        to = str(request.form['to']) #Moeda alvo
        from_ = str(request.form['from']) #Moeda a ser convertida
        value = request.form['Value from'] #Valor a ser convertido
        error = None

        try:
            value = float(value)
            assert value > 0
        except:
            error = 'Insira um valor válido'
        
        r = requests.get(api+from_+'-'+to)#Requisição na API
        
        try:
            cota = (list((r.json().values()))[0])['bid']
        except:
            error = 'Conversão não suportada pela API'

        if error is None:
            val_fin = str(float(cota)*value) +' '+ to #multiplica o valor a ser convertido pela cotação
            session.clear()
        
        if error:
            flash(error)

    return render_template('index.html', lista=lista, val_fin=val_fin)


if __name__ == '__main__':
    app.run()
