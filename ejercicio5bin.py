def copiar_archivo_binario(origen, destino):
    try:
        with open(origen, "rb") as f_origen:
            contenido = f_origen.read()

        with open(destino, "wb") as f_destino:
            f_destino.write(contenido)

        print("Archivo binario copiado correctamente.")

    except FileNotFoundError:
        print("El archivo origen no existe.")
    except Exception as e:
        print("Error:", e)

# Prueba
copiar_archivo_binario("imagen.jpg", "imagen_copia.jpg")
