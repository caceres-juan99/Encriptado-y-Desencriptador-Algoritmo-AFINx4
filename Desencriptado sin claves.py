import random
import sys

# Definiciones necesarias
n = 32**4  # 1'048.576
alfabeto = 'abcdefghijklmnopqrstuvwxyzñ'  # Definimos el alfabeto
len_alfabeto = len(alfabeto)  # Longitud del alfabeto

# Función para leer la tabla de inversos
def leer_tabla_inversos(nombre_archivo):
    tabla_inversos = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            a, inverso = map(int, linea.strip().split(','))
            tabla_inversos[a] = inverso
    return tabla_inversos

# Función para desencriptar un texto con claves 'a' y 'b'
def desencriptar(texto_encriptado, a, b):
    texto_desencriptado = ''
    
    # Aplicar la fórmula de desencriptación
    for char in texto_encriptado:
        if char in alfabeto:
            char_index = alfabeto.index(char)
            # Fórmula de desencriptación
            nuevo_index = (a * (char_index - b)) % len_alfabeto
            # Asegúrate de que nuevo_index esté dentro de los límites del alfabeto
            texto_desencriptado += alfabeto[nuevo_index]
        else:
            texto_desencriptado += char  # Mantener caracteres no alfabéticos
    return texto_desencriptado

# Función para aplicar un análisis lingüístico básico
def analisis_linguistico(texto_desencriptado):
    # Ejemplo de análisis de frecuencia de consonantes y vocales
    consonantes_comunes = 'rnsln'  # Algunas consonantes comunes en español
    vocales_comunes = 'aeo'  # Algunas vocales comunes en español
    frecuencias_consonantes = sum(1 for char in texto_desencriptado if char in consonantes_comunes)
    frecuencias_vocales = sum(1 for char in texto_desencriptado if char in vocales_comunes)
    
    # Si el texto tiene una buena distribución de consonantes y vocales, podemos considerarlo
    if frecuencias_consonantes > 2 and frecuencias_vocales > 2:
        return True
    return False

# Lista de palabras clave comunes en español
palabras_clave_comunes = [
    "deññ", "laññ", "queññ", "elññ", "enññ", "yññ", "aññ", "losñ", "porñ", "conñ",
    "unañ", "suññ", "para", "esññ", "alññ", "como", "seññ", "delñ", "oñññ", "másñ",
    "pero", "susñ", "leññ", "todo", "yaññ", "entreñññ", "este", "cuandoññ", "muyñ",
    "sinñ", "sobreñññ", "tambiénñ", "fueñ", "hastañññ", "desdeñññ", "todo", "hayñ", 
    "cada", "todo", "cual", "bien", "menosñññ", "cada", "otro", "pues", "nosñ", 
    "teññ", "eseñ", "esañ", "tantoñññ", "dosñ", "hacerñññ", "díañ", "dondeñññ", "tieneñññ",
    "poco", "meññ", "añoñ", "esoñ", "túññ", "tiempoññ", "síññ", "hoyñ", "parteñññ", 
    "ahíñ", "niññ", "cosa", "antesñññ", "mismañññ", "hace", "misñ", "trabajoñ", 
    "decirñññ", "despuésñ", "muchoñññ", "nuevoñññ", "ella", "ellosñññ", "ustedñññ", 
    "quieroññ", "pareceññ", "quiénñññ", "cómo", "mismoñññ", "yoññ", "tienesññ", "verñ", 
    "tanñ", "menosñññ", "esto", "estosñññ", "estasñññ", "ahíñ", "seañ", "quiereññ", 
    "bajo", "otra", "formañññ", "maneraññ", "personañ", "muchosññ", "algunosñ", 
    "mayorñññ", "menosñññ", "aquí", "esos", "esas", "hombreññ", "mujerñññ", "genteñññ", 
    "primeroñ", "mismoñññ", "tardeñññ", "entonces", "nuncañññ", "bastante", "días", 
    "talñ", "gran", "primerañ", "está", "hechoñññ", "momentoñ", "tipo", "quizásññ", 
    "manosñññ", "igualñññ", "ciertoññ", "grupoñññ", "algunaññ", "caso", "sabe", "debe", 
    "ciudadññ", "historia", "lugarñññ", "obra", "frenteññ", "familiaññ", "calleñññ", 
    "nombreññ", "mientras", "mujeresñ", "trabajar", "puebloññ", "debajoññ", 
    "amigosññ", "edad", "razónñññ", "medioñññ", "temprano", "frío", "calorñññ", 
    "mesñ", "aúnñ", "puertaññ", "finñ", "hechoñññ", "habíañññ", "ahorañññ", "unoñ", "vida",
    "siempreñ"
]

# Nombre del archivo donde se encuentra la tabla de inversos modulares
nombre_archivo_inversos = 'tabla_inversos_modulares.txt'

# Leer la tabla de inversos modulares
tabla_inversos = leer_tabla_inversos(nombre_archivo_inversos)

# Probar todas las combinaciones posibles de claves 'a' y 'b'
texto_encriptado = "Texto encriptado aquí"  # Cambia esto por el texto que quieres desencriptar

# Desencriptado en tiempo real
for a in tabla_inversos.keys():
    for b in range((n // 2) + 1, n):  # 'b' superior a la mitad más uno
        texto_desencriptado = desencriptar(texto_encriptado, a, b)
        
        # Realizamos el análisis lingüístico y verificamos si es coherente
        if analisis_linguistico(texto_desencriptado):
            # Si es coherente, mostramos el resultado
            print(f"Desencriptado con a={a} y b={b}: {texto_desencriptado}")
            sys.stdout.flush()  # Forzamos la impresión en tiempo real