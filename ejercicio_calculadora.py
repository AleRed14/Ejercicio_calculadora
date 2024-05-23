# Enunciado
# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
# 1. Ingresar 1er operando (A=x)
# 2. Ingresar 2do operando (B=y)
# 3. Calcular todas las operaciones
# a) Calcular la suma (A+B)
# b) Calcular la resta (A-B)
# c) Calcular la división(A/B)
# d) Calcular la multiplicación(A*B)
# e) Calcular factorial(A!)
# 4. Informar resultados
# a) “El resultado de A+B es: r”
# b) “El resultado de A-B es: r”
# c) “El resultado de A/B es: r” o “No es posible dividir por cero”
# d) “El resultado de A*B es: r”
# e) “El factorial de A es: r1 y El factorial de B es: r2”
# 5. Salir
# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
# para realizar las cinco operaciones.
# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
# se debe mostrar el número cargado)
# • Deberán contemplarse los casos de error (división por cero, etc.)
# • Documentar todas las funciones

from funciones_calculadora import *
primer_operando = "x"
segundo_operando = "y"

lista_de_opciones = [f"{'Menu de opciones':^50s}",f"A - Primer operando (A={primer_operando})",
                     f"B - Segundo operando (B={segundo_operando})","C - Elegir operacion",
                     "D - Mostrar resultado","E - Salir"]

bandera_primer_operando = False
bandera_segundo_operando = False
bandera_realizar_operacion = False
seguir = True
while seguir:
    
    lista_de_opciones[1] = f"A - Primer operando (A={primer_operando})"
    lista_de_opciones[2] = f"B - Segundo operando (B={segundo_operando})"
    match menu_con_lista(lista_de_opciones):
        case "a":
            primer_operando = pedir_validar_numero_loop("Elija el primer operando: ")
            bandera_primer_operando = True
            bandera_realizar_operacion = False
        case "b":
            segundo_operando = pedir_validar_numero_loop("Elija el segundo operando: ")
            bandera_segundo_operando = True
            bandera_realizar_operacion = False
        case "c":
            lista_opciones_operaciones = [f"a) Calcular la suma ({primer_operando}+{segundo_operando})",
                            f"b) Calcular la resta ({primer_operando}-{segundo_operando})",
                            f"c) Calcular la división({primer_operando}/{segundo_operando})",
                            f"d) Calcular la multiplicación({primer_operando}*{segundo_operando})",
                            f"e) Calcular factorial({primer_operando}!)"]
            if bandera_primer_operando and bandera_segundo_operando:
                operacion_elegida = mostrar_lista(lista_opciones_operaciones)
                resultado_suma = sumar(primer_operando,segundo_operando)
                resultado_resta = restar(primer_operando,segundo_operando)
                if segundo_operando != 0:
                    resultado_division = dividir(primer_operando,segundo_operando)
                    bandera_division_cero = False
                else:
                    bandera_division_cero = True
                resultado_multiplicacion = multiplicar(primer_operando,segundo_operando)
                if type(primer_operando) == int:
                    primer_factorial = factorial(primer_operando)
                    bandera_primer_factorial = True
                else:
                    bandera_primer_factorial = False
                if type(segundo_operando) == int:
                    segundo_factorial = factorial(segundo_operando)
                    bandera_segundo_factorial = True
                else:
                    bandera_segundo_factorial = False
                bandera_realizar_operacion = True
            else:
                print("Tienen que poner un valor en los dos operando.")
        case "d":
            if bandera_realizar_operacion:
                print(f"El resultado de {primer_operando} + " 
                        f"{segundo_operando} es: {resultado_suma}")
                print(f"El resultado de {primer_operando} - " 
                        f"{segundo_operando} es: {resultado_resta}")
                if not bandera_division_cero:
                    print(f"El resultado de {primer_operando} / " 
                            f"{segundo_operando} es: {resultado_division}")
                else:
                    print("No es posible dividir por cero")
                print(f"El resultado de {primer_operando} * " 
                        f"{segundo_operando} es: {resultado_multiplicacion}")
                if bandera_primer_factorial:
                    print(f"El factorial de {primer_operando} es: "
                            f"{primer_factorial}")
                else:
                    print("No se puede factorizar el primer operando poque es un flotante")
                if bandera_segundo_factorial:
                    print(f"El factorial de {segundo_operando} es: {segundo_factorial}")
                else:
                    print("No se puede factorizar el segundo operando poque es un flotante")
                bandera_primer_operando = False
                bandera_segundo_operando = False
                bandera_realizar_operacion = False
            else:
                print("Primero tiene que hacer la operacion")
        case "e":
            seguir = not pedir_confirmacion("¿Quieres salir de la calculadora? s/n: ")
            continue
    pausar()
print("Fin del programa")