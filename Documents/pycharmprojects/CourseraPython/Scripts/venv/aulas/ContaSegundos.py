segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
restoSegundos = segundos % 86400
horas = restoSegundos // 3600
restoSegundos = restoSegundos % 3600
minutos = restoSegundos // 60
segundos = restoSegundos % 60
print(f"{dias} dia(s), {horas} horas, {minutos} minutos e {segundos} segundos.")