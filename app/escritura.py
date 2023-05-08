from bs4 import BeautifulSoup
from fractions import Fraction 
import requests
import cgi
import os

form_inputs = cgi.FieldStorage()          ##Revisa todo el documento HTML 

if form_inputs.getvalue('entry') is None: ##Revisa que se hayan llenado 
    entrada = ""                        ##todas las celdas de entrada
else:
    entrada = form_inputs.getvalue('entry') ##les asigna una variable en python
                                            ##para poder usarla más adelante


with open("puede.html") as file:    ##Abre el HTML para trabajar con el
    html = file.read()

                                    ##si no tuvieramos el documento, podriamos leer el enlace
                                    ##por eso dejé esto por aquí, para que, en caso de no tener
                                    ##el documento HTML, podamos ejecutar el programa solo con el enlace
                                    ##sería nomas copiar y pegar el enlace de la web
                                    ##y pegarlo en donde dice 'http://127.0.0.1:5500/puede.html'
                                    ##y nomas quitarles los signos de número para poder correr el programa
                                    ##normalmente
##url = 'http://127.0.0.1:5500/puede.html'
##html2 = requests.get(url)
##s1 = BeautifulSoup(html2.content, 'html.parser')
##table = s1.find(id = "matriz")


                                            ##lee todo el HTML para poder utilizar
                                            ##todas las lineas que tiene adentro en el codigo
                                            
soup = BeautifulSoup(html, 'html.parser')

                                            ##busca la parte donde está la tabla con las celdas
                                            ##donde se meten los númeritos; con filas y columnas
                                            ##y le asigna una variable en Python
table = soup.find(id = "matriz")

                                            ##Busca todas las Filas y las llama "rows"
                                            ##porque en inglés se oye mejor XD
                                            ##esto nos servirá para saber ¿cuántas filas tenemos en total?
                                            ##por default siempre vamos a tener 2 filas
rows = table.find_all("tr")


                                            ##esto de acá lo conservo porque chance y podríamos sustituir
                                            ##'row.find_all("td")' con 'entry', porque tienen la misma longitud y no se limitan
                                            ##a que haya el mismo número de filas y de columnas
##entry = table.find_all(class_='entrada')
##print("entradas: ", len(entry))

                                        ##Revisa ¿cúantas filas y cuantas columnas hay en el HTML
                                        ##por default siempre son 3 y 3
                                        ##o sea; num_rows = 3 ; num_cols = 3
num_rows = len(rows)
num_cols = len(rows[0].find_all("td"))

##crea el arreglo donde vamos a guardar nuestra matríz para hacerle el Gauss Jordan
##que vamos a importar.
matriz = []
for row in rows:                        ##crea el arreglo de filas y lo va
    fila = []                           ##llenando poco a poquito
    for cell in row.find_all("td"):     ##va leyendo todas las celdas y entradas
                                        ##del usuario
        valor = cell.find("input").get("value")
        print("valor:", valor)
        """if "/" in valor:
            try:
                vel = valor.split("/")
                print(vel)
                fraccion = Fraction(int(vel[0]), int(vel[1]))
                print("si pasé por aquí: ", fraccion)
                print("es un tipo de dato: ", type(fraccion))
                fila.append(fraccion)
            except ValueError:
                continue"""
        if valor:
            try:
                valor = int(valor)
                fila.append(valor)
            except ValueError:          ##verifica que el valor ingresado sea un número
                if "/" in valor:
                    vel = valor.split("/")
                    fraccion = Fraction(int(vel[0]), int(vel[1]))
                    fila.append(str(fraccion))
                    continue
                else:
                    print("Error: Ingrese un valor numérico")
                    exit()
    if len(fila) != num_cols:   ##verifica que haya el mismo número de filas y de columnas
                                ##para trabajar solamente con matrices cuadradas y que
                                ##podamos obtener la matriz Identidad
        print("Error: La matriz debe tener todas sus filas con la misma cantidad de elementos")
        exit()
    matriz.append(fila) ##mete el arreglo de filas en el arreglo de la matriz
                        ##y continúa hasta quedarse sin filas o columnas que leer

print("Matriz: ", matriz)               ##Nos muestra la matriz en modo de arreglo, por default tiene 9 elementos
print("Número de filas: ", num_rows)    ##nos indica cuantas filas hubo en total, por default siempre es 3
print("Número de columnas: ", num_cols) ##nos indica cuantas columnas hubo en total, por default siempre es de 3

arreglo = matriz                        ##guarda la matriz como un arreglo para hacerle Gauss-Jordan
m = num_rows                            ##guarda el número de filas para meterlo en el código de Gauss-Jordan
n = num_cols                            ##guarda el número de columnas para meterlo en el código de Gauss-Jordan

os.system(f"python algoritmo.py {a} {m} {n} {' '.join(map(str, arreglo))}")

"""Observación:
Para leer entradas ingresadas por el usuario, se agregó en el HTML el Boton
"Validar Matríz"; que mediante el metodo "POST", lee los datos ingresados por
el usuario y se ejecuta este código de Python :D"""