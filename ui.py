import tkinter as tk 

ventana=tk.Tk()
ventana.title= ("Hamburgueseria IT")
ventana.config(width=500, height=500)

#titulo
# Definir el título centrado
titulo = tk.Label(ventana, text="------ Pedidos -------")
titulo.place(relx=0.5, rely=0.15, anchor="center")

#engargado
encargado_label = tk.Label(ventana, text="Nombre de Encargado:", justify="left")
encargado_label.place(relx=0.3, rely=0.3,anchor="center")

encargado_entry = tk.Entry(ventana)
encargado_entry.place(relx=0.8, rely=0.3, anchor="center")

#Combo s
combos_label = tk.Label(ventana, text="Combo S cantidad: ", justify="left")
combos_label.place(relx=0.3, rely=0.4, anchor="center")

combos_label_entry= tk.Entry(ventana)
combos_label_entry.place(relx=0.8, rely=0.4, anchor="center")

#Combo d
combod_label = tk.Label(ventana, text="Combo D cantidad: ", justify="left")
combod_label.place(relx=0.3, rely=0.5, anchor="center")

combod_label_entry= tk.Entry(ventana)
combod_label_entry.place(relx=0.8, rely=0.5, anchor="center")

#Combo t
combot_label = tk.Label(ventana, text="Combo T cantidad: ", justify="left")
combot_label.place(relx=0.3, rely=0.6, anchor="center")

combot_label_entry= tk.Entry(ventana)
combot_label_entry.place(relx=0.8, rely=0.6, anchor="center")

#Combo postre
postre_label = tk.Label(ventana, text="Combo Postre cantidad: ",justify="left")
postre_label.place(relx=0.3, rely=0.7, anchor="center")

postre_label_label_entry= tk.Entry(ventana)
postre_label_label_entry.place(relx=0.8, rely=0.7, anchor="center")

#Combo Cliente
cliente_label = tk.Label(ventana, text="Combo Nombre del Cliente: ",justify="left")
cliente_label.place(relx=0.3, rely=0.8, anchor="center")

cliente_label_entry= tk.Entry(ventana)
cliente_label_entry.place(relx=0.8, rely=0.8, anchor="center")

#botones
salir_boton= tk.Button(ventana, text="Salir Seguro")
salir_boton.place(relx=0.2, rely=0.95, anchor="center", width=130, height=40)

Cancelar_pedido_boton= tk.Button(ventana, text="Cancelar Pedido")
Cancelar_pedido_boton.place(relx=0.5, rely=0.95, anchor="center", width=130, height=40)

Hacer_pedido_boton= tk.Button(ventana, text="Hacer Pedido")
Hacer_pedido_boton.place(relx=0.8, rely=0.95, anchor="center", width=130, height=40)



ventana.mainloop()
    

