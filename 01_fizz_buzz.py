"""
/*
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 *
 */

"""

INI = 1
FIN = 101

def is_multiple_3(n):
    return n % 3 == 0

def is_multiple_5(n):
    return n % 5 == 0
def is_multiple_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0

assert(is_multiple_3_and_5(15)) == True
assert(is_multiple_3(3)) == True
assert(is_multiple_5(5)) == True

for n in range(INI,FIN):
    if is_multiple_3_and_5(n):
        print("fizzbuzz")
    elif is_multiple_5(n):
        print("buzz")
    elif is_multiple_3(n):
        print("fizz")
    else:
        print(n)



    