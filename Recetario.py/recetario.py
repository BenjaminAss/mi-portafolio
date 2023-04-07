import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

recetario = []

#----------------------------METODOS---------------------------------------------------------------------------------------

#---------------------CREAR RECETARIO NUEVO----------------------------------------------------------------------------------------------

def crear_tabla():
    """Crea un recetario"""

    valor = messagebox.askquestion("Recetario nuevo", "Desea crear un recetario nuevo?")
    if valor =='yes':
        with open("recetario.csv", 'w', newline="") as f2:
            f2.close
        messagebox.showinfo("Recetario", "Recetario creado")

    else:
        messagebox.showwarning("Recetario", "Para poder guardar una receta primero debe crear su recetario.")

#---------------------AGREGAR RECETA AL RECETARIO----------------------------------------------------------------------------------------------

def agregar_receta():
    """Agrega una nueva receta al recetario"""

    receta = {}
    receta ['nombre'] = entry_nombre.get()
    receta ['ingredientes'] = entry_ingredientes.get()
    receta ['preparacion'] = entry_preparacion.get()
    receta ['tiempo de preparacion'] = entry_tiempo_preparacion.get()
    receta ['tiempo de coccion'] = entry_tiempo_coccion.get()
    receta ['fecha y hora'] = entry_fecha_hora.get()
    recetario.append(receta)

    with open("recetario.csv", 'a', newline="") as f2:
        f2.write(f"{receta}\n")
        entry_nombre.delete(0,END)
        entry_ingredientes.delete(0,END)
        entry_preparacion.delete(0,END)
        entry_tiempo_preparacion.delete(0,END)
        entry_tiempo_coccion.delete(0,END)
        entry_fecha_hora.delete(0,END)
    
    print("Registro de receta nueva")

#---------------------MODIFICAR RECETA DEL RECETARIO----------------------------------------------------------------------------------------------

def modificar_receta():
    """Modifica una receta del recetario"""

    receta_nueva = {}
    receta_nueva ['nombre'] = entry_nombre.get()
    receta_nueva ['ingredientes'] = entry_ingredientes.get()
    receta_nueva ['preparacion'] = entry_preparacion.get()
    receta_nueva ['tiempo de preparacion'] = entry_tiempo_preparacion.get()
    receta_nueva ['tiempo de coccion'] = entry_tiempo_coccion.get()
    receta_nueva ['fecha y hora'] = entry_fecha_hora.get()
    with open("recetario.csv", 'w', newline="") as f2:

        for receta in recetario:
            if receta_nueva["nombre"][0] == receta['nombre'][0]:
                f2.write(f"{receta_nueva}\n")
                receta = receta_nueva 
                print("Modificacion de receta")
        
        entry_nombre.delete(0,END)
        entry_ingredientes.delete(0,END)
        entry_preparacion.delete(0,END)
        entry_tiempo_preparacion.delete(0,END)
        entry_tiempo_coccion.delete(0,END)
        entry_fecha_hora.delete(0,END)

#----------------------MOSTRAR RECETAS----------------------------------------------------------------------------------------------

def mostrar_datos():
    """Muestra las recetas que se encuentran dentro del recetario"""

    #TABLA
    tabla = ttk.Treeview(root, columns=('nombre', 'ingredientes', 'preparacion','tiempo de preparacion', 'tiempo de coccion', 'fecha y hora'))

    tabla.grid(row=9, column=0, columnspan=6, pady=10)

    tabla.heading('#0', text='ID')
    tabla.heading('#1', text='NOMBRE')
    tabla.heading('#2', text='INGREDIENTES')
    tabla.heading('#3', text='PREPARACION')
    tabla.heading('#4', text='TIEMPO DE PREPARACION')
    tabla.heading('#5', text='TIEMPO DE COCCION')
    tabla.heading('#6', text='FECHA - HORA')

    with open("recetario.csv", 'r', newline="") as f2:

        for elemento in recetario:
            print("receta en pantalla")
            print(elemento['nombre'], elemento['ingredientes'],elemento['preparacion'],
              elemento['tiempo de preparacion'],elemento['tiempo de coccion'],elemento['fecha y hora'])
            tabla.insert("",0,text='1',values= (elemento['nombre'], elemento['ingredientes'],elemento['preparacion'],
              elemento['tiempo de preparacion'],elemento['tiempo de coccion'],elemento['fecha y hora']))       

#---------------------ELIMINAR RECETA DEL RECETARIO----------------------------------------------------------------------------------------------

