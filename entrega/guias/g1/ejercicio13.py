suma_precios = 0
cantidad_productos = 10

for _ in range(cantidad_productos):
    precio = float(input("Ingrese precio: "))
    suma_precios += precio

promedio = suma_precios / cantidad_productos

print("Promedio de precios:", promedio)