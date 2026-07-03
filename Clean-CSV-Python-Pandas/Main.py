from os import name, system
from time import sleep

from rich.console import Console, Group
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.rule import Rule
from rich.text import Text

from LoadFile import LoadFile
from CleanCSV import CleanCSV


class Main:

    @staticmethod
    def main():

        # Limpio la consola
        if name == 'posix':
            system('clear')
        elif name == 'nt' or name == 'ce' or name == 'dos':
            system('cls')


        console = Console()
        progress = Progress(SpinnerColumn(),TextColumn("[bold cyan]{task.description}"))

        try:
            # Cargar archivo CSV para analizar
            file = LoadFile()


            process = CleanCSV(file.open_choose_file())
            process.load_file()

            # Variable que almacena los valores que seran renderizado por consola.
            items = []


            with (Live(auto_refresh=True, console=console) as live):

                task = progress.add_task("Obteniendo Datos...", total=None)
                live.update(Group(*items, progress))
                live.refresh()
                sleep(4)

                # Muestro las 10 primeras filas del DataFrame
                progress.update(task, description="Obteniendo los 10 primeros registros...")
                sleep(4)
                items.append(Text("Primeros 10 registros del archivo", style="#EEF527"))
                items.append(Rule())
                table_head = Table()
                df = process.show_head_file_csv()

                for cols in df.columns:
                    table_head.add_column(cols)

                for rows in df.itertuples(index=False):
                    table_head.add_row(*map(str, rows))

                items.append(table_head)

                live.update(Group(*items, progress))

                # Muestro las 10 ultimas filas del DataFrame
                progress.update(task, description="Obteniendo los ultimos 10 registros...")
                sleep(4)

                items.append(Text("Ultimos 10 registros del archivo", style="#EEF527"))
                items.append(Rule())
                table_tail = Table()
                df = process.show_tail_file_csv()

                for cols in df.columns:
                    table_tail.add_column(cols)

                for rows in df.itertuples(index=False):
                    table_tail.add_row(*map(str, rows))

                items.append(table_tail)

                live.update(Group(*items, progress))

                # Muestro informacion del DataFrame actual (Columns, Dtype, non-null Count)
                progress.update(task, description="Obteniendo informacion de los datos...")
                sleep(4)

                items.append(Text("Tipos de datos", style="#EEF527"))
                items.append(Rule())

                df = process.show_info_file_cvs()
                table_info = Table()
                for col in df.columns:
                    table_info.add_column(col)

                for rows in df.itertuples(index=False):
                    table_info.add_row(*map(str, rows))

                items.append(table_info)

                live.update(Group(*items, progress))

                # Muestro el conteo de los valores nulos por columnas

                progress.update(task, description="Obteniendo informacion de valores nulo...")
                sleep(4)

                items.append(Text("Analisis de valores nulos", style="#EEF527"))
                items.append(Rule())

                df = process.show_null_files_csv()

                table_null_values = Table()
                table_null_values.add_column("Columns")
                table_null_values.add_column("Null Values")

                for index, value in df[0].items():
                    table_null_values.add_row(str(index), str(value))

                items.append(table_null_values)

                live.update(Group(*items, progress))

                # Comienzo a nomalizar datos en el DataFrame y se muestran por consola
                progress.update(task, description="Normalizando Datos")


                df = process.normalize_column_date_file_csv()
                if df:
                    items.append(Text("\u2705 Columna Join_Date normalizada", style="#27F527"))
                    live.update(Group(*items, progress))

                df = process.normalize_column_age_file_csv()

                if df:
                    items.append(Text("\u2705 Columna Age normalizada", style="#27F527"))
                    live.update(Group(*items, progress))
                else:
                    items.append(Text("\u274c Error al normalizar Columna Age", style="#F50505"))
                    live.update(Group(*items, progress))


                if process.normalize_column_phone_file_csv():
                    items.append(Text("\u2705 Columna Phone normalizada", style="#27F527"))
                    live.update(Group(*items, progress))
                else:
                    items.append(Text("\u274c Error al normalizar Columna Phone", style="#F50505"))
                    live.update(Group(*items, progress))


                if process.normalize_null_values_file_csv():
                    items.append(Text("\u2705 Valores nulos normalizados", style="#27F527"))
                    live.update(Group(*items, progress))
                else:
                    items.append(Text("\u274c Error al normalizar valores nulos", style="#F50505"))
                    live.update(Group(*items, progress))

                # Mostrando informacion dataframe nomalizada
                df = process.show_info_file_cvs()
                table_info = Table()
                for col in df.columns:
                    table_info.add_column(col)

                for rows in df.itertuples(index=False):
                    table_info.add_row(*map(str, rows))

                items.append(Text("Informacion datos normalizados", style="#EEF527"))
                items.append(Rule())
                items.append(table_info)

                live.update(Group(*items, progress))

                # Mostrar Dataframe normalizado

                items.append(Text("Datos Normalizados", style="#EEF527"))
                items.append(Rule())

                df = process.data_frame_normalized_file_csv()

                table_normalized = Table()

                for col in df.columns:
                    table_normalized.add_column(col)

                for row in df.itertuples(index=False):
                    table_normalized.add_row(*map(str, row))

                items.append(table_normalized)
                live.update(Group(*items, progress))

                progress.update(task, description="Proceso finalizado")
            # Guardamos el archivo
            process.save_file(file.save_file())
        except FileNotFoundError:
            console.print("[bold red][X] Archivo no encontrado")

        except Exception as e:
            console.print(f"[bold red][X] {e}")


if __name__ == "__main__":
    Main.main()