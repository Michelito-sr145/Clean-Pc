import os
import shutil
import time
import ctypes
import sys

# Archivo para registrar errores
error_log_file = "CleanPcError.txt"

def log_error(file_path, error):
    with open(error_log_file, "a") as log:
        log.write(f"No se pudo eliminar {file_path}. Razón: {error}\n")

def clear_folder(folder_path):
    try:
        # Verifica si la carpeta existe
        if os.path.exists(folder_path):
            # Lista los archivos y carpetas en la ruta
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    # Si es un archivo, intenta eliminarlo
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        print(f"Archivo eliminado: {file_path}")
                    # Si es un directorio, intenta eliminarlo recursivamente
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"Carpeta eliminada: {file_path}")
                except Exception as e:
                    # Si ocurre un error, intenta nuevamente después de un breve periodo
                    print(f"Error al eliminar {file_path}. Reintentando...")
                    time.sleep(2)  # Espera 2 segundos antes de reintentar
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                            print(f"Archivo eliminado en el segundo intento: {file_path}")
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                            print(f"Carpeta eliminada en el segundo intento: {file_path}")
                    except Exception as e2:
                        # Si sigue fallando, registrar el error
                        print(f"No se pudo eliminar {file_path} después de varios intentos.")
                        log_error(file_path, str(e2))
        else:
            print(f"La carpeta {folder_path} no existe.")
    except Exception as e:
        log_error(folder_path, str(e))

def run_as_admin():
    # Verifica si el script se está ejecutando con permisos de administrador
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Si no es administrador, intenta relanzar el script como administrador
        try:
            # Relanza el script con permisos de administrador
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join(sys.argv), None, 1
            )
            sys.exit(0)  # Termina la primera instancia del script
        except Exception as e:
            print(f"No se pudo obtener permisos de administrador: {str(e)}")
            sys.exit(1)  # Cierra el script si no se pueden obtener los permisos

def main():
    # Llama a la función para ejecutar como administrador
    run_as_admin()
    
    # Rutas de las carpetas a limpiar
    temp_folder = os.getenv('TEMP')  # Carpeta 'Temp' del sistema
    temp_user_folder = os.getenv('TMP')  # Carpeta '%temp%' del usuario
    prefetch_folder = r'C:\Windows\Prefetch'  # Carpeta 'Prefetch'

    # Limpiar las carpetas
    print("Limpiando la carpeta Temp del sistema...")
    clear_folder(temp_folder)

    print("\nLimpiando la carpeta %temp% del usuario...")
    clear_folder(temp_user_folder)

    print("\nLimpiando la carpeta Prefetch...")
    clear_folder(prefetch_folder)

    print("\nLimpieza completada. Verifique el archivo CleanPcError.txt si hubo errores.")

if __name__ == "__main__":
    main()
