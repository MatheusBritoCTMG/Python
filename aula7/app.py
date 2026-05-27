from flask import Flask, render_template, request
from calculadora import calcular_operacao

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None
    conta = None
    
    # Valores para manter o formulário preenchido após o envio
    num1_val = ""
    num2_val = ""
    op_val = "somar"

    if request.method == 'POST':
        num1_val = request.form.get('num1', '')
        op_val = request.form.get('operacao', '')
        num2_val = request.form.get('num2', '')

        # Se for raiz ou log, ignora o num2
        if op_val in ['sqrt', 'log']:
            conta, resultado = calcular_operacao(num1_val, op_val)
        else:
            conta, resultado = calcular_operacao(num1_val, op_val, num2_val)

        if conta is None:
            erro = resultado
            resultado = None

    return render_template(
        'calculadora.html',
        resultado=resultado,
        erro=erro,
        conta=conta,
        num1=num1_val,
        num2=num2_val,
        operacao=op_val
    )

if __name__ == '__main__':
    app.run(debug=True)
