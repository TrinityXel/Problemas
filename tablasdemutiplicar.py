# One line to give the program's name and a brief description.
# Copyright © 2022 Trinity
# https://github.com/TrinityXel

# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.

"""
File: tablasdemultiplicar.py
Author: TrinityXel
Email: halrinachs@gmail.com
Github: https://github.com/TrinityXel
Description: Escriba una función en Python llamada tablasMultiplicar.
             La función solicita al usuario el ingreso
             de dos números n y m, ambos
             comprendidos entre 1 y 10, donde n representa el número
             correspondiente asociado a una tabla de multiplicar (por ejemplo
             la tabla del 3) y M representa la línea correspondiente de la
             tabla de multiplicar. Igualmente, la función debe leer una serie
             de archivos llamados tabla-n.txt con la tabla de multiplicar de
             ese número, y mostrar en pantalla la línea m del archivo. Si el
             archivo no existe, debe mostrar un mensaje por pantalla
             informando de ello.
"""

def main():
    # Crear los archivos: Comentar para no hacerlo...
    crear_tablas_multiplicar(10, 50)

    print(tablasMultiplicar(5, 0))


def tablasMultiplicar(tabla: int, linea: int) -> str:
    nombre = f"tabla-{tabla}.txt"
    lineas = []
    resultado = ""

    try:
        with open(nombre, "r") as archivo:
            lineas = archivo.readlines()
            resultado = lineas[linea - 1] if linea >= 1 else "0"
    except FileNotFoundError:
        resultado = f"No se encontró el archivo: {nombre}"

    return resultado


def crear_tablas_multiplicar(limiteT: int, limiteL: int):
    """
    Función para crear las tablas de multiplicar.
    No tiene manejo de errores: pj. comprobar existencia... etc

    @param: limiteT: Cantidad de tablas a crear
    @param: limiteL: Cantidad de multiplos a escribir
    """

    for tabla in range(1, limiteT + 1):
        nombre = "tabla-{}.txt".format(tabla)

        # Siempre creara los archivos o los sobre escribirá
        with open(nombre, "w") as archivo:
            for linea in range(1, limiteL + 1):
                texto = f"{tabla} x {linea} = {tabla*linea}\n"
                archivo.write(texto)


if __name__ == "__main__":
    main()
