#Escribe un programa que pida el precio de un producto sin IVA y muestre el importe del IVA (21 %) y el precio final que debe pagar el cliente.
#Nombre= Saad Jlilou
#Fecha=10/11/2026
precio = float(input("Introduce el precio del producto sin IVA: ").replace(",", "."))

iva = precio * 0.21
precio_final = precio + iva

print(f"Importe del IVA (21 %): {iva:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
