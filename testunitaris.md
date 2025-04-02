# Un test unitario es una prueba automatizada que se utiliza para verificar el comportamiento de una unidad específica de código, generalmente una función o un método, de manera aislada. El objetivo de los tests unitarios es asegurarse de que cada parte del código funcione correctamente por sí sola antes de integrarla con otras partes del sistema.

# Características de un test unitario:
## Aísla una unidad de código: Se prueba una función o método sin depender de otras partes del sistema.

## Automático: Se ejecuta sin intervención manual, lo que facilita su repetición.

## Rápido: Se ejecuta en pocos milisegundos para permitir muchas pruebas en poco tiempo.

## Determinista: Siempre debe dar el mismo resultado si la entrada es la misma.

## Independiente: No debe depender de otros tests ni de la base de datos o API externas.

### Ejemplo en Python con unittest:

import unittest

def sumar(a, b):
    return a + b

class TestSumar(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()


### Aquí, se prueban dos casos para la función sumar. Si alguno falla, el test reportará el error.