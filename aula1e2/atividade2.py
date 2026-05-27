from flask import Flask

app = Flask(__name__)

@app.route("/")
def curriculo():
return """
<h1>Currículo</h1>

<h2>Matheus Vaz</h2>

<p><b>Idade:</b> 18 anos</p>
<p><b>Email:</b> matvaz2001@email.com</p>

<h3>Objetivo</h3>
<p>Atuar na área de tecnologia e desenvolvimento de sistemas.</p>

<h3>Formação</h3>
<p>Ensino Médio em andamento</p>

<h3>Habilidades</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>HTML</li>
<li>Banco de Dados</li>
</ul>
"""

if __name__ == "__main__":
app.run(debug=True)