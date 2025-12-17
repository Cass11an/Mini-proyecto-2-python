from modulos import gestor_archivos as gest
from modulos import notificaciones as noti

deudores = []

try:
    deudores = gest.abrirArchivo()
    if deudores: #en caso de que hayan deudores
        gest.archivoFacturas(deudores)
        noti.notificaciones(deudores)
        
        print("Se han generado las facturas. Los mensajes han sido enviados")
    else: #en caso de que todos esten al dia
        print("No hay deudores para procesar.")

except ValueError:
    print("Los montos y las fechas en el CSV deben estar expresados en el formato correcto.")

except Exception as e:
    
    print(f"Ocurrió un error {e}. Intente de nuevo mas tarde")
