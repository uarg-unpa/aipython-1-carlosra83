# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

invertir= float(input("Ingrese cuanto desea invertir: "))

interesAnual= float(input("ingrease el interes anual: "))

tiempoInversion= int(input("ingrese la cantidad de años a invertir. "))

inversion= invertir*(interesAnual/100)*tiempoInversion

print("su inversion obtenida es de: ", inversion)