################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio:                             #
#   Version:                                   #
################################################
import csv
import xml.etree.ElementTree as tree
import xml.dom.minidom as minidom
import sys

sys.setrecursionlimit(1000)

def crearEstructura():
    listaPaises = []
    with open("./data/ArchivoDePaises.csv","r") as archivoP:
        i = 0
        lectorCSV = csv.reader(archivoP)

        for fila in lectorCSV:          
            nombre = fila[1]  #0 countryName
            codigos = [fila[0],fila[4],fila[5],fila[11],fila[12]]  #1 countryCode, fipsCode, isoNumeric, isoAlpha3, geonameId
            currencyCode = fila[2]  #2 currencyCode
            population = fila[3]  #3 population
            capital = fila[6]  #4 capital
            continente = [fila[7],fila[8]]  #5 continentName, continent
            areaInSqKm = fila[9]  #6 areaInSqKm
            lenguages = fila[10].split(",") #7 Lenguas 
            filaDatos = [nombre,codigos,currencyCode,population,capital,continente,areaInSqKm,lenguages]
            listaPaises.append(filaDatos)
        return listaPaises[1:]
    
def crearArchivoXML(listaPaises):
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
    with open("./ArchivosCreados/datos.xml", "wb") as archivo:
        archivo.write(reparsed.toprettyxml(indent="    ", encoding="utf-8"))
    print("Se ha creado el archivo")
        
def crearPaisesPorContinente(listaPaises):
    opcion = selecionarContinente(listaPaises)
    with open(f"./ArchivosCreados/paisesPorContinente.html","w") as archivoContinente:
        archivoContinente.write("<html><head><title>Paises Por Continente</title></head><body>")
        archivoContinente.write(f"<h1>Paises de {opcion[0]}</h1>")
        archivoContinente.write("<table>")
        archivoContinente.write("<tr style='background-color: #a2c8cc;'><th>Country Code</th><th>Nombre del país</th><th>Capital</th><th>Población</th><th>Área en metros cuadrados</th></tr>")
        i = 0
        for pais in listaPaises:
            if pais[5] == opcion:
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
        print("\n\n******************************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " cantidad de registros *************")
        print("******************************************************************************************\n\n")

def selecionarContinente(listaPaises):
    listaContinentes = []
    for pais in listaPaises:
        i = 0
        listaContinentes.append(pais[5])
        while i != len(listaContinentes):
            if listaContinentes.count(pais[5]) > 1:
                listaContinentes.pop()
            i += 1
    listaContinentes.sort()
    print("\n\n******************************************")
    print("********* Continentes disponibles ********")
    print("******************************************\n\n")
    i = 1
    for index,continent in enumerate(listaContinentes):
        print("Ingrese "+ str(index+1) + ": " + str(continent))
    while True:
        opcion = input("Ingrese un número: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(listaContinentes):
                return listaContinentes[opcion-1]
            else:
                print("\nEl número ingresado es invalido, debe ingresar un número del 1 al " + str(len(listaContinentes)) + "\n")
        except:
            print("\nEl número ingresado es invalido, asegúrese de que el número ingresado este en la lisa de continentes disponibles de arriba\n")
def crearCuantosViven(listaPaises):
    return "Funcion por construir"
def crearGrandePeque(listaPaises):
    listaPaises.sort(key=lambda pais: float(pais[6]), reverse=True)
    with open(f"./ArchivosCreados/paisesPorTamaño.html","w") as archivoContinente:
        archivoContinente.write("<html><head><title>Paises Por Tamaño</title></head><body>")
        archivoContinente.write(f"<h1>Paises de mayor tamaño a menor tamaño</h1>")
        archivoContinente.write("<table>")
        archivoContinente.write("<tr style='background-color: #a2c8cc;'><th>Área en metros cuadrados</th><th>flipCode</th><th>Nombre del país</th><th>Continente</th></tr>")
        i = 0
        for pais in listaPaises:
            if i % 2 == 0:
                fondo = "#c5e0dc"
            else:
                fondo = "#f8edeb"
            archivoContinente.write(f"<tr style='background-color: {fondo}'>")
            archivoContinente.write(f"<td>{pais[6]}</td>")
            archivoContinente.write(f"<td>{pais[1][1]}</td>")
            archivoContinente.write(f"<td>{pais[0]}</td>")
            archivoContinente.write(f"<td>{pais[5][0]}</td>")
            i += 1
            archivoContinente.write("</tr>")
        
        archivoContinente.write("</table></body></html>")
        archivoContinente.close()
        print("\n\n******************************************************************************************")
        print("************* Archivo HTML creado con " +str(i) + " cantidad de registros *************")
        print("******************************************************************************************\n\n")
def crearZonaAzul(listaPaises):
    return "Funcion por construir"
def crearMismoIdioma(listaPaises):
    return "Funcion por construir"
def crearMismaMoneda(listaPaises):
    return "Funcion por construir"
def crearCodigoPais(listaPaises):
    return "Funcion por construir"
def crearHablantesIdiomas(listaPaises):
    return "Funcion por construir"