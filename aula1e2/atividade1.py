from flask import Flask

app = Flask(__name__)

@app.route("/decorator")
def decorator():
return """
<h1>Decorator em Python</h1>

<p><strong>O que é um decorator?</strong></p>
<p>
Um decorator é um recurso do Python utilizado para modificar ou adicionar
funcionalidades a uma função sem alterar diretamente o seu código.
</p>

<p><strong>Para que ele serve?</strong></p>
<p>
Ele serve para reutilizar código, adicionar validações, autenticação,
registros de log e outras funcionalidades extras.
</p>

<p><strong>Como ele é utilizado no Flask?</strong></p>
<p>
No Flask, o decorator @app.route é usado para definir qual URL executará
determinada função.
</p>

<p>Exemplo:</p>
<pre>
@app.route("/decorator")
def decorator():
return "Exemplo de decorator no Flask"
</pre>
"""

if __name__ == "__main__":
app.run(debug=True)