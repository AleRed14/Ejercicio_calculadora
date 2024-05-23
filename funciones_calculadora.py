def menu_calculadoras() -> str:
    """Muestra el manu de opciones, pide ingresar una letra para elegir una opcion

    Returns:
        str: La opcion elegida
    """
    limpiar_pantalla()
    print(f"{'Menu de opciones':^50s}")
    print("A - Primer operando")
    print("B - Segundo operando")
    print("C - Elegir operacion")
    print("D - Mostrar resultado")
    print("E - Salir")
    return input("Ingrese opcion: ").lower()

def menu_con_lista(lista:list) -> str:
    """Imprime una lista con las opciones de un menu y pide un string como opcion a elegir

    Args:
        lista (list): Lista con las opciones a mostrar

    Returns:
        str: El string de la opcion elegida
    """
    limpiar_pantalla()
    for opcion in lista:
        print(opcion)
    return input("Ingrese opcion: ").lower()

def mostrar_lista(lista:list)->None:
    """Imprime los elementos de una lista

    Args:
        lista (list): lista a imprimir
    """
    limpiar_pantalla()
    for elemento in lista:
        print(elemento)
def pedir_validar_numero_loop(mensaje:str)->any:
    """Pide un numero en bluce hasta que sea valide que sea entero o flotante

    Args:
        mensaje (str): Mensaje a mostrar cuando se pida el numero

    Returns:
        Any: El numero ingresado ya casteado, ya sea entero o flotante
    """
    
    while True:
        numero = input(mensaje)
        if validar_entero(numero):
            numero = int(numero)
            break
        elif validar_flotante(numero):
            numero = float(numero)
            break
        else:
            print("Eso no es un numero, vuelva a intentarlo:")
    return numero

def validar_entero(numero_a_probar:str) -> bool:
    """Valida que el numero sea un entero

    Args:
        numero_a_probar (str): cadena a validar

    Returns:
        bool: True si el texto es un entero, false en caso contrario
    """
    return numero_a_probar.isalnum()

def validar_flotante(numero_a_probar:str) -> bool:
    """Valida que el numero sea un flotante

    Args:
        numero_a_probar (str): cadena a validar

    Returns:
        bool: True si el texto es un flotante, false en caso contrario
    """
    try:
        float(numero_a_probar)
        retorno = True
    except ValueError:
        retorno = False
    return retorno

def limpiar_pantalla()->None:
    """Limpia la pantalla
    """
    import os #Viene de sistema operativo
    os.system("cls") # Se encarga de limpiar la pantalla de todo lo de atras

def pedir_confirmacion(mensaje:str)->bool:
    """Pide confirmacion de salida

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        bool: Retorna True si la respuesta es si, false en caso contrario
    """
    rta = input(mensaje).lower()
    return rta == "s"

def pausar()->None:
    """Pausa el programa para leerlo
    """
    import os #Viene de sistema operativo
    os.system("pause") # Pausa el programa hasta que se toque alguna tecla, 
                       #sirve para que no se borre insantaneamente lo mostrado

def sumar(primer_operando, segundo_operando)->any:
    """Suma los dos numeros recividos

    Args:
        primer_operando (num): Primer numero a sumar
        segundo_operando (num): Segundo numero a sumar

    Returns:
        any: Numero del resultado de la suma, ya sea entero o flotante
    """
    return primer_operando + segundo_operando

def restar(primer_operando,segundo_operando)->any:
    """Resta dos numeros

    Args:
        primer_operando (num): Primer numero a restar
        segundo_operando (num): Segundo numero a restar

    Returns:
        any: El resultado de la resta, ya sea entero o flotante
    """
    return primer_operando - segundo_operando

def multiplicar(primer_operando,segundo_operando)->any:
    """Multiplica dos numero

    Args:
        primer_operando (num): primer numero a multiplicar
        segundo_operando (num): segundo numero a multiplicar

    Returns:
        any: el resultado de la multiplicacion, ya sea entero o flotante
    """
    return primer_operando * segundo_operando

def dividir(dividendo,divisor)->float:
    """Divide un numero

    Args:
        dividendo (num: numero a dividir
        divisor (num): numero que divide

    Returns:
        float: el resultado de la division
    """
    return dividendo / divisor

def factorial_funcion(numero:int) -> int:
    """Calcula el factorial de un numero

    Args:
        numero (int): Numero que se busca el factorial

    Returns:
        int: el factorial del numero
    """
    from math import factorial
    return factorial(numero)

def factorial(numero:int) -> int:
    """Calcula el factorial de un numero

    Args:
        numero (int): Numero que se busca el factorial

    Returns:
        int: El factorial del numero
    """
    resultado = 1
    for i in range(2,numero + 1):
        resultado *= i
    return resultado