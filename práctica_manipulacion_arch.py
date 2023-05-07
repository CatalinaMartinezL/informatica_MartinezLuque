# # Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

#import parser


contador = 0 #arranca en cero y va sumando las que no empiezan con determinada letra
ruta_arch = "C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt"
def empieza_con(letra):
    global contador
    # primero tengo que abrir el archivo que voy a leer
    # condiciono para que cada linea en el archivo no empiece con LETRA/ letra
    # si es asi le sumo 1 al contador
    with open(ruta_arch,'r') as archivo:
        for linea in archivo:
            if not linea.startswith(letra.lower() or letra.upper()):
                contador+=1
empieza_con('p')
# print(contador)


# Otra alternativa

def start_with(letra,archivo):
    count = 0
    with open("C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt" ,"r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                count += 1

print(start_with("p","C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt"))


# Ejercicio 2
# Escribí un programa que lea un archivo e imprima las primeras n líneas.
def leer_n_lineas(cantidad,archivo):
    with open(archivo,'r') as file:
        for i in range(cantidad):
            print(file.readline())

# print(leer_n_lineas(1,'C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt'))


# Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def imprimir_ultimas(cantidad,archivo):
    with open(archivo,'r') as file:
        print(file.readlines()[-cantidad:])

# imprimir_ultimas(4,'C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt')

# Alternativa práctica
def read_n_back_lines(n,archivo):
    texto = open(archivo,'r').readlines()
    for i in range((len(texto)-n),len(texto)):
        print(texto[1])


# Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def cantidad_palabras(archivo):
    palabras = 0
    with open(archivo,'r') as file:
        for line in file:
            linea = line.split()
            for palabra in linea:
                palabras +=1
    print(palabras)
# print(cantidad_palabras('C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt'))

#Alternativa práctica

def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        pal = contenido.split()
        cantidad_palabra = len(pal)
        print(archivo,cantidad_palabra)


# Ejercicio 5
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, letra + '\n'))  #Reemplazo y lo escribo en el nuevo archivo



# Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos(archivo):
    sin_saltos = ''
    with open(archivo,'r') as file1, open('.\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt','w') as file2:
        for linea in file1:
            sin_saltos+=linea[:-1]
        file2.write(sin_saltos)
# eliminar_saltos('C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt')


# Ejercicio 7
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_larga(archivo):
    mas_larga = 0
    palabra_larga = ''
    with open(archivo,'r') as file:
        for palabra in file.read().split():
            if len(palabra)>mas_larga:
                mas_larga=len(palabra)
                palabra_larga=palabra
        print('caracteres:', mas_larga, 'palabra:', palabra_larga)

# palabra_larga('C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt')

# Alternativa práctica
def longest_word(archivo):
    max_long=0
    palabra=''
    with open(archivo,'r') as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word)>max_long:
                max_long=len(word)
                palabra=word
    print("La palabra mas larga es: " + palabra)

# Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def archivo1_2_3(archivo1,archivo2,archivo3):
    with open(archivo1,'r') as file1, open(archivo2,'r') as file2, open(archivo3,'a') as file3:
        file3.write(file1.read()+file2.read())

# Alternativa práctica

def join_files(file1,file2,file3):
    with open(file1,'r') as f1, open(file2,'r') as f2, open(file3,'a') as f3:
        f3.write(f1.read()+f2.read())


# Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia_palabra(archivo):
    diccionario = {}
    palabras =0
    with open(archivo,'r')as file:
        for line in file:
            linea = line.split()
            for palabra in linea:
                palabras +=1
                if palabra not in diccionario:
                    diccionario[palabra] = 1/palabras
                else:
                    diccionario[palabra]+=1/palabras
        print(diccionario)

# frecuencia_palabra('C:\Users\catal\OneDrive\Escritorio\fundamentos de informatica\informatica_MartinezLuque\texto_prueba.txt')

