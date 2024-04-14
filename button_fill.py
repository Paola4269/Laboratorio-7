import tkinter as tk
import serial
import threading

# Configura la conexión serial
ser = serial.Serial('COM6', 9600)  # Ajusta el puerto COM y la velocidad de baudios

def listen_to_arduino():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line == "green_pressed":
                fill_circle(circle1,"green")
            elif line =="green_released":
                fill_circle(circle1, "white")
            elif line == "red_pressed":
                fill_circle(circle2, "red")
            elif line =="red_released":
                fill_circle(circle2, "white")
            elif line == "blue_pressed":
                fill_circle(circle3, "blue")
            elif line =="blue_released":
                fill_circle(circle3, "white")

def fill_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

def create_circle(x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

root = tk.Tk()
root.title("Control de círculo con Arduino")

canvas = tk.Canvas(root, height=200, width=500)
canvas.pack()
circle1 = create_circle(100, 100, 50, outline="#f11", fill="#1f1", width=2)
circle2 = create_circle(250, 100, 50, outline="#f11", fill="#1f1", width=2)
circle3 = create_circle(400, 100, 50, outline="#f11", fill="#1f1", width=2)

# Iniciar el hilo de escucha
thread = threading.Thread(target=listen_to_arduino)
thread.daemon = True
thread.start()

root.mainloop()