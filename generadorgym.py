#-----Generador de rutina para gimnasio

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random 
from io import open

root=Tk()
root.title("Generador de rutinas de gimnasio")
root.geometry("+200+100")
root.resizable(0,0)
#-----------Variables-----------------

pechoPrint=StringVar()
bicepPrint=StringVar()
tricepPrint=StringVar()
hombroPrint=StringVar()
espaldaPrint=StringVar()
cuadriPrint=StringVar()
femoPrint=StringVar()
absPrint=StringVar()
pantoPrint=StringVar()


#-----------Lista de ejercicios-------
pecho=("Press de pecho con barra","Press de pecho con mancuernas","Press de pecho inclinado con barra","Press de pecho inclinado con mancuermas",
"Press de pecho declinado con mancuernas", "Fly de pecho con mancuernas", "Fly de pecho en aparato")
triceps=("Extensión de tríceps con polea", "Fondos","Elevación de tricep (copa)","Patada de tríceps con mancuernas","Press de banca con agarre cerrado",
"Extensión de tríceps con barra" )
biceps=("Curl de bícep con mancuermas","Curl de bíceps con barra", "Curl de bíceps con cable", "Curl de bíceps de martillo con mancuernas", "Curl de bíceps en predicador con barra",
"Curl de bíceps de predicador con mancuerna")
hombros=("Press militar con mancuernas","Elevación lateral con mancuernas","Elevación frontal con mancuernas","Elevación frontal con barra","Elevación frontal inclinado",
"Fly inverso en máquina","Press militar con barra",
"Levantamiento frontal con deltoides")
espalda=("Pull down abierto con polea","Remo con cable", "Remo con mancuernas", "Pull down agarre cerrado con polea", "Remo con máquina")
cuadriceps=("Extensión de pierna","Hack squat","Sentadilla libre","Sentadilla en máquina smith","Press de pierna en prensa")
femoral=("Curl de pierna en máquina","Curl de pierna con cable", "Sentadilla con apertura amplia",)
pantorrillas=("Extensión de pantorrila en máquina", "Extensión de pantorrilla con barra","Extensión de pantorrilla en smith", "Máquina costurera")
abdomen=("Crunch abdominal en mánina","Crunch abdominal libre","Extensiones con rodillo","Curl lateral con cable", "Elevaciones de piernas suspendido","Elevaciones de piernas en banco",
"Elevaciones de piernas en máquina")

#------------Funciones del menu---------

def gen_rutina():

    pechoSel=random.choice(pecho)
    bicepSel=random.choice(biceps)
    tricepSel=random.choice(triceps)
    hombroSel=random.choice(hombros)
    espaldaSel=random.choice(espalda)
    cuadriSel=random.choice(cuadriceps)
    femoSel=random.choice(femoral)
    pantoSel=random.choice(pantorrillas)
    abdomenSel=random.choice(abdomen)

    pechoPrint.set(pechoSel)
    bicepPrint.set(bicepSel)
    tricepPrint.set(tricepSel)
    hombroPrint.set(hombroSel)
    espaldaPrint.set(espaldaSel)
    cuadriPrint.set(cuadriSel)
    femoPrint.set(femoSel)
    pantoPrint.set(pantoSel)
    absPrint.set(abdomenSel)

    
def save():
    savepath=filedialog.asksaveasfilename(title="Guardar como archivo de texto", filetypes=[("Archivo de texto", ".txt")])

    archivo=open(savepath, "w")
    rutina=(pechoPrint.get(), bicepPrint.get(), tricepPrint.get(), hombroPrint.get(),espaldaPrint.get(), cuadriPrint.get(),
    femoPrint.get(),pantoPrint.get(),absPrint.get())
    saver=str(rutina)
    archivo.write(saver)
    archivo.close()

def salir():
    kill=messagebox.askyesno("Salir","¿Desea salir del programa?")
    if kill==TRUE:
        root.destroy()


