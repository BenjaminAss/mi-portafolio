from tkinter import *

root = Tk()

root.title("Calculadora")

i = 0

#Entrada

e_texto = Entry (root, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan= 4, padx=5 , pady=5)

#Funcioneas

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operaciones():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

#Botones

boton1 = Button(root, text= "1", width=5, height=2, command= lambda: click_boton(1))
boton2 = Button(root, text= "2", width=5, height=2, command= lambda: click_boton(2))
boton3 = Button(root, text= "3", width=5, height=2, command= lambda: click_boton(3))
boton4 = Button(root, text= "4", width=5, height=2, command= lambda: click_boton(4))
boton5 = Button(root, text= "5", width=5, height=2, command= lambda: click_boton(5))
boton6 = Button(root, text= "6", width=5, height=2, command= lambda: click_boton(6))
boton7 = Button(root, text= "7", width=5, height=2, command= lambda: click_boton(7))
boton8 = Button(root, text= "8", width=5, height=2, command= lambda: click_boton(8))
boton9 = Button(root, text= "9", width=5, height=2, command= lambda: click_boton(9))
boton0 = Button(root, text= "0", width=13, height=2, command= lambda: click_boton(0))

boton_borrar = Button(root, text= "AC", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(root, text= "(", width=5, height=2, command= lambda: click_boton("("))
boton_parentesis2 = Button(root, text= ")", width=5, height=2, command= lambda: click_boton(")"))
boton_punto = Button(root, text= ".", width=5, height=2, command= lambda: click_boton("."))

boton_div = Button(root, text= "/", width=5, height=2, command= lambda: click_boton("/"))
boton_mult = Button(root, text= "x", width=5, height=2, command= lambda: click_boton("x"))
boton_suma = Button(root, text= "+", width=5, height=2, command= lambda: click_boton("+"))
boton_resta = Button(root, text= "-", width=5, height=2, command= lambda: click_boton("-"))
boton_igual = Button(root, text= "=", width=5, height=2, command= lambda: operaciones())


#Agregar Botones en pantalla

boton_borrar.grid(row =1 , column =0, padx = 5, pady = 5)
boton_parentesis1.grid(row =1 , column =1, padx = 5, pady = 5)
boton_parentesis2.grid(row =1 , column =2, padx = 5, pady = 5)
boton_div.grid(row =1 , column =3, padx = 5, pady = 5)

boton7.grid(row = 2 , column =0, padx = 5, pady = 5)
boton8.grid(row =2 , column =1, padx = 5, pady = 5)
boton9.grid(row =2 , column =2, padx = 5, pady = 5)
boton_mult.grid(row =2 , column =3, padx = 5, pady = 5)

boton6.grid(row =3 , column =0, padx = 5, pady = 5)
boton5.grid(row = 3, column =1, padx = 5, pady = 5)
boton4.grid(row = 3, column =2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column =3, padx = 5, pady = 5)

boton3.grid(row = 4 , column =0, padx = 5, pady = 5)
boton2.grid(row = 4, column =1, padx = 5, pady = 5)
boton1.grid(row = 4, column =2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column =3, padx = 5, pady = 5)

boton0.grid(row = 5 , column = 0, padx = 5, pady = 5, columnspan=2)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)

root.mainloop()