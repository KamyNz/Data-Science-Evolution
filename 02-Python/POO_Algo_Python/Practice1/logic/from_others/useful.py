def raizbruta(numero, epsilon = .0001):
    """
    Calcula la raiz cuadrada con un error de epsilon recorriendo los números flotantes entre
    0 y numero con un paso de epsilon

    numero float >0 al cual se calcula la raíz
    epsilon float >0 tolerancia del error
    """
    assert type(numero) == float, f'argumento número debe tener formato float'
    assert numero >0, f'argumento número debe ser positivo'
    assert type(epsilon) == float, f'argumento epsilon debe tener formato float'
    assert epsilon >0, f'argumento epsilon debe ser positivo'

    prueba = epsilon
    conteo = 1

    while numero-prueba**2 > epsilon:
        prueba += epsilon
        conteo += 4
        """
        1   elevar al cuadrado
        1   restar numero-prueba**2
        1   evaluar desigualdad
        1   sumar epsilon
        4   total sin contar asignaciones
        """
    print(f'Con una tolerancia de {epsilon} se usaron {conteo} cálculos para raizbruta')
    return prueba

def raizbiseccion(numero, epsilon = .0001):
    """
    Calcula la raiz con la busqueda por bisección para un error de epsilon.
    numero float >0 del cual queremos la raiz
    epsilon float >0 es el error o tolerancia para la aproximación
    """
    assert type(numero) == float, f'argumento número debe tener formato float'
    assert numero >0, f'argumento número debe ser positivo'
    assert type(epsilon) == float, f'argumento epsilon debe tener formato float'
    assert epsilon >0, f'argumento epsilon debe ser positivo'
    prueba = 1
    conteo = 1
    while abs(prueba**2 - numero) > epsilon:
        prueba = (numero/prueba+prueba)*.5
        conteo += 7
        """
        1   elevar al cuadrado
        1   restar numero
        1   calcular abs
        1   evaluar la desigualdad
        1   numero/prueba
        1   sumar prueba
        1   multiplicar por .5
        7   total de operaciones (sin contar asignaciones)
        """
    print(f'Con una tolerancia de {epsilon} se usaron {conteo} cálculos para raizbiseccion')
    return prueba

if __name__ == '__main__':

    numero = 2.

    for i in range(1,8):
        epsilon=10**(-1*i)
        print(raizbruta(numero,epsilon))
        print(raizbiseccion(numero,epsilon))
