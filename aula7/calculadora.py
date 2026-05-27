import math

def calcular_operacao(num1, operacao, num2=None):
    try:
        n1 = float(num1)
        
        # Operações com apenas um número
        if operacao == 'sqrt':
            if n1 < 0:
                return None, "Erro: Não é possível calcular a raiz quadrada de um número negativo."
            resultado = math.sqrt(n1)
            return f"√{n1}", resultado

        if operacao == 'log':
            if n1 <= 0:
                return None, "Erro: O logaritmo só é definido para números maiores que zero."
            resultado = math.log10(n1) # Logaritmo na base 10
            return f"log₁₀({n1})", resultado

        # Validação para operações que exigem o segundo número
        if num2 is None or num2 == '':
            return None, "Erro: O segundo número é obrigatório para esta operação."
        
        n2 = float(num2)

        # Operações com dois números
        if operacao == 'somar':
            return f"{n1} + {n2}", n1 + n2
        elif operacao == 'subtrair':
            return f"{n1} - {n2}", n1 - n2
        elif operacao == 'multiplicar':
            return f"{n1} × {n2}", n1 * n2
        elif operacao == 'dividir':
            if n2 == 0:
                return None, "Erro: Divisão por zero não é permitida."
            return f"{n1} ÷ {n2}", n1 / n2
        elif operacao == 'potencia':
            return f"{n1} ^ {n2}", n1 ** n2
        else:
            return None, "Erro: Operação inválida."

    except ValueError:
        return None, "Erro: Por favor, insira valores numéricos válidos."
