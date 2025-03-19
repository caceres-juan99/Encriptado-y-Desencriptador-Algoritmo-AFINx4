
alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóú"


n = 32**4  # 1048576


def palabra_a_numero(palabra):
    numero = 0
    for i, letra in enumerate(palabra):
        valor = alfabeto.index(letra)
        numero += valor * (32 ** (len(palabra) - i - 1))
    return numero

def desencriptar_afinx4(palabra_encriptada, a, b):
    numero_encriptado = palabra_a_numero(palabra_encriptada)

    inverso_a = pow(a, -1, n)  
    numero_desencriptado = (inverso_a * (numero_encriptado - b)) % n
    letras_desencriptadas = []

    
    for i in range(4):
        letras_desencriptadas.append(alfabeto[numero_desencriptado % 32])
        numero_desencriptado //= 32

    return ''.join(letras_desencriptadas[::-1])  


def dividir_palabra(palabra):
    return [palabra[i:i+4] for i in range(0, len(palabra), 4)]


def desencriptar_archivo(nombre_archivo_entrada, nombre_archivo_salida, a, b):
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
        texto_encriptado = archivo.read()  

    
    texto_desencriptado = ""

    
    for palabra in texto_encriptado.split(' '):
        if all(letra in alfabeto for letra in palabra) and not any(letra.isdigit() for letra in palabra):
            
            segmentos = dividir_palabra(palabra)
            
            for segmento in segmentos:
                texto_desencriptado += desencriptar_afinx4(segmento, a, b)  
        else:
            print(f"La palabra '{palabra}' contiene caracteres no válidos o números y será ignorada.")
        
        texto_desencriptado += ' '  

    
    texto_desencriptado = texto_desencriptado.rstrip()

    
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(texto_desencriptado)  


a = int(input("Ingrese el valor de la clave 'a': "))
b = int(input("Ingrese el valor de la clave 'b': "))  


nombre_archivo_entrada = 'Texto_encriptado.txt'  
nombre_archivo_salida = 'Texto desencriptado.txt'  


desencriptar_archivo(nombre_archivo_entrada, nombre_archivo_salida, a, b)
print(f'Texto desencriptado guardado en "{nombre_archivo_salida}".')