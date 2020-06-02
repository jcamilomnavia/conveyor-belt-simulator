# CONVEYOR BELT SIMULATOR

[![Generic badge](https://img.shields.io/badge/Pyhton-3.8.x-BLUE.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Proteus-8.9-PURPLE.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Arduino-1.8.12-YELLOW.svg)](https://shields.io/)

## Instalación

Para que el programa en conjunto funcione correctamente, se debe instalar un programa de Puerto Serial Virtual y lograr una comunicación exitosa, uno de estos puede ser [Virtual Serial Port Tools](https://freevirtualserialports.com/features). Revisar la configuración correspondiente.

 También se debe tener instalado el software de **Proteus** para realizar la simulación respectiva con arduino, si se desea hacer con un arduino físico, cambie la respectiva configuración.

### Dependencias de Python
Para el programa ubicado en ```banda-python``` se debe tener instalado las dependencias de **Pillow**(con este podremos manejar las imagenes de la cinta transportadora),**PySerial**(para manejar la comunicación con nuestro Arduino) y **TK & TKinter**(estos dos generaran una interfaz grafica donde veremos actuar nuestros comandos), estas últimas normalmente vienen por defecto con Python. (*Recuerda checkear la versión de python*).
```bash
pip install Pillow pyserial
```

## Configuración

Asegurese de configurar bien la conexión con el puerto serial entre python y arduino en la siguiente linea
```python
# Tendrás que elegir el puerto del arduino y la velocidad si son diferentes
# En mi caso tenia un puente virtual entre el com1-com5. 
# El arduino se configura con el COM1 y el python con el COM5
arduino = serial.Serial("COM5",9600)
```

## Instrucciones de Uso
Una vez se este corriendo el programa de Pyhton(*banda-python/banda.py*) junto con el Arduino(*en proteus*),desde el Arduino(*virtual terminal del proteus*) nos imprimirá en Serial las opciones que tenemos para manejar nuestra cinta/banda transportadora:
- B(*Begin*). Para empezar. Esta opción hara que nuestro objeto se mueva desde S1 hasta S4. Esto se realiza con el metodo left() de la clase CFG.
- S(*Stop*). Para detener el objeto en cualquier parte de la cinta. Esto se realiza con el metodo stop() de la clase CFG.
- 1 - Para ir al punto S1.  Como es el inicio de la cinta, se detendrá. Esto se realiza con el metodo right() de la clase CFG.
- 2 - Para ir al punto S2, y que se detenga. Se calcula si el objeto circle esta mas la izquierda o derecha del sensor y se moverá con el metodo left() o right()
- 3 - Para ir al punto S3, y que se detenga. Se calcula si el objeto circle esta mas la izquierda o derecha del sensor y se moverá con el metodo left() o right()
- 4 - Para ir al punto S4. Como es el fin de la cinta, se detendrá. Esto se realiza con el metodo left() de la clase CFG.


