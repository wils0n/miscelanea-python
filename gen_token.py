__author__ = 'wilson'

import string
import random


def gen_token(tam=6):
    caracters = string.ascii_letters + string.digits + string.punctuation
    token = ''.join(random.choice(caracters) for i in range(tam))  # por cada iteracion se elige un caracter
    return token

'''
random.choice(secuencia_no_vacia), elige un elemento de la secuencia

usos de join:
>>> music=['Abba', 'Rolling Stones', 'Black Sabbath', 'Metallica']
>>> print ' '.join(music)
Abba Rolling Stones Black Sabbath Metallica

>>> print "\n".join(music)
Abba
Rolling Stones
Black Sabbath
Metallica

>>> print "\t".join(music)
Abba    Rolling Stones  Black Sabbath   Metallica
>>>

GENERADORES:
No permite trabajar de manera optima, cuando pensemos que la estructura sera infinita
No hace uso de la memoria, como en las listas por ejemplo. Solamente necesita saber cómo
generar el siguiente valor por lo que no necesita ni reservar espacio ni conocer a priori
ningún elemento.
'''
