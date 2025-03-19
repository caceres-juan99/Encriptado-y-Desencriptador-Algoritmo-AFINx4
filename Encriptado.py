
alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóú"


n = 32**4  # 1048576


def palabra_a_numero(palabra):
    numero = 0
    for i, letra in enumerate(palabra):
        valor = alfabeto.index(letra)
        numero += valor * (32 ** (len(palabra) - i - 1))
    return numero


def encriptar_afinx4(palabra, a, b):
    numero_palabra = palabra_a_numero(palabra)
    numero_encriptado = (a * numero_palabra + b) % n
    letras_encriptadas = []

    
    for i in range(4):
        letras_encriptadas.append(alfabeto[numero_encriptado % 32])
        numero_encriptado //= 32

    return ''.join(letras_encriptadas[::-1])  


def dividir_palabra(palabra):
    return [palabra[i:i+4] for i in range(0, len(palabra), 4)]


def encriptar_archivo(nombre_archivo_entrada, nombre_archivo_salida, a, b):
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()  

    
    texto_encriptado = ""

    
    for palabra in texto.split(' '):
        if all(letra in alfabeto for letra in palabra) and not any(letra.isdigit() for letra in palabra):
            
            segmentos = dividir_palabra(palabra)
            
            for segmento in segmentos:
                texto_encriptado += encriptar_afinx4(segmento, a, b)  
        else:
            print(f"La palabra '{palabra}' contiene caracteres no válidos o números y será ignorada.")
        
        texto_encriptado += ' '  

    
    texto_encriptado = texto_encriptado.rstrip()

   
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(texto_encriptado) 


a = int(input("Ingrese el valor de la clave 'a': "))
b = int(input("Ingrese el valor de la clave 'b': "))  


nombre_archivo_entrada = 'Texto sin encriptar.txt'  
nombre_archivo_salida = 'Texto_encriptado.txt'  


encriptar_archivo(nombre_archivo_entrada, nombre_archivo_salida, a, b)
print(f'Texto encriptado guardado en "{nombre_archivo_salida}".')