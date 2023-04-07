from tkinter import Tk
import tkinter as tk
from tkinter import ttk
        
def prob_ocup():

    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60
    p = float(((min_llegada/min_servicio)*100))
    pantalla_resultado1.insert(0, p)

def fun_lq():

    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60

    lq = float((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))

    pantalla_resultado2.insert(0, lq)

def fun_l():

    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60

    l = float((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada))+(min_llegada/min_servicio))

    pantalla_resultado3.insert(0, l)

def fun_wq():
    
    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60

    wq = float(((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))/min_llegada)

    pantalla_resultado4.insert(0, wq)

def fun_w():

    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60

    w = float((((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))/min_llegada)+(1/min_servicio))

    pantalla_resultado5.insert(0, w)

def fun_n_ocioso():
    
    landa = int(landa_entry.get())
    muu = int(muu_entry.get())

    min_llegada = landa/60
    min_servicio = muu/60
    n = float(100-(((min_llegada/min_servicio)*100)))
    pantalla_resultado6.insert(0, n)

def fun_ws():

    muu = int(muu_entry.get())

    min_servicio = muu/60
    ws = float(1/min_servicio)
    pantalla_resultado7.insert(0, ws)


def nuevo_calculo():
    pantalla_resultado1.delete(0, 1000)
    pantalla_resultado2.delete(0, 1000)
    pantalla_resultado3.delete(0, 1000)
    pantalla_resultado4.delete(0, 1000)
    pantalla_resultado5.delete(0, 1000)
    pantalla_resultado6.delete(0, 1000)
    pantalla_resultado7.delete(0, 1000)
    landa_entry.delete(0, 1000)
    muu_entry.delete(0,1000)

root = Tk()
root.title("Modelo de Lineas de Espera")
root.geometry("880x450")
root.resizable(0,0)
root.configure(background="#2A2C2C")

#LABEL

landa_label = tk.Label(root, text="TIEMPO PROMEDIO DE LLEGADAS: ")
landa_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
landa_label.grid(row=1, column=1, padx= 20, pady= 20, sticky="w")

muu_label = tk.Label(root, text="TIEMPO PROMEDIO DE SERVICIO: ")
muu_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
muu_label.grid(row=2, column=1,  padx= 20, pady= 20, sticky="w")

lq_label = tk.Label(root, text="N° promedio de clientes que se encuentran esperando a ser atendidos --> ")
lq_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
lq_label.grid(row=4, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

l_label = tk.Label(root, text="N° promedio de clientes en el sistema --> ")
l_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
l_label.grid(row=5, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

wq_label = tk.Label(root, text="Tiempo promedio que un cliente espera a ser atendido --> ")
wq_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
wq_label.grid(row=6, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

w_label = tk.Label(root, text="Tiempo promedio que un cliente pasa en el sistema --> ")
w_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
w_label.grid(row=7, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

n_label = tk.Label(root, text="Probabilidad de que el sistema este vacío --> ")
n_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
n_label.grid(row=8, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

ws_label = tk.Label(root, text="Tiempo de servicio --> ")
ws_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
ws_label.grid(row=10, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

#ENTRY

mi_landa = tk.IntVar()
landa_entry = tk.Entry(root)
landa_entry.configure(background="#FFFFFF")
landa_entry.grid(row=1, column=2, padx= 5, pady= 20, sticky="w")

mi_muu = tk.IntVar()
muu_entry = tk.Entry(root)
muu_entry.configure(background="#FFFFFF")
muu_entry.grid(row=2, column=2,  padx= 5, pady= 20, sticky="w")

#RESULTADO

pantalla_resultado1 = tk.Entry(root)
pantalla_resultado1.grid(row=2, column=4)

texto1 = tk.Label(root, text="% " + "del tiempo el sistema está ocupado")
texto1.configure(background="#2A2C2C", foreground="#FFFFFF")
texto1.grid(row=2, column=5)

linea1 = tk.Label(root, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
linea1.grid(row=3, column=0, columnspan=10)

pantalla_resultado2 = tk.Entry(root)
pantalla_resultado2.grid(row=4, column=4)

pantalla_resultado3 = tk.Entry(root)
pantalla_resultado3.grid(row=5, column=4)

pantalla_resultado4 = tk.Entry(root)
pantalla_resultado4.grid(row=6, column=4)

pantalla_resultado5 = tk.Entry(root)
pantalla_resultado5.grid(row=7, column=4)

pantalla_resultado6 = tk.Entry(root)
pantalla_resultado6.grid(row=8, column=2)

texto1 = tk.Label(root, text="% " + "del tiempo el sistema está vacío")
texto1.configure(background="#2A2C2C", foreground="#FFFFFF")
texto1.grid(row=8, column=4)

linea1 = tk.Label(root, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
linea1.grid(row=9, column=0, columnspan=10)

pantalla_resultado7 = tk.Entry(root)
pantalla_resultado7.grid(row=10, column=2)

linea1 = tk.Label(root, text=" * Todos los valores de tiempo están en minutos y los de numero de clientes (cantidad) en unidades")
linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
linea1.grid(row=11, column=0, columnspan=10, padx= 15 , pady= 15)

#BOTONES

boton_calcular1 = tk.Button(root, text="Calcular", width=10, height=1, command= prob_ocup)
boton_calcular1.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular1.grid(row=1, column=4)

boton_nuevo = tk.Button(root, text="Nuevo", width=10, height=1, command= nuevo_calculo)
boton_nuevo.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_nuevo.grid(row=1, column=5)

boton_calcular2 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_lq)
boton_calcular2.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular2.grid(row=4, column=5)

boton_calcular3 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_l)
boton_calcular3.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular3.grid(row=5, column=5)

boton_calcular4 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_wq)
boton_calcular4.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular4.grid(row=6, column=5)

boton_calcular5 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_w)
boton_calcular5.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular5.grid(row=7, column=5)

boton_calcular6 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_n_ocioso)
boton_calcular6.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular6.grid(row=8, column=5)

boton_calcular7 = tk.Button(root, text="Calcular", width=10, height=1, command= fun_ws)
boton_calcular7.config(font=('Arial',8,'bold'),
    fg = 'white', bg = '#52BE80', 
    cursor = 'hand2', activebackground='#58D68D')
boton_calcular7.grid(row=10, column=5)

root.mainloop()
