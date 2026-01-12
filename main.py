import os
import shutil

# Carpeta donde están los archivos a organizar
CARPETA_ORIGEN = "archivos"

# Tipos de archivos y sus carpetas destino
CARPETAS_DESTINO = {
    "PDF": [".pdf"],
    "Imagenes": [".jpg", ".jpeg", ".png"],
    "Documentos": [".txt", ".docx"],
    "Otros": []
}


def crear_carpetas():
    """
    Crea las carpetas destino si no existen
    """
    for carpeta in CARPETAS_DESTINO:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)


def obtener_extension(nombre_archivo):
    """
    Devuelve la extensión del archivo en minúsculas
    """
    return os.path.splitext(nombre_archivo)[1].lower()


def mover_archivo(nombre_archivo):
    """
    Mueve el archivo a la carpeta correspondiente según su extensión
    """
    extension = obtener_extension(nombre_archivo)

    for carpeta, extensiones in CARPETAS_DESTINO.items():
        if extension in extensiones:
            shutil.move(
                os.path.join(CARPETA_ORIGEN, nombre_archivo),
                os.path.join(carpeta, nombre_archivo)
            )
            return

    # Si no coincide con ningún tipo, va a "Otros"
    shutil.move(
        os.path.join(CARPETA_ORIGEN, nombre_archivo),
        os.path.join("Otros", nombre_archivo)
    )


def organizar_archivos():
    """
    Función principal que organiza todos los archivos
    """
    crear_carpetas()

    if not os.path.exists(CARPETA_ORIGEN):
        print("❌ La carpeta 'archivos' no existe.")
        return

    archivos = os.listdir(CARPETA_ORIGEN)

    if not archivos:
        print("📂 No hay archivos para organizar.")
        return

    for archivo in archivos:
        ruta_completa = os.path.join(CARPETA_ORIGEN, archivo)
        if os.path.isfile(ruta_completa):
            mover_archivo(archivo)

    print("✅ Archivos organizados correctamente.")


if __name__ == "__main__":
    organizar_archivos()