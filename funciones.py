################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio: 04/10/2023 4:55 pm          #
#   Version: 3.11.4                            #
################################################
import csv
import xml.etree.ElementTree as tree
import xml.dom.minidom as minidom
import sys

sys.setrecursionlimit(1000)

def crearEstructura():
    """
    Función: obtiene los datos de un archivo CSV y los escribe en una estructura tipo lista
    Salidas:
    - listaPaises[1:](list): lista con todos los datos de cada país
    """
    listaPaises = []
    with open("./data/ArchivoDePaises.csv","r") as archivoP:
        i = -1
        lectorCSV = csv.reader(archivoP)
        for fila in lectorCSV:          
            nombre = fila[1]  #0 countryName
            codigos = [fila[0],fila[4],fila[5],fila[11],fila[12]]  #1 countryCode#0, fipsCode#1, isoNumeric#2, isoAlpha3#3, geonameId#4
            currencyCode = fila[2]  #2 currencyCode
            population = fila[3]  #3 population
            capital = fila[6]  #4 capital
            continente = [fila[7],fila[8]]  #5 continentName#0, continent#1
            areaInSqKm = fila[9]  #6 areaInSqKm
            lenguages = fila[10].split(",") #7 Lenguas 
            filaDatos = [nombre,codigos,currencyCode,population,capital,continente,areaInSqKm,lenguages]
            listaPaises.append(filaDatos)
            i += 1
        print("\n\n******************************************************************")
        print("***************** Archivo Creado con "+str(i)+" registros ***************")
        print("******************************************************************\n\n")
        return listaPaises[1:]
    
def crearArchivoXML(listaPaises):
    """
    Función: crea un archivo XML con la información de cada país 
    Entradas:
    - listaPaises(list): lista con todos los datos de cada país
    Salidas:
    datos.xml: archivo XML con lo especificado 
    """
    root = tree.Element("Paises")
    for lista in listaPaises:
        pais = tree.Element("Pais")
        root.append(pais)
       
        nombre = tree.SubElement(pais, "Nombre")
        nombre.text = (str(lista[0]))
        codigos = tree.SubElement(pais, "codigos")
        codigos.text = str(lista[1])
        codigoMoneda = tree.SubElement(pais, "codigoMoneda")
        codigoMoneda.text = str(lista[2])
        poblacion = tree.SubElement(pais, "poblacion")
        poblacion.text = str(lista[3])
        capital = tree.SubElement(pais, "capital")
        capital.text = str(lista[4])
        continente = tree.SubElement(pais, "continente")
        continente.text = str(lista[5])
        areaEnKm = tree.SubElement(pais, "areaEnKm")
        areaEnKm.text = str(lista[6])
        lenguages = tree.SubElement(pais, "lenguajes")
        lenguages.text = str(lista[7])
  
    xml_str = tree.tostring(root, encoding='utf-8')
    reparsed = minidom.parseString(xml_str)
    with open("./data/datos.xml", "wb") as archivo:
        archivo.write(reparsed.toprettyxml(indent="    ", encoding="utf-8"))
    print("\n\n*************************************************")
    print("***************** Archivo Creado ****************")
    print("*************************************************\n\n")
    return ""

