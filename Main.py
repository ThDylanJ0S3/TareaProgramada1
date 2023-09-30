################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio:                             #
#   Version:                                   #
################################################
import csv
import xml.etree.ElementTree as tree
import sys
sys.setrecursionlimit(1000)
listaPaises = []
def crearEstructura():
    global listaPaises
    with open("./data/ArchivoDePaises.csv","r") as archivoP:
        i = 0
        lectorCSV = csv.reader(archivoP)

        for fila in lectorCSV:          
            nombre = fila[1]  # countryName
            codigos = [fila[0],fila[4],fila[5],fila[11],fila[12]]  # countryCode, fipsCode, isoNumeric, isoAlpha3, geonameId
            currencyCode = fila[2]  # currencyCode
            population = fila[3]  # population
            capital = fila[6]  # capital
            continente = [fila[7],fila[8]]  # continentName, continent
            areaInSqKm = fila[9]  # areaInSqKm
            lenguages = fila[10].split(",")
            filaDatos = [nombre,codigos,currencyCode,population,capital,continente,areaInSqKm,lenguages]
            listaPaises.append(filaDatos)
##        while i != len(listaPaises):
##            print("Lista",i,listaPaises[i])
##            i += 1
    
    

def crearXml():
    global listaPaises
    i=0
    root = tree.Element("Paises")
    for lista in listaPaises:
        pais = tree.Element("Pais")
        root.append(pais)
       
        nombre = tree.SubElement(pais, "Nombre")
        nombre.text = (str(listaPaises[i][0]))
        codigos = tree.SubElement(pais, "codigos")
        codigos.text = str(listaPaises[i][1])
        codigoMoneda = tree.SubElement(pais, "codigoMoneda")
        codigoMoneda.text = str(listaPaises[i][2])
        poblacion = tree.SubElement(pais, "poblacion")
        poblacion.text = str(listaPaises[i][3])
        capital = tree.SubElement(pais, "capital")
        capital.text = str(listaPaises[i][4])
        continente = tree.SubElement(pais, "continente")
        continente.text = str(listaPaises[i][5])
        areaEnKm = tree.SubElement(pais, "areaEnKm")
        areaEnKm.text = str(listaPaises[i][6])
        lenguages = tree.SubElement(pais, "lenguages")
        lenguages.text = str(listaPaises[i][7])
        i+=1
    
        
    arbol = tree.ElementTree(root)
    with open("./data/datos.xml", "wb") as archivo:
        arbol.write(archivo)
    
    
        
    
crearEstructura()
crearXml()
