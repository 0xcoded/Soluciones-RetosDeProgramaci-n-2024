'''
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
'''
 
#Funciones establecidas
def no_ret_no_args():
     print("Hola Mundo!")

def ret_no_args():
    return 2**16

def ret_args(name):
    return f"Hola, {name}"

no_ret_no_args()
print(f"OUTPUT función: {ret_no_args()}")
print(ret_args("david"))

#Funciones del propio lenguaje
print(len("DAVID"))
print("DAVID".lower())

local_var = "Variable local"
print(local_var)

global_var = 10
def print_global_var():
    global global_var
    global_var += 10
    print(global_var)
print_global_var()

'''
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y
 retorne un número.
 * - La función imprime todos los números del 1 al 100.
 Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar
 en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar 
 para que el código se entienda.
'''

def str_function_numbers(string1,string2):
    for i in range(1,101):
        print(i)
        if i % 3 == 0 and not i % 5 == 0:
            print(string1)
        elif not i % 3 == 0 and i % 5 == 0:
            print(string2)
        else:
            print(string1 + string2)
    return i

print(f"Total de números analizados: {str_function_numbers("Hola ","Mundo")}")