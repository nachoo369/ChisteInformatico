#Debe tener la libreria Tkinter para continuar
import tkinter as tk
from tkinter import *
import secrets
from tkinter.messagebox import *
from tkinter import ttk
#Se crea el objeto en este caso una ventana 
ventana = tk.Tk()
#Titulo de nuestra ventana -> str
ventana.title("Chistosito")
#Dimensiones de la ventana al ejecutarse.
ventana.geometry("300x100")
#Creamos textos necesarios
pregunta = tk.Label(ventana, text="¿Quieres leer los mejores chistes?")
comentario = tk.Label(ventana, text="Comentario: cuando lea todos \nlos chistes el programa se cerrara")
pregunta.pack()
comentario.pack()
#image = tk.PhotoImage(file="oo.png")
 # creando objeto
 

class CHISTE:
    
    def __init__(self):
        self.chistes = [
                        "— ¿Qué le dice un jaguar a otro jaguar. \n-- Jaguar you",
                        "— Papá, ¿qué se siente tener un hijo tan guapo?\n— No sé hijo, pregúntale a tu abuelo…", 
                        "— ¿Qué le dice una taza a otra?\n—¿Que taza ciendo?", 
                        "— Me da un café con leche corto.\n — Se me ha roto la máquina, cambio. ",
                        "— ¿Por qué lloraba el libro de matemáticas?\n — ¡Porque tenía muchos problemas!"]
    def chistee(self):
        print(secrets.choice(self.chistes))
    def click(self):
        top = Toplevel()
        top.geometry("400x250")
        texto = self.chistes.pop()
        label1 = Label(top, text=texto)

        label1.pack()
        if (top):
            if texto == "— ¿Qué le dice un jaguar a otro jaguar. \n-- Jaguar you":
                self.chistes.append("— ¿Qué le dice un jaguar a otro jaguar. \n-- Jaguar you")
                self.chistes.append("— Papá, ¿qué se siente tener un hijo tan guapo?\n— No sé hijo, pregúntale a tu abuelo…")
                self.chistes.append("— ¿Qué le dice una taza a otra?\n—¿Que taza ciendo?")
                self.chistes.append("— Me da un café con leche corto.\n — Se me ha roto la máquina, cambio. ")
                self.chistes.append("— ¿Por qué lloraba el libro de matemáticas?\n — ¡Porque tenía muchos problemas!")
                return texto
                
            else:
                return
                
                

        
a = CHISTE().click



#Creamos botones para interaccion con usuario
boton1 = Button(ventana, text='Si  ', command=a)

boton2 = Button(ventana, text="No, Gracias", command=ventana.quit)



#Metodos de botones 
#place permite acomodar dentro de nuestra ventana en la grafica 
#x , y
pregunta.place(x=65, y= 20)
comentario.place(x=55, y= 65)
boton1.place(x=100, y=40)
boton2.place(x= 130, y= 40)


# 
ventana.mainloop()