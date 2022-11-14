"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    filename = 'clusters_report.txt'
    file = open(filename, mode='r')
    titles1 = file.readline().split("  ")
    for _ in range(3): file.readline()
    titleTot = []
    for t in titles1:
        preTitle = t.strip()
        if(preTitle != ''):
            titleTot.append(preTitle)
    titleTot[1] += " palabras clave"
    titleTot[2] += " palabras clave"
    titleTot = [t.replace(" ", "_").lower() for t in titleTot]
    data = []
    palabrasClave = ""
    newRow = True
    row = []
    line = file.readline()
    while(line):
        if(newRow):
            aux = line.strip().replace('%', '').replace('  ', ' ')
            while('  ' in aux):
                aux = aux.replace('  ',' ')
            row = aux.split(' ')
            newRow = False
        elif(line.strip() == ''):
            newRow = True
            data.append([
                int(row[0]),
                int(row[1]),
                float(row[2].replace(",",".")),
                " ".join(row[3:])
            ])
        else:
            aux = line.strip().replace(".","")
            while('  ' in aux):
                aux = aux.replace('  ',' ')
            row += aux.split(' ')
        line = file.readline()
    df = pd.DataFrame(data, columns=titleTot)
    return df