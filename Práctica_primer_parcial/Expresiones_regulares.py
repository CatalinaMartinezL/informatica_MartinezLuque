import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto))
print(texto[22:26])
# re.search(patron, texto) busca la primera vez que sale el patron en ese texto, en que posición esta
print(re.match(patron,texto))
# devuelve la primera aparición solo al principio de la línea, sino None
print(re.search(patron, texto).group())
#sirve para mostrar el resultado de una búsqueda, la coincidencia
print(re.search(patron, texto).group(0))
print(re.findall(patron,texto))
#agrupa en una lista todas las veces que aparece amet

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit" # . cualquier caracter 
                        # * indica que puede haber 0 o más de estos caracteres
                        # devuelve lo que se encuentra entre ipsum y sit
print(re.search(patron, texto).group())
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print(re.search(patron, texto).group(0))
#'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
print(re.search(patron, texto).group(1))
#' dolor sit amet, consectetur ipsum elit. Amet '
# group(1) lo uso nada mas si quiero quedarme con el substring que esta contenido

# Existe una forma de priorizar los matches internos y es con el metacaracter ?
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
print(re.search(patron, texto).group())
'ipsum dolor sit'
print(re.search(patron, texto).group(0))
'ipsum dolor sit'
print(re.search(patron, texto).group(1))
' dolor  '

print(re.sub(patron, "###", texto))
# reemplaza todas las ocurrencias del patrón por otro que elegimos