from pandas import read_csv, DataFrame, to_datetime
from pandas.errors import ParserError


class CleanCSV:
    """
    Carga y limpia un archivo CSV, normalizando columnas especificas.

    Encapsula un DataFrame de Pandas (privado) y expone metodos para
    inspeccionar el archivo cargado y normalizar columna conocidas
    (Join_Date, Age, Phone) antes de guardar el resultado.

    Attributes:
        __df (DataFrame | None): DataFrame cargado desde el CSV. None hasta
            que se llame a load_file().

        __path(str): Ruta del archivo CSV a cargar.
    """
    def __init__(self, file_path):
        self.__df = None
        self.__file_path = file_path

    def load_file(self):
        """
        Carga un archivo CSV en un DataFrame interno.

        Raises:
            ParserError: Si el archivo no existe, no es un CSV valido
                o tiene problemas de codificacicion.
        """
        try:
            self.__df = read_csv(self.__file_path)
        except (UnicodeDecodeError, ParserError):
            raise ParserError('Error: El archivo no es un archivo CSV valido.')


    def show_head_file_csv(self):
        """
        Devuelve las primera 10 filas del DataFrame.

        Returns:
            DataFrame: primeras 10 filas.
        """
        return self.__df.head(10)

    def show_tail_file_csv(self):
        """
        Devuelve las ultimas 10 filas del DataFrame.

        Returns:
            DataFrame: ultimas 10 filas.
        """
        return self.__df.tail(10)

    def show_info_file_cvs(self):
        """
        Genera un resumen de columnas, tipos de datos y conteo de valores no nulos.

        Returns:
            DataFrame: Tabla con columnas 'Columns', 'Dtype', y 'non-null Count'.
        """
        df_info = DataFrame({
            'Columns': self.__df.columns,
            'Dtype': self.__df.dtypes,
            'non-null Count': self.__df.count().values
        })

        return df_info

    def show_null_files_csv(self):
        """
        Cuenta valores nulos por columnas.

        Returns:
            DataFrame: Conteo de valores nulos por columna.
        """
        df = self.__df.isna().sum()
        df = df.to_frame()
        return df

    def normalize_column_date_file_csv(self):
        """
        Normaliza el formato de la columna 'Join_Date' a dd/mm/aaaa.

        Reemplaza guiones por barras, convierte a datetime asumiendo
        formato original mes/día/año, y reformatea a texto dd/mm/aaaa.
        Solo aplica la conversión si no había nulos originalmente y si
        la conversión no generó nulos nuevos (fechas inválidas).

        Returns:
            bool: True si la normalización fue exitosa, False si había
                nulos en la columna original o si la conversión generó
                nulos por fechas inválidas.
        """

        null_values = self.__df['Join_Date'].isna().sum()

        if null_values == 0:

            self.__df['Join_Date'] = self.__df['Join_Date'].str.replace('-', '/', regex=False)

            # Convertir a datetime indicando que el formato original es Mes/Día/Año
            # De esta forma Pandas interpretara correctamente el archivo sin generar nulos por error
            self.__df['Join_Date'] = to_datetime(self.__df['Join_Date'], format='%m/%d/%Y', errors='coerce')

            null_values = self.__df['Join_Date'].isna().sum()

        if null_values == 0:
            self.__df['Join_Date'] = self.__df['Join_Date'].dt.strftime('%d/%m/%Y')
            return True
        return False

    def normalize_column_age_file_csv(self):
        """
        Rellena los valores nulos columna 'Age' con la mediana y convierte a int.

        Returns:
            bool: True si la normalizacion fue exitoza, False si ocurre
                un error.
        """
        try:
            self.__df['Age'] = self.__df['Age'].fillna(self.__df['Age'].median())
            self.__df['Age'] = self.__df['Age'].astype(int)

            return True
        except Exception:
            return False

    def normalize_column_phone_file_csv(self):
        """
        Convierte la columna 'Phone' a str y elimina los guiones

        Returns:
            bool: True si la normalizacion fue exitosa, False si ocurre
                un error.
        """
        try:
            self.__df['Phone'] = self.__df['Phone'].astype(str)
            self.__df['Phone'] = self.__df['Phone'].str.replace('-', '')

            return True

        except Exception:
            return False

    def normalize_null_values_file_csv(self):
        """
        Elimina del DataFrame filas que contengan valores nulos.

        Returns:
            bool: True si la operacion fue exitosa, False si ocurre un error.
        """
        try:
            self.__df.dropna(inplace=True)
            return True

        except Exception:
            return False

    def data_frame_normalized_file_csv(self):
        """
        Devuelve las primera 20 filas del DataFrame normalizado.

        Returns:
            DataFrame: Primera 20 filas del DataFrame normalizado.
        """
        return self.__df.head(20)

    def save_file(self, path):
        """
        Guarda el DataFrame actual como un archivo CSV.

        Args:
            path (str): Ruta de destino donde se guardara el archivo.
        """
        self.__df.to_csv(path, index=False)
