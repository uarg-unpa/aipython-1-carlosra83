#
def mutables(lista):
    lista[2]=35
    return lista

mis_numeros=[1,2,3]
print(f"antes de invocar a la Funcion")
print(mis_numeros)
mutables(mis_numeros)
print("despues de llamar a la funcion mutables")
print(mis_numeros)

