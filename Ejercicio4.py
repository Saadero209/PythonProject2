#Escribe un programa que pida un número entero de tres cifras y muestre:Cada una de sus cifras (centenas, decenas y unidades).La suma de sus cifras.El número invertido, calculado como número (no como texto), de forma que pueda usarse en otras operaciones.No se permite convertir el número a cadena de texto (str): usa // y %.
#Nombre= Saad
#Fecha= 10/11/2026

numero = int(input("Introduce un número de tres cifras: "))

centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10

suma_cifras = centenas + decenas + unidades
numero_invertido = unidades * 100 + decenas * 10 + centenas

print(f"Centenas: {centenas} Decenas: {decenas} Unidades: {unidades}")
print(f"Suma de las cifras: {suma_cifras}")
print(f"Número invertido: {numero_invertido}")



