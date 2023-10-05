################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
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
    try:
        opcion = int(input("Elija una opción: "))
        if opcion >=1 and opcion <=4:
            if opcion == 1:
                listaPaises = crearEstructura()
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
                    elif opcionHTML == 3:
                        crearGrandePeque(listaPaises)
                    elif opcionHTML == 4:
                        crearZonaAzul(listaPaises)
                    elif opcionHTML == 5:
                        crearMismoIdioma(listaPaises)
                    elif opcionHTML == 6:
                        crearMismaMoneda(listaPaises)
                    elif opcionHTML == 7:
                        crearCodigoPais(listaPaises)
                    elif opcionHTML == 8:
                        crearHablantesIdiomas(listaPaises)
                    else:
                        print("\n\n******************************************")
                        print("****** Ingrese una opción del 1 al 8 *****")
                        print("******************************************\n\n")
                        return menu(listaPaises)
            elif opcion == 4:
                print("\n\n****************************************************************************************************************")
                print("************ Programa Cerrado, esperamos le haya sido util la información consultada, vuelva pronto ************")
                print("****************************************************************************************************************\n\n") 
                return
            elif 2 <= opcion <= 3 and listaPaises == []:
                print("\n\n******************************************")
                print("*** No se ha creado ninguna estructura ***")
                print("******************************************\n\n")
                return menu(listaPaises)
        else:
            print("\n\n******************************************")
            print("****** Ingrese una opción del 1 al 4 *****")
            print("******************************************\n\n")
        return menu(listaPaises)
    except:
        print("\n\n***********************************************")
        print("****** Algo salio mal, regresando al menu *****")
        print("***********************************************\n\n")
        return menu(listaPaises)

# Main
listaPaises = []
menu(listaPaises)