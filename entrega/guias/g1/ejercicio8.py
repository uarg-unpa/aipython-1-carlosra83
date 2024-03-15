# conocer el perímetro y el área de un rectángulo según su base y altura.
base = float(input("Ingrese base: ")),input("cm", end=" ")
altura = float(input("Ingrese altura: "))

perimetro_rectangulo = 2*(base+altura)
area_rectangulo = base*altura

print("Perimetro rectangulo: ", perimetro_rectangulo)
print("Area rectangulo: ", area_rectangulo)

# conocer el perímetro y el área de una circunferencia según su radio.
radio = float(input("Ingrese radio: "))

perimetro_circunferencia = 2*radio*3.1416
area_circunferencia = 3.1416*radio**2

print("Perimetro circunferencia: ", perimetro_circunferencia)
print("Area circunferencia: ", area_circunferencia)