# Punto 1 utilizando la funcion print()
# inciso a
print("Las máquinas me sorprenden con mucha frecuencia")
# inciso b
print()
# inciso c
print("hola","soy","Carlos")
#  inciso d prueba  
print("23")
print(23)
# por mas que el 23 este o no con comillas me imprime el 23 sin comillas.
# inciso e
print("Una computadora puede ser llamada \"inteligente\"si logra engañar a una persona haciéndole creer que es un humano.")
# inciso f
print("Carlos","Raúl","Alvarez","40 años")
# separador "sep=" y "end="
print("carlos","Raúl","Alvarez","40 Años",sep="_")
# separador "end="
print("probando argumentos","soy el segundo argumento",end='-')
print('soy otra linea 6')
print('soy linea 7')
# clases de daltos o literales
print(type(40))
print((40+9))
print((40+9)/2)

# 05-03-2024
# argumentos posicionales

edad=18
print(f"su edad es {edad}")

# 
texto="Esto eS uN texTo MeZclAdO"
# title
print(texto.title())
print(texto)
texto=texto.title()
print(texto)
# upper lower
print(texto.upper())
print(texto.lower())
# repleace
print(texto.replace("","?"))
print(len(texto))

# inciso h
print("Calle: Libertad" "\t","\t" "Numero: 762","\t" "Codigo Postal: 9400")

# sentencia if
edad=int(input("ingrese su edad: "))
if edad > 18:
    print("es mayor de edad")
    else:
print("es menor de edad")
# 
calificacion=int(input("ingrese calificacion: "))
if calificacion >=90:
    print("Excelente")
else: 
   if calificacion >=80:
      print("Muy bien")
      else:
      if calificacion >=70:
         print("Bien")
         else:
         print("insuficiente")
   
