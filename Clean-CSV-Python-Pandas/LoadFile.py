from tkinter import Tk
from tkinter import filedialog

class LoadFile:
    """
    Gestiona la selección y guardado de archivos CSV mediantes dialogos nativos del sistema.

    Utiliza TKinter para desplegar cuadros de dialogos del sistema operativo
    que permitan al usuario elegir un archivo existente (para abrir) o
    definir la ruta de destino (para guardar), restringido a archivos CSV.

    Attributes:
        __file_path (str): Ruta absoluta del archivo seleccionado o guardado.
            es un atributo privado; se accede a su valor a través del retorno
            de los metodos open_choose_file() save_file()
    """

    def __init__(self):
        self.__file_path = ''

    def open_choose_file(self):
        root = Tk()
        root.withdraw()

        file = filedialog.askopenfilename(
            title="Seleccionar Archivo",
            filetypes=[("CSV files", "*.csv")]
        )
        self.__file_path = file
        return self.__file_path

    def save_file(self):
        path = filedialog.asksaveasfilename(
            title="Guardar",
            defaultextension=".csv",
            initialfile="output")

        self.__file_path = path
        return self.__file_path
