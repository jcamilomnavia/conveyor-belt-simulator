# CONVEYOR BELT SIMULATOR

[![Generic badge](https://img.shields.io/badge/Pyhton-3.8.x-BLUE.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Proteus-8.9-PURPLE.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Arduino-1.8.12-YELLOW.svg)](https://shields.io/)

## Instalación

Para que el programa en conjunto funcione correctamente, se deben instalar un programa de Puerto Serial Virtual y lograr una comunicación exitosa, uno de estos puede ser [Virtual Serial Port Tools](https://freevirtualserialports.com/features). Revisar la configuración correspondiente. También se debe tener instalado el software de Proteus para realizar la simulacion respectiva con arduino, si se desea hacer con un arduino físico, cambie la respectiva configuración.

### Dependencias de Python
Para el programa ubicado en ```banda-python``` se debe tener instalado las dependencias de **Pillow**,**PySerial** y **TK & TKinter**, esta ultima normalmente viene por defecto con Python. Recuerda checkear la versión de python.
```bash
pip install Pillow pyserial
```

## Configuración

Asegurese de configurar bien la conexión con el puerto serial entre python y arduino en la siguiente linea
```python
# Tendrás que elegir el puerto del arduino y la velocidad si son diferentes
arduino = serial.Serial("COM5",9600)
```

## Instrucciones de Uso
Una vez se este corriendo el programa de Pyhton junto con el Arduino, desde el Arduino nos imprimirá en Serial las opciones que tenemos para manejar nuestra cinta/banda transportadora:
- B(*Begin*). Para empezar. Esta opción hara que nuestro objeto se mueva desde S1 hasta S4.
- S(*Stop*). Para detener el objeto en cualquier parte de la cinta.
- 1 - Para ir al punto S1.  Como es el inicio de la cinta, se detendrá
- 2 - Para ir al punto S2, y que se detenga. 
- 3 - Para ir al punto S3, y que se detenga.
- 4 - Para ir al punto S4. Como es el fin de la cinta, se detendrá.


