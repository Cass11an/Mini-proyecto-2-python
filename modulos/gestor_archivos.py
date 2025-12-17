import csv
from datetime import datetime

fecha = datetime.now()
fechaActual = fecha.strftime('%d/%m/%Y')

def abrirArchivo():
    deudores = []
    try:
        with open("proyectos\mini proyecto 2\clientes.csv", "r") as file:
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
    try: 
        for i in range(len(deudores)):

            ubicacion = "proyectos\\mini proyecto 2\\facturas\\" 
            nombreArchivo = 'factura ' + deudores[i]['Nombre'] + '.txt'

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

            document = open(f"{ubicacion}{nombreArchivo}", "w")
            document.write(contenido)
            document.close()
        return print(f'Se ha generado la factura de los clientes con deuda')
            
    except FileNotFoundError:
        return("El archivo no fue encontrado.")
    
