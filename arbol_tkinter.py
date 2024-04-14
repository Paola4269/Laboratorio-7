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

# Crear el árbol
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
import tkinter as tk
import threading
import time

# Funciones para la GUI
def create_circle(x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def highlight_circle(circle, color="red", delay=0.5):
    canvas.itemconfig(circle, fill=color)
    root.update()
    time.sleep(delay)
    canvas.itemconfig(circle, fill="white")
    root.update()

def start_inorder():
    for value in inorder(raiz):
        highlight_circle(circles[value - 1], "green", 1)  # Indexamos desde 0

# Configurar la GUI
root = tk.Tk()
root.title("Árbol Binario y Circulos")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
circles = [
    create_circle(200, 50, 30, outline="#f11", fill="white", width=2),
    create_circle(100, 150, 30, outline="#f11", fill="white", width=2),
    create_circle(300, 150, 30, outline="#f11", fill="white", width=2),
    create_circle(50, 250, 30, outline="#f11", fill="white", width=2),
    create_circle(150, 250, 30, outline="#f11", fill="white", width=2)
]

# Botón para iniciar el recorrido inorder
btn_start = tk.Button(root, text="Iniciar Inorder", command=start_inorder)
btn_start.pack()

root.mainloop()
