import win32com.client
import os
import sys
import argparse
import glob


def main():
    usage = '%(prog)s -d | --directorio <Directorio Entrada> -s | --salida <Directorio Salida>'
    description = 'Script para Convertir los archivos Excel de un directorio en CSV'
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument('-d', '--directorio', action='store', nargs=1, dest='directorioIn',
                        help='Directorio de donde se leeran los Excels.', metavar="", required=True)
    parser.add_argument('-s', '--salida', action='store', nargs=1, dest='directorioOut',
                        help='Directorio de Salida de los CSV. (Opcional)', metavar="", required=False)

    # parsear los argumentos
    args = parser.parse_args()

    if not args.directorioOut:
        convertirArchivosExcel(args.directorioIn[0])
    else:
        convertirArchivosExcel(args.directorioIn[0], args.directorioOut[0])


def convertirArchivosExcel(directorio, directorioSalida=None):
    """Busca todos los archivos Excel en un directorio y los pasa a CSV"""

    # Verifico que el sea un directorio
    if not (os.path.exists(directorio) and os.path.isdir(directorio)):
        raise ConvertException(">>>>>>>> {0} no es un Directorio o no existe.".format(directorio))

    if (directorioSalida and not (os.path.isdir(directorioSalida))):
        directorioSalida = None

    archivosExcel = glob.glob(os.path.join(directorio, "*.xls"))

    if len(archivosExcel) == 0:
        raise Exception("No se encontraron archivos Excel en el directorio {0}.".format(directorio))

    for excel in archivosExcel:
        excel.replace('\\', '/')  # invertir las barras
        convertirXLS2CSV(excel, directorioSalida)
    return


def convertirXLS2CSV(archivo, directorioSalida=None):
    """Convierte un archivo Excel en CSV"""
    try:

        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = False

        archivoCSV = cambiarExtension(archivo, "CSV")  # Cambio la extension del archivo

        if (directorioSalida != None):
            archivoCSV = cambiarDirectorio(archivoCSV, directorioSalida)

        workbook = excel.Workbooks.Open(archivo)
        workbook.SaveAs(archivoCSV, 6)  # 6 representa CSV
        workbook.Close(True)
        excel.Quit()
        del excel
    except:
        raise ConvertException(">>>>>>> Fallo la conversion del archivo {0} a CSV".format(archivo))


def cambiarDirectorio(archivo, directorioNuevo):
    """Cambia el directorio en el que apuntara el nuevo archivo."""

    directorio, nombreArchivo = os.path.split(archivo)
    return os.path.join(directorioNuevo, nombreArchivo)


def cambiarExtension(archivo, formato):
    """Cambia la extension de un archivo pasado por parametro"""

    directorioArchivo, nombreArchivo = os.path.split(archivo)
    SoloNombre = os.path.splitext(nombreArchivo)
    nombreNuevo = SoloNombre[0] + "." + formato
    return os.path.join(directorioArchivo, nombreNuevo)


# Excel2csv user Exception
class ConvertException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    main()