def seleccionarContinente(listaPaises):
    """
    Función: crea un menu que permite al usuario elegir el continente
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    listaContinentes[opcion-1](list): lista con el continente elegido por el usuario
    """
    listaContinentes = []
    #Ciclo para crear la lista que se mostrara al usuario como submenu
    for pais in listaPaises:
        i = 0
        listaContinentes.append(pais[5])
        while i != len(listaContinentes):
            if listaContinentes.count(pais[5]) > 1:
                listaContinentes.pop()
            i += 1
    listaContinentes.sort() #Ordena la lista de manera alfabética par mostrarla en el submenu
    
    print("\n\n******************************************")
    print("********* Continentes disponibles ********")
    print("******************************************\n\n")
    #Ciclo que muestra el submenu
    for index,continent in enumerate(listaContinentes):
        print("\nIngrese "+ str(index+1) + ": " + str(continent))
    #Ciclo para que el usuario elija una opcion 
    while True:
        opcion = input("Ingrese un número: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(listaContinentes):
                return listaContinentes[opcion-1]
            else:
                print("\nEl número ingresado es invalido, debe ingresar un número del 1 al " + str(len(listaContinentes)) + "\n")
        except:
            print("\nEl número ingresado es invalido, asegúrese de que el número ingresado este en la lista de continentes disponibles de arriba\n")

def seleccionarMoneda(listaPaises):
    """
    Función: crea un menu que permite al usuario elegir una moneda
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    listaCompleta[opcion-1][0](dtr): texto con el tipo de moneda que eligió el usuario
    """
    listaMonedas = []
    cantidadMonedas = []
    #Ciclo para crear las listas que se mostrara al usuario como submenu 
    for pais in listaPaises:
        moneda = pais[2]
        if moneda in listaMonedas:
            pos = listaMonedas.index(moneda)
            cantidadMonedas[pos] += 1
        else:
            listaMonedas.append(moneda)
            cantidadMonedas.append(1)
            
    print("\n\n******************************************")
    print("*********** Monedas disponibles **********")
    print("******************************************\n\n")
    
    #Ciclo que concatena las monedas con la cantidad de paises que usan esta 
    listaCompleta = []
    for i in range(len(listaMonedas)):
        if cantidadMonedas[i] > 2:
            listaCompleta.append([listaMonedas[i],cantidadMonedas[i]])
    #Ciclo que imprime el submenu y permite al usuario elegir una opcion
    print("\n          Moneda   Cantidad de países")
    for index,(monedas,cantidad) in enumerate(listaCompleta):
        print("\nIngrese "+ str(index+1) + ": " + str(monedas)+ "            " + str(cantidad))
    while True:
        opcion = input("Ingrese un número: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(listaCompleta):
                return listaCompleta[opcion-1][0]
            else:
                print("\nEl número ingresado es invalido, debe ingresar un número del 1 al " + str(len(listaCompleta)) + "\n")
        except:
            print("\nEl número ingresado es invalido, asegúrese de que el número ingresado este en la lista de continentes disponibles de arriba\n")

def seleccionarPais(listaPaises,continente):
    """
    Función: crea un menu que permite al usuario elegir un país del continente elegido
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    listaPaisCot[opcion-1](list): lista con el continente elegido por el usuario
    """
    listaPaisesCont = []
    #Ciclo para crear la lista que se mostrara al usuario como submenu
    for pais in listaPaises:
        if continente == pais[5]:
            listaPaisesCont.append(pais[0])

    listaPaisesCont.sort() #Ordena la lista de manera alfabética par mostrarla en el submenu
    
    print("\n\n******************************************")
    print("********* Países disponibles ********")
    print("******************************************\n\n")
    #Ciclo que muestra el submenu
    for index,pais in enumerate(listaPaisesCont):
        print("\nIngrese "+ str(index+1) + ": " + str(pais))
    #Ciclo para que el usuario elija una opcion 
    while True:
        opcion = input("Ingrese un número: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(listaPaisesCont):
                return listaPaisesCont[opcion-1]
            else:
                print("\nEl número ingresado es invalido, debe ingresar un número del 1 al " + str(len(listaPaisesCont)) + "\n")
        except:
            print("\nEl número ingresado es invalido, asegúrese de que el número ingresado este en la lista de países disponibles de arriba\n")

def crearPaisesPorContinente(listaPaises):
    """
    Función: crea un archivo HTML con todos los países de un continente
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    opcion = seleccionarContinente(listaPaises) #Opción = continente elegido 
    #Creación del archivo HTML
    with open(f"./data/paisesPorContinente.html","w") as archivoContinente:
        archivoContinente.write("<meta charset='UTF-8'>")
        archivoContinente.write("<html><head><title>Paises Por Continente</title></head><body>")
        archivoContinente.write(f"<h1>Paises de {opcion[0]}</h1>")
        archivoContinente.write("<table>")
        archivoContinente.write("<tr style='background-color: #a2c8cc;'><th>Country Code</th><th>Nombre del pais</th><th>Capital</th><th>Poblacion</th><th>Area en kilometros cuadrados</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for pais in listaPaises:
            if pais[5] == opcion: # Si el pais pertenece al continente
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb"
                archivoContinente.write(f"<tr style='background-color: {fondo}'>")
                archivoContinente.write(f"<td>{pais[1][0]}</td>")
                archivoContinente.write(f"<td>{pais[0]}</td>")
                archivoContinente.write(f"<td>{pais[4]}</td>")
                archivoContinente.write(f"<td>{pais[3]}</td>")
                archivoContinente.write(f"<td>{pais[6]}</td>")
                i += 1
                archivoContinente.write("</tr>")
        
        archivoContinente.write("</table></body></html>")
        archivoContinente.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""

def crearCuantosViven(listaPaises):
    """
    Función: crea un archivo HTML con todos los paises ordenados por cantidades de población de mayor a menor
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    listaPaises.sort(key=lambda pais: int(pais[3]), reverse=True) #Ordena la lista por el mayor número de población
    #Creación del archivo HTML
    with open(f"./data/paisesPorPoblacion.html","w") as archivoPoblacion:
        archivoPoblacion.write("<meta charset='UTF-8'>")
        archivoPoblacion.write("<html><head><title>Paises Por Poblacion</title></head><body>")
        archivoPoblacion.write(f"<h1>Paises por poblacion de mayor a menor</h1>")
        archivoPoblacion.write("<table>")
        archivoPoblacion.write("<tr style='background-color: #a2c8cc;'><th>Poblacion</th><th>isoAlpha3</th><th>Nombre del pais</th><th>Area en kilometros cuadrados</th><th>Continente</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for pais in listaPaises:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoPoblacion.write(f"<tr style='background-color: {fondo}'>")
            archivoPoblacion.write(f"<td>{pais[3]}</td>")
            archivoPoblacion.write(f"<td>{pais[1][3]}</td>")
            archivoPoblacion.write(f"<td>{pais[0]}</td>")
            archivoPoblacion.write(f"<td>{pais[6]}</td>")
            archivoPoblacion.write(f"<td>{pais[5][0]}</td>")
            i += 1
            archivoPoblacion.write("</tr>")
        
        archivoPoblacion.write("</table></body></html>")
        archivoPoblacion.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
    return ""

def crearGrandePeque(listaPaises):
    """
    Función: crea un archivo HTML con todos los países ordenados por tamaño, de mayor a menor
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorTamaño.html: archivo HTML con la información pedida
    """
    listaPaises.sort(key=lambda pais: float(pais[6]), reverse=True) #Ordena la lista por ara en metros cuadrados
    #Creación del archivo HTML
    with open(f"./data/paisesPorTamaño.html","w") as archivoTamaño:
        archivoTamaño.write("<meta charset='UTF-8'>")
        archivoTamaño.write("<html><head><title>Paises Por Tamaño</title></head><body>")
        archivoTamaño.write(f"<h1>Paises de mayor tamaño a menor tamaño</h1>")
        archivoTamaño.write("<table>")
        archivoTamaño.write("<tr style='background-color: #a2c8cc;'><th>Area en kilometros cuadrados</th><th>flipCode</th><th>Nombre del pais</th><th>Continente</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for pais in listaPaises:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoTamaño.write(f"<tr style='background-color: {fondo}'>")
            archivoTamaño.write(f"<td>{pais[6]}</td>")
            archivoTamaño.write(f"<td>{pais[1][1]}</td>")
            archivoTamaño.write(f"<td>{pais[0]}</td>")
            archivoTamaño.write(f"<td>{pais[5][0]}</td>")
            i += 1
            archivoTamaño.write("</tr>")
        
        archivoTamaño.write("</table></body></html>")
        archivoTamaño.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""
        
def crearZonaAzul(listaPaises):
    """
    Función: crea un archivo HTML con los datos de los países marcados como zonas azules
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    zonasAzules = ["Costa Rica", "United States", "Greece", "Italy", "Japan"]
    with open(f"./data/paisesPorZonaAzul.html", "w") as archivoZonasAzules:
        archivoZonasAzules.write("<meta charset='UTF-8'>") 
        archivoZonasAzules.write("<html><head><title>Paises Por Zonas Azules</title></head><body>")
        archivoZonasAzules.write("<h1>Paises con Zonas Azules</h1>")
        archivoZonasAzules.write("<table>")
        archivoZonasAzules.write("<tr style='background-color: #a2c8cc;'><th>GeonameId</th><th>Nombre del pais</th><th>CurrencyCode</th><th>Lenguajes</th><th>Capital</th><th>Poblacion</th><th>Area en kilometros cuadrados</th></tr>")
        i = 0
        for zonAzul in zonasAzules:
            for pais in listaPaises:
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb" 
                if pais[0] == zonAzul:
                    archivoZonasAzules.write(f"<tr style='background-color: {fondo}'>")
                    archivoZonasAzules.write(f"<td>{pais[1][4]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[0]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[2]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[7]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[4]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[3]}</td>")
                    archivoZonasAzules.write(f"<td>{pais[6]}</td>")
                    archivoZonasAzules.write("</tr>")
                    i += 1
                
        archivoZonasAzules.write("</table></body></html>")
        archivoZonasAzules.close()
        print("\n\n******************************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " cantidad de registros *************")
        print("******************************************************************************************\n\n")
        return ""

def crearMismoIdioma(listaPaises):
    """
    Función: crea un archivo HTML con los datos de los países que hablan el mismo idioma
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    listaPaisIdioma = []
    todosIdiomas = []
    #Ciclo para separar cada pais por idioma, si estos se repiten, los divide con forme a todos los idiomas hablen
    for pais in listaPaises:
        for idiomasP in pais[7]:
            idioma = idiomasP.split("-")[0]
            if not idioma in todosIdiomas:
                todosIdiomas.append(idioma)
            listaPaisIdioma.append([idioma,pais[0],pais[5][0]])
    
    listaOrdenada = []
    #Ciclo que ordena la lista con la información de lenguaje-Cantidad de paises que hablan-Nombre del pais-Nombre del continente
    for lenguaje in todosIdiomas:
        paisLenguaje = ""
        continente = ""
        cantHablantes = 0
        for pais in listaPaisIdioma:
            if lenguaje == pais[0] and lenguaje != "":
                paisLenguaje += str(pais[1])+", "
                if not pais[2] in continente:
                    continente += str(pais[2])+", "
                cantHablantes += 1
        if cantHablantes >= 3:
            listaOrdenada.append([lenguaje,cantHablantes,paisLenguaje,continente])
    
    #Creación del archivo HTML
    with open(f"./data/IdiomasPorPais.html","w") as archivoMismoIdioma:
        archivoMismoIdioma.write("<meta charset='UTF-8'>")
        archivoMismoIdioma.write("<html><head><title>Paises por idioma</title></head><body>")
        archivoMismoIdioma.write(f"<h1>Paises por idioma</h1>")
        archivoMismoIdioma.write("<table>")
        archivoMismoIdioma.write("<tr style='background-color: #a2c8cc;'><th>Idioma</th><th>Cantidad de paises</th><th>Nombre de los paises</th><th>Nombre de los continentes</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for paises in listaOrdenada:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoMismoIdioma.write(f"<tr style='background-color: {fondo}'>")
            archivoMismoIdioma.write(f"<td>{paises[0]}</td>")
            archivoMismoIdioma.write(f"<td>{paises[1]}</td>")
            archivoMismoIdioma.write(f"<td>{paises[2]}</td>")
            archivoMismoIdioma.write(f"<td>{paises[3]}</td>")
            i += 1
            archivoMismoIdioma.write("</tr>")
        
        archivoMismoIdioma.write("</table></body></html>")
        archivoMismoIdioma.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""

def crearMismaMoneda(listaPaises):
    """
    Función: crea un archivo HTML con los países que tienen la misma moneda, ordenados por continente y alfabeto
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    moneda = seleccionarMoneda(listaPaises)
    listaPaises.sort(key=lambda pais: (pais[5][0], pais[0])) #Ordena la lista en continentes y a su vez a lo paises de manera alfabética 
    #Creación del archivo HTML
    with open(f"./data/mismaMoneda.html","w") as archivoMonedas:
        archivoMonedas.write("<meta charset='UTF-8'>")
        archivoMonedas.write("<html><head><title>Paises por misma moneda</title></head><body>")
        archivoMonedas.write(f"<h1>Paises que usan la moneda {moneda}</h1>")
        archivoMonedas.write("<table>")
        archivoMonedas.write("<tr style='background-color: #a2c8cc;'><th>Continente</th><th>Nombre del pais</th><th>Capital</th><th>Lenguajes</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for pais in listaPaises:
            if moneda == pais[2]: #Si la moneda del pais es la misma que el usuario eligió
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb"
                archivoMonedas.write(f"<tr style='background-color: {fondo}'>")
                archivoMonedas.write(f"<td>{pais[5][0]}</td>")
                archivoMonedas.write(f"<td>{pais[0]}</td>")
                archivoMonedas.write(f"<td>{pais[4]}</td>")
                archivoMonedas.write(f"<td>{pais[7]}</td>")
                i += 1
                archivoMonedas.write("</tr>")
        
        archivoMonedas.write("</table></body></html>")
        archivoMonedas.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""

def crearCodigoPais(listaPaises):
    """
    Función: crea un archivo HTML con los codigos de un país elegido por el usuario
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    continente = seleccionarContinente(listaPaises)
    buscarPais = seleccionarPais(listaPaises,continente)
    print(buscarPais)
    with open(f"./data/InformeCodigosPais.html","w") as archivoCodigo:
        archivoCodigo.write("<meta charset='UTF-8'>")
        archivoCodigo.write("<html><head><title>Informe de pais </title></head><body>")
        archivoCodigo.write(f"<h1>Informe del pais seleccionado</h1>")
        archivoCodigo.write("<table>")
        archivoCodigo.write("<tr style='background-color: #a2c8cc;'><th>Continente</th><th>Nombre del pais</th><th>CountryCode</th><th>flipCode</th><th>isoNumeric</th><th>isoAlpha3</th><th>geonameld</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for pais in listaPaises:
            if pais[0] == buscarPais:
                if i % 2 == 0:
                    fondo = "#c5e0dc"
                else:
                    fondo = "#f8edeb"
                archivoCodigo.write(f"<tr style='background-color: {fondo}'>")
                archivoCodigo.write(f"<td>{pais[5][0]}</td>")
                archivoCodigo.write(f"<td>{pais[0]}</td>")
                archivoCodigo.write(f"<td>{pais[1][0]}</td>")
                archivoCodigo.write(f"<td>{pais[1][1]}</td>")
                archivoCodigo.write(f"<td>{pais[1][2]}</td>")
                archivoCodigo.write(f"<td>{pais[1][3]}</td>")
                archivoCodigo.write(f"<td>{pais[1][4]}</td>")
                i += 1
                archivoCodigo.write("</tr>")
        
        archivoCodigo.write("</table></body></html>")
        archivoCodigo.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""  

def crearHablantesIdiomas(listaPaises):
    """
    Función: crea un archivo HTML con los idiomas hablados y la cantidad de hablantes que tiene
    Entradas:
    -listaPaises(list): lista con todos los datos de cada país
    Salidas:
    paisesPorContinente.html: archivo HTML con la información pedida
    """
    listaPaisIdioma = []
    todosIdiomas = []
    #Ciclo para separar cada pais por idioma, si estos se repiten, los divide con forme a todos los idiomas hablen
    for pais in listaPaises:
        for idiomasP in pais[7]:
            idioma = idiomasP.split("-")[0]
            if not idioma in todosIdiomas:
                todosIdiomas.append(idioma)
            listaPaisIdioma.append([idioma,pais[0],int(pais[3])])
    
    listaOrdenada = []
    #Ciclo que ordena la lista con la información de lenguaje-Pais:Poblacion-TotalDeHablantes
    for lenguaje in todosIdiomas:
        paisLenguaje = ""
        total = 0
        for pais in listaPaisIdioma:
            if lenguaje == pais[0] and lenguaje != "":
                if pais[2] > 0:
                    paisLenguaje += str(pais[1])+": "+str(pais[2])+"--"
                total += pais[2]
        if total != 0:
            listaOrdenada.append([lenguaje,paisLenguaje,total])
    listaOrdenada.sort()
    
    #Creación del archivo HTML
    with open(f"./data/totalHablantes.html","w") as archivoHablantes:
        archivoHablantes.write("<meta charset='UTF-8'>")
        archivoHablantes.write("<html><head><title>Total de hablantes</title></head><body>")
        archivoHablantes.write(f"<h1>Total de hablantes por idioma</h1>")
        archivoHablantes.write("<table>")
        archivoHablantes.write("<tr style='background-color: #a2c8cc;'><th>Idioma</th><th>Paises hablantes</th><th>Total de hablantes</th></tr>")
        i = 0
        #Ciclo para crear cada fila
        for paises in listaOrdenada:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoHablantes.write(f"<tr style='background-color: {fondo}'>")
            archivoHablantes.write(f"<td>{paises[0]}</td>")
            archivoHablantes.write(f"<td>{paises[1]}</td>")
            archivoHablantes.write(f"<td>{paises[2]}</td>")
            i += 1
            archivoHablantes.write("</tr>")
        
        archivoHablantes.write("</table></body></html>")
        archivoHablantes.close()
        print("\n\n***************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " registros *************")
        print("***************************************************************************\n\n")
        return ""
