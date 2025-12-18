#copiar el contenido de un archivo txt a otro

def copiar_archivo_texto(origen, destino):
    try:
        with open(origen, "r", encoding="utf-8") as f_origen:
            contenido = f_origen.read()

        with open(destino, "w", encoding="utf-8") as f_destino:
            f_destino.write(contenido)

        print("Archivo de texto copiado correctamente.")

    except FileNotFoundError:
        print("El archivo origen no existe.")
    except Exception as e:
        print("Error:", e)


# Prueba
copiar_archivo_texto("archivo_origen.txt", "archivo_copia.txt")