def eliminar_receta():
    """Elimina una receta del recetario"""

    with open("recetario.csv", 'w', newline="") as f2:
        
        receta_borrar = {}
        receta_borrar ['nombre'] = mi_nombre.set('')
        receta_borrar ['ingredientes'] = mi_ingredientes.set('')
        receta_borrar ['preparacion'] = mi_preparacion.set('')
        receta_borrar ['tiempo de preparacion'] = mi_tiempo_preparacion.set('')
        receta_borrar ['tiempo de coccion'] = mi_tiempo_coccion.set('')
        receta_borrar ['fecha y hora'] = mi_fecha_hora.set('')
        print("Receta eliminada")
        recetario.pop()
        
        entry_nombre.delete(0,END)
        entry_ingredientes.delete(0,END)
        entry_preparacion.delete(0,END)
        entry_tiempo_preparacion.delete(0,END)
        entry_tiempo_coccion.delete(0,END)
        entry_fecha_hora.delete(0,END)

#---------------------SALIR DEL RECETARIO----------------------------------------------------------------------------------------------

def salir():
    """Funcion que permite cerrar la interfaz"""
    valor = messagebox.askquestion("Salir", "Desea salir del recetario?")
    if valor =='yes':
        root.destroy()
    else:
        pass

#---------------------CAMBIO DE FONDO CLARO/OSCURO----------------------------------------------------------------------------------------------

def imprimir():
    """Funcion que perimte cambiar las tonalidades del fondo del programa entre claro y oscuro"""
    if varOpcion.get()==1:
        root.configure(background="#FFFFFF")
        label_nombre.configure(background="#FFFFFF")
        label_ingredientes.configure(background="#FFFFFF")
        label_preparacion.configure(background="#FFFFFF")
        label_tiempo_preparacion.configure(background="#FFFFFF")
        label_tiempo_coccion.configure(background="#FFFFFF")
        label_fecha_hora.configure(background="#FFFFFF")
        label_nombre.config(font=('Arial',12,'bold'),foreground="black")
        label_ingredientes.config(font=('Arial',12,'bold'),foreground="black")
        label_preparacion.config(font=('Arial',12,'bold'),foreground="black")
        label_tiempo_preparacion.config(font=('Arial',12,'bold'),foreground="black")
        label_tiempo_coccion.config(font=('Arial',12,'bold'),foreground="black")
        label_fecha_hora.config(font=('Arial',12,'bold'),foreground="black")

    
    else:
        root.configure(background="#2C2A2A")
        label_nombre.configure(background="#2C2A2A")
        label_ingredientes.configure(background="#2C2A2A")
        label_preparacion.configure(background="#2C2A2A")
        label_tiempo_preparacion.configure(background="#2C2A2A")
        label_tiempo_coccion.configure(background="#2C2A2A")
        label_fecha_hora.configure(background="#2C2A2A")
        label_nombre.config(font=('Arial',12,'bold'),foreground="#FFFFFF")
        label_ingredientes.config(font=('Arial',12,'bold'),foreground="#FFFFFF")
        label_preparacion.config(font=('Arial',12,'bold'),foreground="#FFFFFF")
        label_tiempo_preparacion.config(font=('Arial',12,'bold'),foreground="#FFFFFF")
        label_tiempo_coccion.config(font=('Arial',12,'bold'),foreground="#FFFFFF")
        label_fecha_hora.config(font=('Arial',12,'bold'),foreground="#FFFFFF")

#-------------------------INTERFAZ TKINTER-------------------------------------------

root = tk.Tk()
root.title('Recetario de Sanguches')
root.resizable(0,0)
root.configure(background="#FFFFFF")

root.iconbitmap('ham.ico')

#-----------------------BARRA DE MENÚ-----------------------------------------

barra_menu = tk.Menu(root)
root.config(menu = barra_menu, width = 300, height = 300)

menu_inicio = tk.Menu(barra_menu, tearoff=0)
menu_temas = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label= 'Inicio', menu = menu_inicio)

menu_inicio.add_command(label = 'Crear Registro', command=crear_tabla)
menu_inicio.add_command(label = 'Eliminar Registro')
menu_inicio.add_separator()
menu_inicio.add_command(label = 'Salir', command= salir)

barra_menu.add_cascade(label= 'Consultas')
barra_menu.add_cascade(label= 'Configuración')
barra_menu.add_cascade(label= 'Ayuda')
barra_menu.add_cascade(label= 'Acerca de')

varOpcion = IntVar()
barra_menu.add_cascade(label= 'Cambiar Tema', menu = menu_temas)
menu_temas.add_radiobutton( label="Claro", variable=varOpcion, value=1, command= imprimir)
menu_temas.add_separator()
menu_temas.add_radiobutton( label="Osuro", variable=varOpcion, value=2, command= imprimir)

#--------------------LABEL DE CADA CAMPO----------------------------------------

