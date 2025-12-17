
Gestor de Cobranzas Automático 
    Este sistema automatiza la identificación de deudores desde un archivo CSV, 
    genera facturas individuales en formato .txt y envía notificaciones automáticas por WhatsApp.

Requisitos Previos
    Debes tener instalada una versión reciente de Python.
    Requerida obligatoriamente para que pywhatkit pueda cargar WhatsApp Web y enviar los mensajes.
    Debes tener una sesión activa de WhatsApp Web en tu navegador predeterminado.
    Es fundamental instalar las librerías necesarias, se indica un requeriments.txt con esto.

Estructura del Proyecto: 
    main.py: Punto de entrada para ejecutar el programa.
    clientes.csv: Archivo de base de datos con los deudores.
    modulos/: Contiene la lógica de gestión de archivos y notificaciones.
    facturas/: Carpeta donde se generarán los comprobantes de cobro.