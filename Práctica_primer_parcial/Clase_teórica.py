import re

"""
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group())
print(texto[22:26])
#probemos match
print(re.match(patron,texto))
#probemos findall
print(re.findall(patron,texto))
"""
"""
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
print(re.search(patron, texto), "\n")
print(re.search(patron, texto).group())
print(re.search(patron, texto).group(0))
print(re.search(patron, texto).group(1))
""" 

# reemplaza la expresion lorem por amet(en este caso)
print(re.sub(patron, "###", texto))