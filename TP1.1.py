from sympy import *
from cmath import * 

def ex1():
    z1 = 3 + 4j
    z2 = 1 - 2j

    print(f"z1 = {z1}")
    print(f"Partie réelle de z1 : {z1.real}")
    print(f"Partie imaginaire de z1 : {z1.imag}\n")

    print(f"z2 = {z2}")
    print(f"Partie réelle de z2 : {z2.real}")
    print(f"Partie imaginaire de z2 : {z2.imag}\n")

    module_z1 = abs(z1)
    module_z2 = abs(z2)

    print(f"Module de z1 : {module_z1}")
    print(f"Module de z2 : {module_z2}\n")

    argument_z1 = phase(z1)
    argument_z2 = phase(z2)

    print(f"Argument de z1 : {argument_z1} ")
    print(f"Argument de z2 : {argument_z2} ")

ex1()
