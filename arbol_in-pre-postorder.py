import tkinter as tk
from tkinter import messagebox
import serial
import threading
import time

try:
    ser = serial.Serial('COM6', 9600)
except serial.SerialException as e:
    messagebox.showerror("Error de conexión serial", f"No se pudo abrir el puerdo serial: {e}")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def inorder(nodo):
    if nodo:
        yield from inorder(nodo.izquierda)
        yield nodo.valor
        yield from inorder(nodo.derecha)

def preorder(nodo):
    if nodo:
        yield nodo.valor
        yield from preorder(nodo.izquierda)
        yield from preorder(nodo.derecha)

def postorder(nodo):
    if nodo:
        yield from postorder(nodo.izquierda)
        yield from postorder(nodo.derecha)
        yield nodo.valor

raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

def listen_to_arduino():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line == "green_pressed":
                root.event_generate("<<GreenPressed>>", when="tail")
            elif line == "red_pressed":
                root.event_generate("<<RedPressed>>", when="tail")
            elif line == "blue_pressed":
                root.event_generate("<<BluePressed>>", when="tail")

def on_green_pressed(event):
    start_inorder()

def on_red_pressed(event):
    start_preorder()

def on_blue_pressed(event):
    start_postorder()

def highlight_circle(circle, color="red", delay=0.5):
    canvas.itemconfig(circle, fill=color)
    root.update_idletasks()
    time.sleep(delay)
    canvas.itemconfig(circle, fill="white")
    root.update_idletasks()

def start_inorder():
    for value in inorder(raiz):
        highlight_circle(circles[value - 1], "green", 1)  # Indexamos desde 0

def start_preorder():
    for value in preorder(raiz):
        highlight_circle(circles[value - 1], "red", 1)

def start_postorder():
    for value in postorder(raiz):
        highlight_circle(circles[value - 1], "blue", 1)

def create_circle(x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def on_closing():
    if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
        ser.close()
        root.destroy()

root = tk.Tk()
root.title("Árbol binario con pushbuttons")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
circles = [
    create_circle(200, 50, 30, outline="#f11", fill="white", width=2),
    create_circle(100, 150, 30, outline="#f11", fill="white", width=2),
    create_circle(300, 150, 30, outline="#f11", fill="white", width=2),
    create_circle(50, 250, 30, outline="#f11", fill="white", width=2),
    create_circle(150, 250, 30, outline="#f11", fill="white", width=2)
]

root.bind("<<GreenPressed>>", on_green_pressed)
root.bind("<<RedPressed>>", on_red_pressed)
root.bind("<<BluePressed>>", on_blue_pressed)

arduino_thread = threading.Thread(target=listen_to_arduino, daemon=True)
arduino_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
