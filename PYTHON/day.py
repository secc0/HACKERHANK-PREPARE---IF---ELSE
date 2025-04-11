import calendar

mes, dia, ano = map(int, input().split())
dias = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(dias[calendar.weekday(ano, mes, dia)])
