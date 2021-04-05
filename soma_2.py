import datetime
from datetime import date


nome = input("Qual o seu nome! ")
print(f'Olá {nome} precisamos de mais informações')
dia = int(input('Dia do nascimento: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

datan = datetime.date(ano, mes, dia)

dif = (date.today() - datan)

result = (dif.days / 365.25)

print('%s você tem atualmente %d' %(nome, result))
