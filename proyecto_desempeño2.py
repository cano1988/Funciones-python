#importando librerías
from random import *
import random 
#Ingresando a casa de juegos por medio de un diccionario
print('')
print('******** INGRESA A LA CASA DE JUEGOS ********')
print('')
#Caso 1 con funciones convencionales

ingresando = {'usuario':'andres','clave':123}
def ingresar():
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        user = ingresando.get('usuario')
        key = ingresando.get('clave')

        if usuario.lower().strip() == user and int(clave) == key:
            print("")
            print('Bienvenido a la casa de juegos')
            break
        else:
            print('Usuario o clave errada, vuelve a intentarlo')

#opcion 1 (Lanzar moneda)
def lanzar_moneda():
        moneda = ('Cara','Cruz')
        aleatorio = choice(moneda)
        print(f'El lado de la moneda salió {aleatorio}')
        return aleatorio

lista_numeros = ['Amor','Salud','Dinero']
def probar_suerte(resultado,lista):
        if resultado == 'Cara':
            lista.clear()
            print(f'La lista de poesía fue vaciada: {lista}')
            return lista
        else:
            print(f"Obtuviste una lista de poesía...FELICITACIONES {lista}")
            return lista

#Inicia caso 2 con funciones lambda
palitos = ['-','--','---','----']
#
# #Mezclar palitos
shuffle_lista = lambda lista: random.sample(lista,len(lista))
#intento

intentos = lambda: int(input("Elige un número del 1 al 4: "))
probando_suerte = lambda : print(f'Tu suerte esta con el número {numero_elegido}')\
    if numero_elegido in (1,2,3,4) else print(f'numero {numero_elegido} no esta dentro de la lista')


#Comprobar intento
chequear_intento = lambda numero,lista,intento: print("A lavar los platos")\
    if shuffle_lista == '-' else print('Esta vez te has salvado de realizar una actividad')


#Línea para ejecutar nuestro código directamente
if __name__=="__main__":
    ingresar()
    print("")
    print("Opciones de juegos")
    print("1.  Lanzar moneda")
    print("2.  Dados")
    print("3.  Salir")
    opciones = (input("Elija el número del juego que desea: "))
    print("")
    if int(opciones) == 1:
        print('**** Este juego consite en tirar la moneda y si sale cruz obtendras una lista de poesía\n'
              'pero si sale cara obtendras una lista vacía, tienes tres intentos ****')
        intentos = 1
        while intentos <= 3:
            print("")
            lanzar = input('Desea lanzar moneda?\n1. Si \n2. No\nRespuesta: ')
            if int(lanzar) == 1:
                probar_suerte(lanzar_moneda(),lista_numeros)
                print(f'Te quedan {3 - intentos} intentos')
                intentos += 1
            else:
                print('Saliste de la casa de juegos')
                break
    elif int(opciones) == 2:
        print('**** Este juego consiste en elegir un numero que esta en el rango de una tupla de 1 a 4 y \n'
              'nos arroja un valor, si ese valor coincide con el de la tercera'
              ' funcion nos toca realizar una tarea. ****')
        print("")
        revolver_lista = input('Desea revolver?\n1. Si \n2. No\nRespuesta: ')
        if int(revolver_lista) == 1:
            palitos_mezclados = print(shuffle_lista(palitos))
            numero_elegido = intentos()
            seleccion = probando_suerte()
            chequear_intento(palitos_mezclados,probando_suerte,seleccion)
        else:
            print('Saliste de la casa de juegos')
    elif int(opciones) == 3:
        print('Vuelve pronto....')
