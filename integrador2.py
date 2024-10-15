import sqlite3 
from time import asctime



#funcion para ingregar encargado
def ingreso_encargado():
        
    mensaje_bienvenida="Buenvenida \n Ingrese su nombre de encargado: "
    nombre=input(mensaje_bienvenida)
    
    while not nombre.strip():
        print("El nombre esta vacio")
        nombre=input(mensaje_bienvenida)
    return nombre.title()

#funcion para insertar la venta de la base de datos
def insertar_ventas_db(venta):
    cursor=conexion.cursor()
    try:
        cursor.execute("create table if not exists venta (id INTEGER PRIMARY KEY, cliente TEXT, fecha TEXT, Combo_s INTEGER, Combo_D INTEGER, Combo_T INTEGER, cant_flurby INTEGER, total REAL)")
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR.{e}")
    try:
        cursor.execute(
            f"INSERT INTO venta (cliente, fecha,Combo_s,Combo_D, Combo_T, cant_flurby, total) VALUES (?,?,?,?,?,?,?)",(
                       venta["cliente"],
                       venta["fecha"],
                       venta["combo_s"],
                       venta["combo_D"],
                       venta["combo_T"],
                       venta["cant_flurby"],
                       venta["total"]))
    
        conexion.commit()
        print("venta confirmada")
    except sqlite3.OperationalError as e:
        print(f"ERROR.{e}")
    

#funcion que inserta el registro de turnos de encargados
def Insertar_registro_db(encargado, evento): 
    cursor=conexion.cursor()
    try:
        cursor.execute("create table if not exists registro (id INTEGER PRIMARY KEY, encargado TEXT, fecha TEXT, evento TEXT, caja REAL)")
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR.{e}")
    try:
        cursor.execute(
            f"INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?,?,?,?)",
            (encargado,asctime(),evento,caja)
            )
    
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR.{e}")
    
#funcion para hacer un pedido
def nuevo_pedido():
    #valor de cada combo
    precio_s, precio_D, precio_T, precio_flurby=5,6,7,2
    
    #ingreso nombre cliente
    nombre_clente=input("Ingrese nombre del cliente: ")
    while not nombre_clente.strip():
        print("El nombre del cliente esta vacio")
        nombre_clente=input("Ingrese nombre del cliente: ")
    
    while True:
        cant_combo_s=input("Ingresar cantidad de combro S: ")
        try:
            #combo simple
            cant_combo_s=int(cant_combo_s)
            break
        except ValueError:
            print("La cantidad debe ser un número")

            
    #combo doble
    
    while True:
        cant_combo_D=input("Ingresar cantidad de combos D: ")
        try:
            cant_combo_D=int(cant_combo_D)
            break
        except ValueError:
            print("La cantidad debe ser un número")
            
    #combo triple
   
    while True:
        cant_combo_T=input("Ingresar cantidad de combos T: ")
        try:
            cant_combo_T=int(cant_combo_T)
            break
        except ValueError:
            print("La cantidad debe ser un número")
            
    #helado
    while True:
        cant_flurby=input("Ingresar cantidad de combos flurby: ")
        try:
            cant_flurby=int(cant_flurby)
            break
        except ValueError:
            print("La cantidad debe ser un número")
    
    #precio total        
    precio_total=(cant_combo_s*precio_s)+(cant_combo_D*precio_D)+(cant_combo_T*precio_T)+(cant_flurby*precio_flurby)
    print(f"total ${precio_total}") 
    
    #ingreso de pago del cliente
    while True:
        pago=input("Abono con $ ") 
        try:
            pago=float(pago)
            if pago<precio_total:
                print("pago insuficientes")
                continue
            break
        except ValueError:
            print("El pago debe ser un número")
    
    #calcular vuelto 
    vuelto=pago-precio_total 
    print(f"vuelto ${round(vuelto,2)}")
    
    #confirmar pedido
    while True:
        confirmacion=input("Confirma pedido? (y/n): ")
        if confirmacion.lower()=='y':
            venta={
                "cliente":nombre_clente,
                "fecha": asctime(),
                "combo_s": cant_combo_s, 
                "combo_D": cant_combo_D,
                "combo_T": cant_combo_T,
                "cant_flurby": cant_flurby,
                "total": precio_total,
                
            }
            insertar_ventas_db(venta)
            global caja
            caja +=precio_total
        
            print("Pedido confirmado")
            break
        elif confirmacion.lower()=='n':
            print("Pedido cancelado")
            break
        else:
            print("Respuesta no válida")
    
        
 #funcion principal  
 #conectar con la db
global conexion
conexion = sqlite3.connect("comercio.sqlite")

#variables globales
caja=0

      
nombre =ingreso_encargado() 
insertar_ventas_db(nombre, "IN")
       
while True:
    menu= f"Hamburquesas IT\nEncargad@ -> {nombre}\nRecuerda, siempre hay que recibir al cliente con una sonrisa :)\n1 – Ingreso nuevo pedido\n2 – Cambio de turno\n3 – Apagar sistema \n"
    opcion_selecionada = input(menu)
    match opcion_selecionada:
        #ingresar nuevo pedido funcion aparte
        case '1':
            nuevo_pedido()
        #cambio de turno
        case '2':
            insertar_ventas_db(nombre,"out")
            caja=0
            nombre =ingreso_encargado()
            insertar_ventas_db(nombre, "IN")
            
        #apagar sistema
        case '3':
          
            break
        #default
        case _:
            print("Opción inválida")
            continue
# Función para salir del sistema y guardar los datos del encargado
#def salir_seguro():
    #encargado = encargado_entry.get()
    #if encargado:
        #insertar_registro_db(encargado, "OUT")
        #conexion.close()
        #ventana.quit()
    #else:
        #messagebox.showerror("Error", "No hay encargado registrado para guardar el turno.")

conexion.close()

print("Apagando sistema...")
