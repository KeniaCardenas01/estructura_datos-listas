# base_datos.py

# Base de datos: Lista principal que almacena pares de números
lista_numeros = []

# Listas para tuplas
tuplas_pares = []
tuplas_impares = []

# Añadir par de números a lista
def agregar_par(num1, num2):
    lista_numeros.append([num1, num2])

# Eliminar el último par ingresado
def eliminar_ultimo_par():
    if lista_numeros:
        return lista_numeros.pop()
    return None

# Insertar par en posición específica
def insertar_par(posicion, num1, num2):
    lista_numeros.insert(posicion, [num1, num2])

# Eliminar par específico
def eliminar_par(par):
    if par in lista_numeros:
        lista_numeros.remove(par)

# Buscar índice de un par
def buscar_par(par):
    if par in lista_numeros:
        return lista_numeros.index(par)
    return -1

# Contar cuántas veces aparece un par
def contar_par(par):
    return lista_numeros.count(par)

# Ordenar la lista de pares
def ordenar_lista():
    lista_numeros.sort()

# Invertir la lista
def invertir_lista():
    lista_numeros.reverse()

# Mostrar lista actual
def obtener_lista():
    return lista_numeros

# Crear tupla de números pares
def crear_tupla_par(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        tupla = (num1, num2)
        tuplas_pares.append(tupla)
        return tupla
    return None

# Crear tupla de números impares
def crear_tupla_impar(num1, num2):
    if num1 % 2 != 0 and num2 % 2 != 0:
        tupla = (num1, num2)
        tuplas_impares.append(tupla)
        return tupla
    return None

# Mostrar tuplas
def obtener_tuplas_pares():
    return tuplas_pares

def obtener_tuplas_impares():
    return tuplas_impares

# Modificar una tupla (se convierte en lista, se cambia, y se vuelve a convertir en tupla)
def modificar_tupla(tipo, index, nuevo_valor):
    if tipo == "par" and 0 <= index < len(tuplas_pares):
        tuplas_pares[index] = tuple(nuevo_valor)
    elif tipo == "impar" and 0 <= index < len(tuplas_impares):
        tuplas_impares[index] = tuple(nuevo_valor)

# Eliminar una tupla
def eliminar_tupla(tipo, index):
    if tipo == "par" and 0 <= index < len(tuplas_pares):
        tuplas_pares.pop(index)
    elif tipo == "impar" and 0 <= index < len(tuplas_impares):
        tuplas_impares.pop(index)