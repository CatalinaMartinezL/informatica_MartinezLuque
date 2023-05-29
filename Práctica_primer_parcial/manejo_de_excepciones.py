'''
def eneavo(numero):
    try:
        print(1/numero)
    except ZeroDivisionError:
        print("No se puede dividir por", numero)
    except ZeroDivisionError:
        print("El", numero, "es un string")
        print(numero)  

eneavo(9)
eneavo(0)

# Ejercicio 2
def ejercicio2 (lista_n, n):
    lista_nueva = []
    try:
        for numero in lista_n:
            lista_nueva.append(numero/n)
            print(lista_nueva)
    except TypeError:
        print("Hay un string")

ejercicio2([2,4,6,8], 2)
ejercicio2([2,4,6,"8"], 2)
ejercicio2([2,4,6,8], "2")
ejercicio2([2,4,6,8])
ejercicio2()
ejercicio2(2)
'''

# Ejercicio 3
def lista_positivos(a,b):
    lista_p = []
    for i in a:
        if i < 0:
            raise Exception (f"{i} no es positivo")
                            # (str(i) + " no es positivo")
        if i> 0:
            lista_p.append(i)

    return lista_p

print(lista_positivos([1,2,3]))
print(lista_positivos([1,2,-1]))