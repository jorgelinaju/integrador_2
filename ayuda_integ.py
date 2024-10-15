import tkinter as tk
import sqlite3
from time import asctime
from tkinter import messagebox

# Conectar con la base de datos
conexion = sqlite3.connect("comercio.sqlite")
caja = 0

# Función para insertar ventas en la base de datos
def insertar_ventas_db(venta):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS venta (
                id INTEGER PRIMARY KEY, 
                cliente TEXT, 
                fecha TEXT, 
                Combo_s INTEGER, 
                Combo_D INTEGER, 
                Combo_T INTEGER, 
                cant_flurby INTEGER, 
                total REAL
            )
        """)
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR: {e}")
    try:
        cursor.execute("""
            INSERT INTO venta 
            (cliente, fecha, Combo_s, Combo_D, Combo_T, cant_flurby, total) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            venta["cliente"], 
            venta["fecha"], 
            venta["combo_s"], 
            venta["combo_D"], 
            venta["combo_T"], 
            venta["cant_flurby"], 
            venta["total"]
        ))
        conexion.commit()
        print("Venta confirmada")
    except sqlite3.OperationalError as e:
        print(f"ERROR: {e}")

# Función para insertar registro de encargados en la base de datos
def insertar_registro_db(encargado, evento):
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registro (
                id INTEGER PRIMARY KEY, 
                encargado TEXT, 
                fecha TEXT, 
                evento TEXT, 
                caja REAL
            )
        """)
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR: {e}")
    try:
        cursor.execute("""
            INSERT INTO registro (encargado, fecha, evento, caja) 
            VALUES (?, ?, ?, ?)
        """, (encargado, asctime(), evento, caja))
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR: {e}")

# Función para realizar un nuevo pedido
def hacer_pedido():
    global caja
    nombre_cliente = cliente_label_entry.get()
    encargado = encargado_entry.get()

    try:
        cant_combo_s = int(combos_label_entry.get())
        cant_combo_d = int(combod_label_entry.get())
        cant_combo_t = int(combot_label_entry.get())
        cant_flurby = int(postre_label_label_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        return

    if not nombre_cliente or not encargado:
        messagebox.showerror("Error", "El nombre del cliente y el encargado son obligatorios.")
        return

    # Precios de los combos
    precio_s, precio_d, precio_t, precio_flurby = 5, 6, 7, 2
    precio_total = (cant_combo_s * precio_s) + (cant_combo_d * precio_d) + (cant_combo_t * precio_t) + (cant_flurby * precio_flurby)

    # Guardar el pedido en la base de datos
    venta = {
        "cliente": nombre_cliente,
        "fecha": asctime(),
        "combo_s": cant_combo_s,
        "combo_D": cant_combo_d,
        "combo_T": cant_combo_t,
        "cant_flurby": cant_flurby,
        "total": precio_total,
    }
    insertar_ventas_db(venta)
    caja += precio_total
    messagebox.showinfo("Confirmación", f"Pedido confirmado\nTotal: ${precio_total}")

# Función para cancelar el pedido (limpiar campos excepto el encargado)
def cancelar_pedido():
    combos_label_entry.delete(0, tk.END)
    combod_label_entry.delete(0, tk.END)
    combot_label_entry.delete(0, tk.END)
    postre_label_label_entry.delete(0, tk.END)
    cliente_label_entry.delete(0, tk.END)

# Función para salir del sistema y guardar los datos del encargado
def salir_seguro():
    encargado = encargado_entry.get()
    if encargado:
        insertar_registro_db(encargado, "OUT")
        conexion.close()
        ventana.quit()
    else:
        messagebox.showerror("Error", "No hay encargado registrado para guardar el turno.")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title = "Hamburguesería IT"
ventana.config(width=500, height=500)

# Título
titulo = tk.Label(ventana, text="------ Pedidos -------")
titulo.place(relx=0.5, rely=0.15, anchor="center")

# Encargado
encargado_label = tk.Label(ventana, text="Nombre de Encargado:", justify="left")
encargado_label.place(relx=0.3, rely=0.3, anchor="center")
encargado_entry = tk.Entry(ventana)
encargado_entry.place(relx=0.8, rely=0.3, anchor="center")

# Combo S
combos_label = tk.Label(ventana, text="Combo S cantidad: ", justify="left")
combos_label.place(relx=0.3, rely=0.4, anchor="center")
combos_label_entry = tk.Entry(ventana)
combos_label_entry.place(relx=0.8, rely=0.4, anchor="center")

# Combo D
combod_label = tk.Label(ventana, text="Combo D cantidad: ", justify="left")
combod_label.place(relx=0.3, rely=0.5, anchor="center")
combod_label_entry = tk.Entry(ventana)
combod_label_entry.place(relx=0.8, rely=0.5, anchor="center")

# Combo T
combot_label = tk.Label(ventana, text="Combo T cantidad: ", justify="left")
combot_label.place(relx=0.3, rely=0.6, anchor="center")
combot_label_entry = tk.Entry(ventana)
combot_label_entry.place(relx=0.8, rely=0.6, anchor="center")

# Combo Postre
postre_label = tk.Label(ventana, text="Combo Postre cantidad: ", justify="left")
postre_label.place(relx=0.3, rely=0.7, anchor="center")
postre_label_label_entry = tk.Entry(ventana)
postre_label_label_entry.place(relx=0.8, rely=0.7, anchor="center")

# Cliente
cliente_label = tk.Label(ventana, text="Nombre del Cliente: ", justify="left")
cliente_label.place(relx=0.3, rely=0.8, anchor="center")
cliente_label_entry = tk.Entry(ventana)
cliente_label_entry.place(relx=0.8, rely=0.8, anchor="center")

# Botones
salir_boton = tk.Button(ventana, text="Salir Seguro", command=salir_seguro)
salir_boton.place(relx=0.2, rely=0.95, anchor="center", width=130, height=40)

cancelar_pedido_boton = tk.Button(ventana, text="Cancelar Pedido", command=cancelar_pedido)
cancelar_pedido_boton.place(relx=0.5, rely=0.95, anchor="center", width=130, height=40)

hacer_pedido_boton = tk.Button(ventana, text="Hacer Pedido", command=hacer_pedido)
hacer_pedido_boton.place(relx=0.8, rely=0.95, anchor="center", width=130, height=40)

ventana.mainloop()
