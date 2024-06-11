import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def saludar():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")

root = tk.Tk()
root.title("Ventana con Botón")
root.geometry("300x200")  # Tamaño de la ventana

boton = ttk.Button(root, text="Pug", command=saludar)
boton.place(x=50, y=50)  # Posición del botón

root.mainloop()