def acerca_de():
    messagebox.showinfo("Generador de rutinas","Programa escrito por Guzblack\nguz.black@gmail.com")


#------------Contenidos del menu------------------------

barramenu=Menu(root)

root.config(menu=barramenu)

menuArchivo=Menu(barramenu, tearoff=0)
menuArchivo.add_command(label="Guardar en archivo de texto",command=lambda:save())
menuArchivo.add_command(label="Salir", command=lambda:salir())

menuAyuda=Menu(barramenu,tearoff=0)
menuAyuda.add_command(label="Acerca de",command=lambda:acerca_de())

#-----------Textos de la barra menu----------

barramenu.add_cascade(label="Archivo",menu=menuArchivo)
barramenu.add_cascade(label="Ayuda",menu=menuAyuda)


#-------------FRAME-----------------------
frame=Frame(root, width=800, height=600)
frame.pack()

try:
    imagen=PhotoImage(file="blumatrix.png")
    fondo=Label(frame, image=imagen).place(x=0, y =0)
except:
    pass

#-----------Contenido del frame------------------
textopecho=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Pecho")
textopecho.grid(row=0, column=0, padx=15, pady=15)

cuadropecho=Entry(frame, width=31, font=("Uroob, bold", 12), textvariable=pechoPrint)
cuadropecho.grid(row=0, column=1, padx=15, pady=15)

textobiceps=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Bíceps")
textobiceps.grid(row=1, column=0, padx=15, pady=15)

cuadrobiceps=Entry(frame, width=31,font=("Uroob, bold", 12), textvariable=bicepPrint)
cuadrobiceps.grid(row=1, column=1, padx=15, pady=15)

textotriceps=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Tríceps")
textotriceps.grid(row=2, column=0, padx=15, pady=15)

cuadrotriceps=Entry(frame, width=31,font=("Uroob, bold", 12), textvariable=tricepPrint)
cuadrotriceps.grid(row=2, column=1, padx=15, pady=15)

textohombros=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Hombros")
textohombros.grid(row=3, column=0, padx=15, pady=15)

cuadrohombros=Entry(frame, width=31, font=("Uroob, bold", 12), textvariable=hombroPrint)
cuadrohombros.grid(row=3, column=1, padx=15, pady=15)

textoespalda=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Espalda")
textoespalda.grid(row=4, column=0, padx=15, pady=15)

cuadroespalda=Entry(frame, width=31, font=("Uroob, bold", 12), textvariable=espaldaPrint)
cuadroespalda.grid(row=4, column=1, padx=15, pady=15)

textocuads=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Cuádriceps")
textocuads.grid(row=0, column=2, padx=15, pady=15)

cuadrocuads=Entry(frame, width=31,font=("Uroob, bold", 12), textvariable=cuadriPrint)
cuadrocuads.grid(row=0, column=3, padx=15, pady=15)

textofemo=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Femoral")
textofemo.grid(row=1, column=2, padx=15, pady=15)

cuadrofemo=Entry(frame, width=31,font=("Uroob, bold", 12), textvariable=femoPrint)
cuadrofemo.grid(row=1, column=3, padx=15, pady=15)

textoabs=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Abdomen")
textoabs.grid(row=2, column=2, padx=15, pady=15)

cuadroabs=Entry(frame, width=31, font=("Uroob, bold", 12),textvariable=absPrint)
cuadroabs.grid(row=2, column=3, padx=15, pady=15)

textopanto=Label(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Pantorrillas")
textopanto.grid(row=3, column=2, padx=15, pady=15)

cuadropanto=Entry(frame, width=31,font=("Uroob, bold", 12), textvariable=pantoPrint)
cuadropanto.grid(row=3, column=3, padx=15, pady=15)

botonGenerar=Button(frame, font=("Uroob, bold", 16),fg="white", bg="black", text="Generar rutina", command=lambda:gen_rutina())
botonGenerar.grid(row=4, column=3, padx=15, pady=15)


root.mainloop()

