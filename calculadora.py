import tkinter as tk
from tkinter import font as tkfont
import sys
import os

def ruta_recurso(nombre):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, nombre)

ANCHO_BASE = 400
ALTO_BASE = 500 

def ajustar_fuentes(event=None):
    escala = min(ventana.winfo_width() / ANCHO_BASE,
                 ventana.winfo_height() / ALTO_BASE)
    fuente_pantalla.configure(size=max(12, int(48 * escala)))
    fuente_botones.configure(size=max(8, int(24 * escala)))


OPERADORES = "+-*/"

def al_presionar(valor):
    actual = pantalla.get()

    if valor and (actual == "Error de sintaxis" or actual == "No se pueden dividir números por 0"):
        if valor == "C":
            pantalla.set("")
        else:
            pass
    elif valor == ".":
        numero_actual = actual
        for op in OPERADORES:
            numero_actual = numero_actual.split(op)[-1]

        if "." in numero_actual:
            return
        elif actual == "":
            pass
        elif actual[-1] in OPERADORES:
            pass
        elif actual[-1] not in OPERADORES:
            pantalla.set(actual + ".")
        
    elif valor == "C":
        pantalla.set("")
    elif valor == "Borrar":
        if actual == "Error de sintaxis" or actual == "No se pueden dividir números por 0":
            pass
        else:
            pantalla.set(actual[:-1])
    elif valor == "=":
        try:
            resultado = eval(actual)
            pantalla.set(str(resultado))
        except ZeroDivisionError:
            pantalla.set("No se pueden dividir números por 0")
        except (NameError, SyntaxError):
            pantalla.set("Error de sintaxis")
    

    elif valor in OPERADORES:
        if actual == "":
            return
        elif actual[-1] in OPERADORES:
            pass
        else:
            pantalla.set(actual + valor)
    else:
        pantalla.set(actual + valor)

ventana = tk.Tk()
ventana.iconbitmap(ruta_recurso("icono.ico"))
fuente_pantalla = tkfont.Font(family="Arial", size=24)
fuente_botones = tkfont.Font(family="Arial", size=16)
ventana.title("Calculadora")
ventana.geometry(f"{ANCHO_BASE}x{ALTO_BASE}")
ventana.minsize(250, 350)

pantalla = tk.StringVar()

entrada = tk.Entry(
    ventana,
    textvariable=pantalla,
    font=("Arial", 20),
    justify="right",
    bd=5
)

entrada.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

botones = [
    ("7",      1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("/", 1, 3, 1), ("Borrar", 1, 4, 1),
    ("4",      2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("*", 2, 3, 1), ("C",      2, 4, 1),
    ("1",      3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("-", 3, 3, 1), ("+",      3, 4, 1),
    ("0",      4, 0, 2), (".", 4, 2, 1), ("=", 4, 3, 2),
]

for texto, fila, col, span in botones:
    boton = tk.Button(
    ventana,
    text=texto,
    font=("Arial", 16),
    command=lambda valor=texto: al_presionar(valor)
    )
    boton.grid(row=fila, column=col, columnspan=span, sticky="nsew", padx=3, pady=3)

for i in range(5):
    ventana.columnconfigure(i, weight=1)
for i in range(5):
    ventana.rowconfigure(i, weight=1)

def alternar_fullscreen(event=None):
    activo = ventana.attributes("-fullscreen")
    ventana.attributes("-fullscreen", not activo)

def salir_fullscreen(event=None):
    ventana.attributes("-fullscreen", False)

ventana.bind("<Configure>", ajustar_fuentes)
ventana.bind("<F11>", alternar_fullscreen)
ventana.bind("<Escape>", salir_fullscreen)

ventana.mainloop()

