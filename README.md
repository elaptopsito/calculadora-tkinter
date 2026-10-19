# Calculadora con tkinter

Calculadora de escritorio hecha en Python con la librería estándar `tkinter`.

## Características

- Operaciones básicas: suma, resta, multiplicación y división
- Botón `Borrar` para eliminar el último carácter
- Botón `C` para limpiar la pantalla
- Control de operadores consecutivos y de decimales repetidos
- La pantalla y los botones escalan al cambiar el tamaño de la ventana
- Pantalla completa con `F11` y salida con `Escape`

## Descargar el ejecutable

Para Windows no necesitas tener Python instalado. Descarga `calculadora.exe` desde la sección [Releases](https://github.com/elaptopsito/calculadora-tkinter/releases) y ábrelo con doble clic.

## Ejecutar desde el código fuente

Requisitos: Python 3.10 o superior.

```bash
git clone https://github.com/elaptopsito/calculadora-tkinter.git
cd calculadora-tkinter
python calculadora.py
```

`tkinter` viene incluido con Python, así que no hace falta instalar nada más.

## Estructura

```
calculadora.py   # código principal
icono.ico        # icono de la ventana y del ejecutable
```

## Generar el ejecutable

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --icon=icono.ico --add-data "icono.ico;." calculadora.py
```

El resultado queda en `dist/calculadora.exe`.

## Aviso de seguridad

Windows Defender o SmartScreen pueden advertir sobre el ejecutable porque no tiene firma digital. Es un falso positivo común en programas generados con PyInstaller.

## Autor

elaptopsito
