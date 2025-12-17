import csv
from datetime import datetime
import os

fecha = datetime.now()
fechaActual = fecha.strftime('%d/%m/%Y')

def abrirArchivo():
    deudores = []
    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionCSV = os.path.join(ubicacionActual, "..", "clientes.csv")

    try:
        with open(ubicacionCSV, "r") as file:
            archivo = csv.DictReader(file, delimiter= ',')
            for row in archivo:
                fechaVencimiento = datetime.strptime(row['FechaVencim'],'%d/%m/%Y')
                if fechaVencimiento < fecha:
                    deudores.append(row)
            
            print(f'Los clientes con pago pendientes son: {deudores}')
            return deudores
    except FileNotFoundError:
        print('No se ha encontrado el archivo de clientes')
        return []


def archivoFacturas(deudores):
    ubicacionActual = os.path.dirname(os.path.abspath(__file__))
    ubicacionFacturas = os.path.join(ubicacionActual, "..", "facturas")

    if not os.path.exists(ubicacionFacturas):
            os.makedirs(ubicacionFacturas)

    try: 
        for i in range(len(deudores)):

            nombreArchivo = 'factura ' + deudores[i]['Nombre'] + '.txt'
            ubicacion = os.path.join(ubicacionFacturas, nombreArchivo)

            contenido = f"""
                *************************************************
                *           AVISO DE COBRO PENDIENTE            *
                *************************************************

                [FECHA DE GENERACION: {fechaActual}]

                --- DATOS DEL CLIENTE ---
                NOMBRE: {deudores[i]['Nombre']}
                TELEFONO DE CONTACTO: {deudores[i]['Telefono']}

                --- DETALLES DE LA DEUDA ---
                MONTO PENDIENTE:    {float(deudores[i]['MontoDeuda'])} Bs
                FECHA DE VENCIMIENTO: {deudores[i]['FechaVencim']}

                Por favor, complete el pago antes de la fecha de 
                vencimiento para evitar la interrupcion del servicio.
                ************************************************* """

            document = open(f"{ubicacion}", "w")
            document.write(contenido)
            document.close()
        return print(f'Se ha generado la factura de los clientes con deuda')
            
    except FileNotFoundError:
        return("El archivo no fue encontrado.")
    
