from bs4 import BeautifulSoup
import requests
import csv

URL = "http://ramenparados.com/"
#Expecificamos el tipo de encoding dado que la pagina a analizar utiliza distintos simbolos fuera de lo normal
archivo = open("datos.csv",'w',encoding='utf-8-sig')

# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code

if status_code == 200:
    archivo.write("genero")
    archivo.write(";")
    archivo.write("titulo")
    archivo.write(";")
    archivo.write("autor")
    archivo.write(";")
    archivo.write("fecha")
    archivo.write("\n")

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('div', {'class': 'story-contain-text'})

    # Recorremos todas las entradas para extraer el genero, título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        genero = entrada.find('span', {'class': 'img-cat left'}).getText()
        titulo = entrada.find('h2').getText()
        autor = entrada.find('span', {'class': 'home-text-author left'}).getText()
        fecha = entrada.find('span', {'class': 'home-text-date left'}).getText()

        # Imprimo el resultado por pantalla y lo almacenamos en el archivo .csv
        print (i + 1, genero,titulo, autor, fecha)
        archivo.write(genero)
        archivo.write(";")
        archivo.write(titulo)
        archivo.write(";")
        archivo.write(autor)
        archivo.write(";")
        archivo.write(fecha)
        archivo.write("\n")

    archivo.close()

else:
    print ("Status Code %d" % status_code)