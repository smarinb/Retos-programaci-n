"""
/*
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
 *
 */
 """

def es_primo(n):
    for i in range(1,n+1):
        if i == 1 or i == n:
            continue
        else:
            if n % i == 0:
                return False
    return True
    


        

for n in range(1,101):
    if es_primo(n):
        print(n)


