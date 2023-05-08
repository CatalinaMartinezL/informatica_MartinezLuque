# Workshops/[ES]Scripting.md at master · WomenBioinfoDataScLA/Workshops · GitHub

- <os> → operative system
	Biblioteca que permite mover/ejecutar cosas
- <sys> → biblioteca que toma parámetros entre terminales

# ARCHIVOS DE LECTURA
> Se puede leer todo en una línea o línea por línea.
> open(path_al_articulo, modo) → abre archivo. close → cierro el archivo
	> Tiene que ser un STR con la dirección a mi archivo
	> modo → la forma en que quiero ejecutarlo 
		> <r> → de lectura
		> <w> → escritura. Si el archivo no existe crea uno, si es que si, sobreescribe sobre eso borrando lo anterior.
		> <r+> → lectura y escritura
		> <a> → agrega al final del archivo
		> STR “ “
		> .readlines() → lee línea a línea. Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.
		> .read() Lee el archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.
		> .readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.
		> <os.chdir(path)>


> Otra forma para abrir archivo de forma segura:
	> with open(path_al_archivo, modo) as miarch:
    	# Aquí van las líneas de procesamiento del archivo

> RUTA ABSOLUTO: home/usuario/doc/Mi_nombre.txt → esto lo hago si el archivo que llama está en otro directorio.
	> Asumo un usuario, cuando lo prueba otro rompe.

> RUTA RELATIVA: “donde estoy parada”./doc/Mi_nombre.txt
	> No asume un usuario → mejor para los parciales.

## RESUMEN APB 
> *Paso 1*: pienso lo que quiero hacer en palaras, y lo escribo.

> *Paso 2*: importo lo que necesite:
	> <os> → si quiero mover/ejecutar cosas
		> permite:
			> <pwd> → Obtener directorio actual → getcwd()
			> <chdir(path)> → cambiar el directorio.
			> <mkdir(path[,modo])> → crear un directorio.

 	> <sys> → biblioteca que toma parámetros entre terminales

> *Paso 3*: abro el archivo.
	> with open(nombre del archivo, "modo") as miarchivo
		> Modos: <r>(read), <w>(write), <r+>(las dos), <a>(append)
		> miarchivo (o la palabra que elija) es para refererise al archivo que abro.
		> como uso with, no tengo que usar close, es como un cierre automatico.
	> ej: 
		>def es_un_ejemplo(archivo)
		with open(archivo, "modo") as miarchivo
			#en ese caso, el archivo que decido abrir es un parametro. Si lo pusiera entre comillas, le asginaria un archivo especifico con .txt

> *Paso 4*: definir que metodo voy a usar, en base a que quiero hacer.
	> <readlines()> lee las lineas del archivo y las devuelve como listas.
	> <readline()>  lee la primer linea del archivo.
		> al agregarle un numero, lee esa cantidad de caracteres, de la primera linea.
	> <read()> lee el contenido del archivo y lo devuelve como cadena de texto.
		>acepta un parámetro extra, ahi se puede especificar el nro de caracteres a leer.
		>Ej:
		with open("lista_compras.txt", r) as miarch
		print(archivo.read(5))
		#eso va a leer los primeros 5 caracteres del archivo.

> Algunas Funciones:
> > ><replace>("lo que quier reemplazar", "el reemplazo")
		>ej:
		with open ("ejemplo.txt", "r")
		lineas = archivo.readlines()
		for l in lineas:
			return (l.replace("\n", "|"))

> > > <split>("lo que quier separar")
	> ej:
	with open ("ejemplo.txt", "r")
	contenido= archivo.read()
	lineas = contenido.split("\n")
	print(lineas)
		#devuelve una cadena con el contenido, sin los enters

