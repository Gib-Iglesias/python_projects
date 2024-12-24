# -*- coding: utf-8 -*-

def palindromo(sentencia):

    """
    Permite conocer si un str es, o no, un palíndromo.
    Examples
    ----------
    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('Se van sus naves')
    True

    >>> palindromo('Gib Iglesias')
    False
    """

    sentencia = sentencia.lower().replace(' ','')
    return sentencia == sentencia[::-1]
