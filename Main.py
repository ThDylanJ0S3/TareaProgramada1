################################################
#   Autor: Dylan Meza y Junior Monge           #
#   Fecha de creación: 21/09/2023  21:34 pm    #
#   Ultimo cambio:                             #
#   Version:                                   #
################################################
import csv

def crearEstructura():
    listaPaises = []
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
        while i != len(listaPaises):
            print("Lista",i,listaPaises[i])
            i += 1

crearEstructura()