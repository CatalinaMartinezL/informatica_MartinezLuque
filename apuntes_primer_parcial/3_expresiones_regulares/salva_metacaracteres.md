Tabla 1. Meta caracteres para expresiones regulares de Perl. La tabla contiene algunos de los caracteres de escape estándares que se pueden utilizar en expresiones regulares Perl. Estas expresiones reciben soporte en registros de EmailPlusRule y EmailPlusTemplate.
Meta carácter
Descripción
\	Marca el carácter siguiente como un carácter especial o un literal. Por ejemplo, n coincide con el carácter n, mientras que \n corresponde a un carácter de nueva línea. La secuencia \\ coincide con \ y \( coincide con (.
> ^	Corresponde al inicio de la entrada.
> $	Corresponde al final de la entrada.
> *	Corresponde al carácter anterior cero o más veces. Por ejemplo, zo* coincide con z o zoo.
> +	Corresponde al carácter anterior una o más veces. Por ejemplo, zo+ coincide con zoo, pero no con z.
> ?	Corresponde al carácter anterior cero o una sola vez. Pr ejemplo, a?ve? coincide con ve en never.
> .	Corresponde a cualquier carácter único excepto el carácter de nueva línea.
(pattern) Coincide con un patrón y recuerda la coincidencia. La subserie coincidente puede recuperarse del conjunto de coincidencias resultante utilizando este código: Item [0]... [n]. Para que coincidan los caracteres de paréntesis ( ), utilice \( o \).
> x|y	Coincide con x o y. Por ejemplo, z|wood coincide con z o wood. (z|w)oo coincide con zoo o wood.
> {n}	n es un entero no negativo. Coincide exactamente n veces. Por ejemplo, o{2} no coincide con o en Bob, pero sí con las dos primeras o de foooood.
{n,}	En esta expresión, n es un entero no negativo. Coincide con el carácter anterior al menos n veces. Por ejemplo, o{2,} no coincide con la o de Bob y coincide con todas las o de foooood. La expresión o{1,} equivale a o+ y o{0,} equivale a o*.
> {n,m}	Las variables m y n son enteros no negativos. Corresponde al carácter anterior al menos n veces y como máximo m veces. Por ejemplo, o{1,3} coincide con las tres primeras o de fooooood. La expresión o{0,1} equivale a o?.
> [xyz]	Un juego de caracteres. Coincide con cualquiera de los caracteres encerrados entre corchetes. Por ejemplo, [abc] coincide con a en plain.
> [^xyz] --> Un juego de caracteres negativos. Compara todos los caracteres que no están incluidos entre corchetes. Por ejemplo, [^abc] coincide con p en plain.
[a-z]	Un rango de caracteres. Coincide con cualquiera de los caracteres dentro del rango especificado. Por ejemplo, [a-z] coincide con cualquier carácter alfabético en minúsculas del alfabeto inglés.
> [^m-z] --> Un rango de caracteres negativos. Coincide con cualquiera de los caracteres que no están dentro del rango especificado. Por ejemplo, [m-z] coincide con cualquier carácter que no está en el rango comprendido entre m y z.
> \A	Corresponde solo al principio de una serie.
> \b	Coincide con el límite de una palabra, es decir, la posición entre una palabra y un espacio. Por ejemplo, er\b coincide con er en nunca, pero no con er en verb.
> \B	Coincide con un límite que no es de palabra. La expresión ea*r\B coincide con ear en never early.
> \d	Coincide con un carácter de dígito.
> \D	Coincide con un carácter que no es de dígito.
> \f	Coincide con un carácter de alimentación de papel.
> \n	Coincide con un carácter de nueva línea.
> \r	Coincide con un carácter de retorno de carro.
> \s	Coincide con cualquier espacio en blanco incluyendo espacios, tabuladores, caracteres de alimentación de papel, etc.
> \S	Coincide con un carácter de espacio que no esté en blanco.
> \t	Coincide con un carácter de tabulación.
> \v	Coincide con un carácter de tabulación vertical.
> \w	Coincide con cualquier carácter de palabra incluido el subrayado. Esta expresión es equivalente a [A-Za-z0-9_].
> \W	Coincide con cualquier carácter que no sea de palabra. Esta expresión equivale a [^A-Za-z0-9_].
> \z	Corresponde solo al final de una serie.
> \Z	Compara sólo el final de una serie o antes de un carácter de nueva línea al final.