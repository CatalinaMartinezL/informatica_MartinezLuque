# Patrones
> Lo que voy a querer buscar.
> Se puede escribir como <patron= “   ”> → y después ponerlo en el () del re.
o directo en el re. como; <re.función (r “   ”,    )

# Evaluar resultados de búsqueda
> Funciones; search, findall, sub
> *<re.search>* → método de biblioteca re.
    > Obtiene string buscado y posición donde se encuentra.
    > Ej: 
        import re
        if re.search(patron, texto) is not None:
            bloque de código
        else:
            bloque de código
> *<re.findall>* → se obtienen todas las apariciones del patrón.
    >Ej: "encontrar todos los numeros de capital"
        import re
        def tel_capital(texto):
            return re.findall (“(54911) [0-9] {8}”, texto)

> *<re.sub>* → reemplazas todas las ocurrencias del patrón, por otro en un string.
    > Ej:
        def reemplazar_por_barra (string1):
            string_nuevo = re.sub(r"[ _:]", "|", string1)
            return string_nuevo
    - o si escribo el patrón primero:
        def reemplazar_por_barra (string1):
            patron = "[ _:]"
            string_nuevo = re.sub(patron, "|", string1)
            return string_nuevo
> .group() → mostrar el rtado de una busqueda.
> <None> → no es nada
    > is not None → si es algo

# Unión de rangos
> Poner el inicio y el fin del rango entre corchetes y separados por un guión ([a-z] para todas las letras en minúscula)
> [^a-z] → ignorar rango
> ^[a-z] → 

# Apuntes
> Todo lo que no sea 0 es True → (booleano)
> No encuentra rtado: bool(None) → Falso
> “he{}” → solo busca esa palabra entre esos valores
> $ → donde termina la línea
> <find all> → devuelve lista cada vez que encuentra un patron
> . → cualquier cosa
> * → cero o una más veces
> ? →
    ? después de  un caracter → cero o una vez
    ? después de un modificador → todos los matches
> "^ac.{10}gt$"
    > que empiece con ac y termine en gt, y que tome 10 caracteres en el medio.

>"ac\d{10}gt"
    >Que entre ac y gt lea 10 caracteres alfanuméricos.
    
>{} el número que va ahí, es el número de caracteres que va a leer. 







