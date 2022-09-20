"""
Exercicios de fixação
"""
# 36
#from datetime import timedelta


def timeconv(segundospassados):
    if segundospassados is not None:
        dias = segundospassados // (3600 * 24)
        hora = segundospassados // 3600 % 24
        minutos = segundospassados % 3600 // 60
        segundos = segundospassados % 3600 % 60
        # return '{:02d}:{:02d}:{:02d}'.format(hora, minutos, segundos)
        if dias > 0:
            return f'{dias}D:{hora}H:{minutos}m:{segundos}s'
        elif hora > 0:
            return f'{hora}H:{minutos}m:{segundos}s'
        elif minutos > 0:
            return f'{minutos}m:{segundos}s'
        elif segundos > 0:
            return f'{segundos}s'
    return 'Falha'


valor_total_seg = int(input("Digite o valor total em segundos: "))
print(f'O resultado em Horas:minutos:segundos é: {timeconv(valor_total_seg)}')
