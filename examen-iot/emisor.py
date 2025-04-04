import tkinter as tk
import serial

# Configurar puerto serial (COM5 a 9600 baud)
ser = serial.Serial('COM5', 9600)  # Abrir COM5. Reemplaza 'COM5' por el puerto que uses.

def enviar_dato(valor):
    """Envía el valor dado por el puerto serial."""
    # Convertir el valor a bytes y enviar
    ser.write(valor.encode('utf-8'))
    print(f"Dato '{valor}' enviado por serial")  # (Opcional: mensaje en la consola de Python)

# Crear ventana principal
root = tk.Tk()
root.title("Emisor Serial")

# Crear botones y asignar comandos
boton1 = tk.Button(root, text="Enviar 1", command=lambda: enviar_dato("1"))
boton1.pack(padx=10, pady=5)

boton2 = tk.Button(root, text="Enviar 2", command=lambda: enviar_dato("2"))
boton2.pack(padx=10, pady=5)

botonA = tk.Button(root, text="Enviar A", command=lambda: enviar_dato("A"))
botonA.pack(padx=10, pady=5)

# Iniciar bucle principal de la interfaz
root.mainloop()