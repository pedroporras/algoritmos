# from .ventana_deslizante import solucion_fuerza_bruta, solucion_ventana_deslizante
from . import ventana_deslizante
from . import longest_substring

# Para encontrar la longitud de la subcadena más larga sin repetir en la cadena "abcabcbb", se puede utilizar el algoritmo de "Sliding Window" o ventana deslizante.

# El algoritmo consiste en mantener dos índices que representan el comienzo y el final de una ventana en la cadena. En cada iteración, el índice final se mueve hacia la derecha hasta que se encuentra un carácter repetido dentro de la ventana. En este punto, se actualiza la longitud máxima de la subcadena no repetida y el índice de inicio se mueve hacia la derecha hasta que el carácter repetido se elimine de la ventana.

# El proceso se repite hasta que el índice final alcance el final de la cadena.

# Aquí hay un ejemplo de cómo se aplicaría el algoritmo a la cadena "abcabcbb":

# Inicialmente, el índice de inicio y el índice final se establecen en 0.
# El índice final se mueve hacia la derecha hasta que se encuentra el segundo carácter "b" en la posición 3. La ventana actual es "abc".
# Se actualiza la longitud máxima de la subcadena no repetida a 3.
# El índice de inicio se mueve hacia la derecha hasta la posición 1 para eliminar el primer carácter "a" de la ventana. La ventana actual es "bc".
# El índice final se mueve hacia la derecha hasta la posición 4. La ventana actual es "abcb".
# El índice final se mueve hacia la derecha hasta la posición 5. La ventana actual es "bcbb".
# Se actualiza la longitud máxima de la subcadena no repetida a 3.
# El índice de inicio se mueve hacia la derecha hasta la posición 3 para eliminar el segundo carácter "b" de la ventana. La ventana actual es "cbb".
# El índice final se mueve hacia la derecha hasta la posición 6. La ventana actual es "cbba".
# El índice final se mueve hacia la derecha hasta el final de la cadena.
# Se devuelve la longitud máxima de la subcadena no repetida, que es 3.
# Por lo tanto, la longitud de la subcadena más larga sin repetir en la cadena "abcabcbb" es 3.
