from __future__ import division
 
from math import *
 
def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    x=1
    for i in x range(2,n+1):
        x*=i
    return x
 
def poisson(k,m):
    """poisson(k,m): donne la probabilité d'avoir k évènements distribués selon une loi de Poisson de paramètre m"""
    return e**(-m)*m**k/fact(k)
 
# exemple d'utilisation
print (poisson(2,3))