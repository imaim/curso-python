"""
Exercicios de fixação
"""
# 51


valor_premio = float(input("Digite o valor do Premio: "))
aposta1 = float(input("Digite o valor da primeira aposta: "))
aposta2 = float(input("Digite o valor da segunda aposta: "))
aposta3 = float(input("Digite o valor da terceira aposta: "))
total_aposta = aposta1 + aposta2 + aposta3


def resultado_percent(valor_aposta):
    resultado = (valor_aposta / total_aposta) * valor_premio
    return resultado


premio_aposta1 = resultado_percent(aposta1)
premio_aposta2 = resultado_percent(aposta2)
premio_aposta3 = resultado_percent(aposta3)
print(f'A aposta 1 va receber {premio_aposta1:.2f}\nA aposta 2 va receber {premio_aposta2:.2f}\nA aposta 3 va receber {premio_aposta3:.2f}')
