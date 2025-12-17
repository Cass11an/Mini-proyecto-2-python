import pywhatkit

def notificaciones(deudores):
    try:
        for i in range(len(deudores)):
            numero = '+' + deudores[i]['Telefono']
            pywhatkit.sendwhatmsg_instantly(numero, f'Hola {deudores[i]['Nombre']}, tu factura ya fue generada. Debes: {deudores[i]['MontoDeuda']}.')

        print(f'Se han enviado {i} mensajes de notificacion')
    except Exception as e:
        return ('No fue posible enviar las notificaciones. Intente nuevamente mas tarde')

