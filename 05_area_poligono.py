"""
/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 *
 */

"""

def calc_area(poligono):
    resultado = 0
    if poligono=='cuadrado':
        lado = int(input("Introduce la medida del lado del cuadrado => "))
        resultado = lado * lado
        print(f"Area cuadrado - Lado x lado - {lado} x {lado} = {resultado}")
    elif poligono == 'triangTulo':
        base = int(input("Introduce la base del triangulo => "))
        altura = int(input("Introfuce la altura del triangulo => "))
        resultado = (base * altura)/2
        print(f"Area triangulo - (Base x Altura) / 2 - ({base} x {altura}) / 2 = {resultado}")
    else:
        base = int(input("Introduce la base del triangulo => "))
        altura = int(input("Introfuce la altura del triangulo => "))
        resultado = base * altura
        print(f"Area rectangulo - (Base x Altura) - ({base} x {altura}) = {resultado}")


opcion = None
poligonos = ('triangulo','cuadrado','rectangulo')
while opcion not in poligonos:
    opcion = input("Introduzca un poligono para calcular area (Trinagulo/Cuadrado/Rectangulo) => ").lower()
    if opcion not in poligonos:
        print("Introduce un poligono correcto")
    else:
        calc_area(opcion)
