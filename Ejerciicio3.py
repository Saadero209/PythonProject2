#Un servidor guarda el tiempo que lleva encendido como una cantidad total de segundos. Escribe un programa que pida esa cantidad (número entero) y muestre a cuántos días, horas, minutos y segundos corresponde.
#Nombre=Saad Jlilou
#Fecha= 10/11/2026
segundos_totales = int(input("Introduce el tiempo en segundos: "))

dias = segundos_totales // 86400
resto = segundos_totales % 86400
horas = resto // 3600
resto = resto % 3600
minutos = resto // 60
segundos = resto % 60

print(segundos_totales ,"son", f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")