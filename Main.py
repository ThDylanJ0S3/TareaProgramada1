################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio:                             #
#   Version:                                   #
################################################

from funciones import *

def menu(listaPaises):
    print("\n\n******************************************")
    print("************* Menu Principal *************")
    print("******************************************\n\n")
    print("\nDigite 1: Crear estructura")
    print("\nDigite 2: Generar XML")
    print("\nDigite 3: Construir HTML")
    print("\nDigite 4: Salir\n")
    opcion = int(input("Elija una opción: "))
    if opcion >=1 and opcion <=4:
        if opcion == 1:
            listaPaises = crearEstructura()
            print("\n\n******************************************")
            print("************* Archivo Creado *************")
            print("******************************************\n\n")
        elif opcion == 2 and listaPaises != []:                
            crearArchivoXML(listaPaises)
        elif opcion == 3 and listaPaises != []:
            print("\n\n******************************************")
            print("************* Ordenar Países *************")
            print("******************************************\n\n")
            print("\nDigite 1: Países por continente")
            print("\nDigite 2: ¿Cuántos viven?")
            print("\nDigite 3: De grandes a pequeños")
            print("\nDigite 4: Zonas Azules")
            print("\nDigite 5: Países con el mismo idioma")
            print("\nDigite 6: Pago con la misma moneda")
            print("\nDigite 7: Códigos de un determinado país")
            print("\nDigite 8: Hablantes por idioma\n")
            opcionHTML = int(input("Elija una opción: "))
            if opcionHTML >=1 and opcion <=8:
                if opcionHTML == 1:
                    crearPaisesPorContinente(listaPaises)
                elif opcionHTML == 2:
                    crearCuantosViven(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 3:
                    crearGrandePeque(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 4:
                    crearZonaAzul(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 5:
                    crearMismoIdioma(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 6:
                    crearMismaMoneda(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 7:
                    crearCodigoPais(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                elif opcionHTML == 8:
                    crearHablantesIdiomas(listaPaises)
                    print("\n\n******************************************")
                    print("************* Archivo Creado *************")
                    print("******************************************\n\n") 
                else:
                    print("\n\n******************************************")
                    print("****** Ingrese una opción del 1 al 8 *****")
                    print("******************************************\n\n")
                    return menu(listaPaises)
        elif opcion == 4:
            print("\n\n******************************************")
            print("************ Programa Cerrado ************")
            print("******************************************\n\n") 
            return
        elif 2 <= opcion <= 4 and listaPaises == []:
            print("\n\n******************************************")
            print("*** No se ha creado ninguna estructura ***")
            print("******************************************\n\n")
            return menu(listaPaises)
    else:
        print("\n\n******************************************")
        print("****** Ingrese una opción del 1 al 4 *****")
        print("******************************************\n\n")
    return menu(listaPaises)

# Main
listaPaises = []
menu(listaPaises)