from algoritmo import gaussJ 
from fractions import Fraction


archivo = open("archivo.txt", "r")
lineas = archivo.readlines()
archivo.close()

numeros_antes = []
numeros_despues = []
max_numeros_antes = 0
contador_m = 0

for linea in lineas:
    # Contar líneas
    contador_m += 1

    # Revisar si la línea contiene letras
    if any(c.isalpha() for c in linea):
        print("Matriz inválida, verifica que NO contenga LETRAS o que NO SEA NULA")
        exit()

    # Buscar el índice del símbolo "=" en la línea
    index = linea.find("=")
    if index != -1:
        # Dividir la línea en dos partes por el signo "="
        parte1 = linea[:index].strip()
        parte2 = linea[index+1:].strip()

        # Leer los números de cada parte y detectar si deben ser negativos
        numeros1 = [Fraction(x) if not (x.startswith('-') and x[1:].isdigit()) else -Fraction(x[1:]) for x in parte1.split()]
        numeros2 = [Fraction(x) if not (x.startswith('-') and x[1:].isdigit()) else -Fraction(x[1:]) for x in parte2.split()]

        # Contar el número de números en la línea antes del signo "="
        num_numeros_antes = len(numeros1)
        if num_numeros_antes > max_numeros_antes:
            max_numeros_antes = num_numeros_antes

        # Agregar los números a los arreglos correspondientes
        numeros_antes.extend(numeros1)
        numeros_despues.extend(numeros2)

# Para evitar que se metan matrices nulas
if all(num == 0 for num in numeros_antes):
        print("Matriz inválida, verifica que NO contenga LETRAS o que NO SEA NULA")
        exit()
        
for i in range(0, len(numeros_antes), contador_m):
        if all(num == 0 for num in numeros_antes[i:i+contador_m]):
            print("Matriz inválida, la línea", i//contador_m+1, "contiene todos los números de antes del signo '=' iguales a cero.")
            exit()



# Imprimir resultado
if numeros_antes and numeros_despues:
    print("Números antes del signo'=':", numeros_antes)
    print("Números después del signo '=':", numeros_despues)

print("m:", contador_m)
print("n:", max_numeros_antes)

# Crear matriz de fracciones vacía
matriz = [[0]*max_numeros_antes for _ in range(contador_m)]

# Llenar matriz con fracciones
indice = 0
for i in range(contador_m):
    for j in range(max_numeros_antes):
        if j < len(numeros_antes) and indice < len(numeros_antes):
            matriz[i][j] = Fraction(numeros_antes[indice])
            indice += 1

# Imprimir matriz
for fila in matriz:
    print(fila)



#######################################################################################################
#implementación GJ
g = gaussJ(matriz, contador_m, max_numeros_antes, numeros_despues)
print("GAUSS JORDAN \n\n")

for i in range(contador_m):
    for j in range(max_numeros_antes):
        if i < len(g) and j < len(g[i]):
          print(g[i][j])
    print(end="\n")
    
    ##HOLA :D