label_nombre = tk.Label(root, text='Nombre: ')
label_nombre.config(font=('Arial',12,'bold'))
label_nombre.configure(background="#FFFFFF")
label_nombre.grid(row=0, column=0, padx = 10, pady=10, sticky="w")

label_ingredientes = tk.Label(root, text='Ingredientes: ')
label_ingredientes.config(font=('Arial',12,'bold'))
label_ingredientes.configure(background="#FFFFFF")
label_ingredientes.grid(row=1, column=0, padx = 10, pady=10, sticky="w")

label_preparacion = tk.Label(root, text='Preparacion: ')
label_preparacion.config(font=('Arial',12,'bold'))
label_preparacion.configure(background="#FFFFFF")
label_preparacion.grid(row=2, column=0, padx = 10, pady=10, sticky="w")

label_tiempo_preparacion = tk.Label(root, text='Tiempo de preparacion: ')
label_tiempo_preparacion.config(font=('Arial',12,'bold'))
label_tiempo_preparacion.configure(background="#FFFFFF")
label_tiempo_preparacion.grid(row=3, column=0, padx = 10, pady=10, sticky="w")

label_tiempo_coccion = tk.Label(root, text='Tiempo de Coccion: ')
label_tiempo_coccion.config(font=('Arial',12,'bold'))
label_tiempo_coccion.configure(background="#FFFFFF")
label_tiempo_coccion.grid(row=3, column=2, padx = 10, pady=10, sticky="w")

label_fecha_hora = tk.Label(root, text='Fecha y Hora: ')
label_fecha_hora.config(font=('Arial',12,'bold'))
label_fecha_hora.configure(background="#FFFFFF")
label_fecha_hora.grid(row=4, column=0, padx = 10, pady=10, sticky="w")

#---------------------ENTRY DE CADA CAMPO------------------------------------------

mi_nombre = tk.StringVar()
entry_nombre = tk.Entry(root)
entry_nombre.config(width=100, font=('Arial',12))
entry_nombre.grid(row=0, column=1, padx = 10, pady=10, columnspan=4)

mi_ingredientes = tk.StringVar()
entry_ingredientes = tk.Entry(root)
entry_ingredientes.config(width=100, font=('Arial',12))
entry_ingredientes.grid(row=1, column=1, padx = 10, pady=10, columnspan=4)

mi_preparacion = tk.StringVar()
entry_preparacion = tk.Entry(root)
entry_preparacion.config(width=100, font=('Arial',12))
entry_preparacion.grid(row=2, column=1, padx = 10, pady=10, columnspan=4)

mi_tiempo_preparacion = tk.StringVar()
entry_tiempo_preparacion = tk.Entry(root)
entry_tiempo_preparacion.config(width=22, font=('Arial',12))
entry_tiempo_preparacion.grid(row=3, column=1, padx = 5, pady=5, columnspan=1)

mi_tiempo_coccion = tk.StringVar()
entry_tiempo_coccion = tk.Entry(root)
entry_tiempo_coccion.config(width=22, font=('Arial',12))
entry_tiempo_coccion.grid(row=3, column=3, padx = 5, pady=5, columnspan=1)

mi_fecha_hora = tk.StringVar()
entry_fecha_hora = tk.Entry(root)
entry_fecha_hora.config(width=100, font=('Arial',12))
entry_fecha_hora.grid(row=4, column=1, padx = 10, pady=10, columnspan=4)

#-------------------------------BOTONES------------------------------------------

#-------------------------------GUARDAR------------------------------------------

boton_guardar = tk.Button(root, text="Guardar", command = agregar_receta)
boton_guardar.config(width=20, font=('Arial',12,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_guardar.grid(row=6, column=0)

#-------------------------------MODIFICAR------------------------------------------

boton_modificar = tk.Button(root, text="Modificar", command = modificar_receta)
boton_modificar.config(width=20, font=('Arial',12,'bold'),
    fg = 'white', bg = '#1ABC9C', 
    cursor = 'hand2', activebackground='#48C9B0')
boton_modificar.grid(row=6, column=1)

#-------------------------------ELIMINAR------------------------------------------

boton_eliminar = tk.Button(root, text="Eliminar", command =lambda: eliminar_receta())
boton_eliminar.config(width=20, font=('Arial',12,'bold'),
    fg = 'white', bg = '#CB4335', 
    cursor = 'hand2', activebackground='#EC7063')
boton_eliminar.grid(row=6, column=2)

#-------------------------------MOSTRAR------------------------------------------

boton_mostrar = tk.Button(root, text="Mostrar Recetario", command = mostrar_datos)
boton_mostrar.config(width=20, font=('Arial',12,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_mostrar.grid(row=6, column=3)

root.mainloop()

