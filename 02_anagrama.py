"""
    /*
 * Reto #2
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 *
 */

"""



def is_anagrama(word_one,word_two):
    if word_one == word_two:
        return False
    elif (sorted(word_one.lower()) == sorted(word_two.lower())):
        return True
    else:
        return False

assert(is_anagrama('INGLATERRA','InTeGrarla')) == True
assert(is_anagrama('Sergio','casa')) == False
assert(is_anagrama('casa','casa')) == False

word_one = input("Introduzca la primera palabra => ")
word_two = input("Introduzca la segunda palabra => ")

result = is_anagrama(word_one,word_two)

print(f"¿Las palabras {word_one} y {word_two} son anagramas ? => {result}")

