import tkinter as tk
from tkinter import ttk
import serial
import threading
import time

PUERTO = "COM5"
BAUDIOS = 9600

try:
    ser = serial.Serial(PUERTO, BAUDIOS)
    print(f"[✓] Conectado al puerto {PUERTO}")
except Exception as e:
    print(f"[X] Error al conectar: {e}")
    ser = None

# Obtener datos de la GUI
def obtener_datos():
    comp_estado = [str(var.get()) for var in computadoras_vars]  # 10 valores: '1' o '0'
    comp_cadena = ",".join(comp_estado)

    datos = [
        "Detectado" if var_sonico.get() else "No Detectado",
        "Oscuro" if var_luz.get() else "Claro",
        entry_temp.get(),
        entry_hum.get(),
        "ON" if var_lampara.get() else "OFF",
        comp_cadena,
        "Activo" if var_buzzer.get() else "Inactivo",
        entry_rfid.get()
    ]
    return ",".join(datos)

# Envío automático cada 10 segundos
def enviar_periodicamente():
    while True:
        if ser:
            datos = obtener_datos()
            print(f"[→] Enviado: {datos}")
            ser.write((datos + '\n').encode('utf-8'))
        time.sleep(10)

# Interfaz gráfica
root = tk.Tk()
root.title("Emulador Arduino - PLC")

# Sensor Sónico (checkbox)
var_sonico = tk.BooleanVar()
tk.Checkbutton(root, text="Sensor Sónico Detectado", variable=var_sonico).grid(row=0, columnspan=2, sticky="w")

# Sensor de Luz (checkbox)
var_luz = tk.BooleanVar()
tk.Checkbutton(root, text="Oscuridad detectada", variable=var_luz).grid(row=1, columnspan=2, sticky="w")

# Temperatura
tk.Label(root, text="Temperatura (°C):").grid(row=2, column=0)
entry_temp = tk.Entry(root)
entry_temp.grid(row=2, column=1)

# Humedad
tk.Label(root, text="Humedad (%):").grid(row=3, column=0)
entry_hum = tk.Entry(root)
entry_hum.grid(row=3, column=1)

# Lámpara
var_lampara = tk.BooleanVar()
tk.Checkbutton(root, text="Lámpara encendida", variable=var_lampara).grid(row=4, columnspan=2, sticky="w")

# Computadoras RGB (10 checkboxes)
tk.Label(root, text="Computadoras RGB (10):").grid(row=5, column=0, sticky="w")
computadoras_vars = []
for i in range(10):
    var = tk.IntVar()
    cb = tk.Checkbutton(root, text=f"PC{i+1}", variable=var)
    cb.grid(row=6 + i // 5, column=i % 5)
    computadoras_vars.append(var)

# Buzzer
var_buzzer = tk.BooleanVar()
tk.Checkbutton(root, text="Buzzer activo", variable=var_buzzer).grid(row=8, columnspan=2, sticky="w")

# RFID
tk.Label(root, text="ID RFID:").grid(row=9, column=0)
entry_rfid = tk.Entry(root)
entry_rfid.grid(row=9, column=1)

# Hilo de envío
threading.Thread(target=enviar_periodicamente, daemon=True).start()

root.mainloop()

