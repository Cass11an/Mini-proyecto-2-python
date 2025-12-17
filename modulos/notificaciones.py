import pywhatkit
import time

def notificaciones(deudores):
    try:
        for i in range(len(deudores)):
            numero = '+' + deudores[i]['Telefono']
            mensaje = f'Hola {deudores[i]['Nombre']}, tu factura ya fue generada. Debes: {deudores[i]['MontoDeuda']}.'
            pywhatkit.sendwhatmsg_instantly(numero, mensaje, wait_time=20, tab_close=True)

        print(f'Se han enviado los mensajes de notificacion')
    except Exception as e:
        return ('No fue posible enviar las notificaciones. Intente nuevamente mas tarde')

