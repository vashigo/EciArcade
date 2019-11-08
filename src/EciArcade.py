import sys  # lib control de archivos
import os as Os  # lib control de archivos
import os.path as path  # lib leer archivos
import tkinter as tk  # lib tkinter
from tkinter import messagebox  # lib messagebox de tkinter
import re  # email verification libreria
import random

# variables de control de ventanas de tkinter para abrir y cerrarlas libremente
ventana_Principal = 0
ventana_selección = 0
ventana_autentificacion = 0
ventana_tic = 0
ventana_ahorcado = 0
vent_selec = 0

# variables globales tic-tac-toe
pa = ""
playerb = ""
p1 = ""
p2 = ""
bclick = True
flag = 0
buttons = []
botonesAhorcado = []
# variable ahorcado
marcasAhorcado=["coca cola","nike","chrome","google","windows","apple","mcdonalds","youtube","samsung","huawei","disney","virgin",
           "gillette","lacoste","lenovo","caterpillar","amazon","mastercard","rolex","nintendo","play station","kelloggs",
           "spotify","instagram","facebook","snapchat","yahoo"]
autosAhorcado=["chevrolet","renault","ferrari","volkswagen","fiat","volvo","land Rover","Lotus","ford","mercedes benz","toyota",
            "jaguar","dodge","lamborghini","koenigseng","maserati","bugatti","hyundai","roll royce","porsche","mclaren",
            "lexus","pagani","aston martin","peugeot","mini cooper","subaru","mitsubishi","cadillac","chrysler","bentley"]
equiposAhorcado=["tottenham","chelsea","liverpool","burnley","southampton","swansea","manchester city","arsenal","juventus","atalanta",
            "fiorentina","cagliari","sampdoria","bologna","udinese","olympique","marsella","toulose","barcelona","real madrid",
            "atletico de madrid","villarreal","espanyol","getafe","real sociedad","las palmas","leverkusen","wolfsburgo","hamburgo",
            "dortmund","bayern munich","shalke"]
marcas = False
autos = False
equipos = False
seleccionAhorcadoCategoria = 0
imagenAhorcado = ""
tectPerdAhorcado = ""
palabraAdivinar = ""
intentosAhorcado = 0
TEXT1restantes = ""
TEXT1intentos = ""
TEXT1Ahor = ""
palabrasRestantesAhorcado = 0
letrasSeleccionadas = []
palabraAhorcado = ""
palabras = []
palabra= ""


# ventana de bienvenida
def ventana_Principal():
    global ventana_Principal, ventana_selección, ventana_autentificacion
    # crea ventana y se le hacen configuraciones
    ventana_Principal = tk.Tk()
    ventana_Principal.title("Bienvenido")
    ventana_Principal.configure(background="white")
    ventana_Principal.geometry("650x300")
    ventana_Principal.resizable(
        width=False, height=False)  # no se podra grandar
    fondo = tk.PhotoImage(file="fondo2.png")  # carga imagen
    lblFondo = tk.Label(ventana_Principal, image=fondo)  # fondo
    bit = ventana_Principal.iconbitmap('icono.ico')  # icono
    lblFondo.place(x=0, y=0, relwidth=1, relheight=1)  # centrar fondo
    # texto de bienvenida
    TEXT1 = tk.Label(ventana_Principal, text="Bienvenido a minijuegos\n EciArcade",
                     bg="#086E85", fg="white", font='Helvetica 30 bold', relief="flat")
    TEXT1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton2 = tk.Button(ventana_Principal, text="Entrar", command=ventana_autentificacion, font='Helvetica 16 bold',
                       bg="#086E85", fg="white", bd=5, activebackground="white", relief="solid")  # boton iniciar
    boton2.pack(padx=5, pady=2, ipadx=20, ipady=5,
                side=tk.BOTTOM, before=TEXT1)
    boton3 = tk.Button(ventana_Principal, text="Cerrar", command=ventana_Principal.destroy,
                       font='Helvetica 10 bold', bg="white", fg="black", relief="solid", bd=5)  # boton cerrar
    boton3.pack(padx=5, pady=2, ipadx=20, ipady=5,
                side=tk.BOTTOM, before=boton2)
    center(ventana_Principal)  # centrar ventana
    ventana_Principal.mainloop()


def ventana_autentificacion():
    global ventana_Principal, ventana_selección, ventana_autentificacion

    def verifica():
        global ventana_selección
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.get().lower()):
            if("mail.escuelaing.edu.co" in correo.get()):
                if(vent_selec == 0):
                    ventana_selección()
                else:
                    ventana_autentificacion.withdraw()
                    ventana_selección.deiconify()
            else:
                messagebox.showinfo(message="Correo no Valido!", title="Error")
                caja1.delete(0, tk.END)  # limpia la caja
        else:
            messagebox.showinfo(message="Correo no Valido!", title="Error")
            caja1.delete(0, tk.END)  # limpia la caja
    ventana_Principal.withdraw()
    ventana_autentificacion = tk.Toplevel()
    ventana_autentificacion.title("Autentificación")
    ventana_autentificacion.resizable(width=False, height=False)

    fondo = tk.PhotoImage(file="fondo2.png")
    bit = ventana_autentificacion.iconbitmap('icono.ico')  # icono
    lblFondo = tk.Label(ventana_autentificacion, image=fondo).place(x=0, y=0)
    TEXT1 = tk.Label(ventana_autentificacion, text="Ingrese el correo para continuar",
                     bg="black", fg="white", font='Helvetica 20 bold')
    TEXT1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    correo = tk.StringVar(ventana_autentificacion)
    tk.Label(ventana_autentificacion, text="Correo de la escuela:").pack(
        padx=5, pady=5, ipadx=5, ipady=5)
    caja1 = tk.Entry(ventana_autentificacion,
                     textvariable=correo, justify=tk.CENTER)
    caja1.pack(padx=5, pady=5, ipadx=100, ipady=5)

    botonVerifica = tk.Button(ventana_autentificacion, text="INGRESAR",
                              command=verifica, font='Helvetica 16 bold', bg="#21BDE8")
    botonVerifica.pack(padx=5, pady=2, ipadx=40, ipady=0, side=tk.TOP)

    center(ventana_autentificacion)
    ventana_autentificacion.mainloop()


def ventana_selección():
    global ventana_Principal, ventana_selección, ventana_autentificacion, vent_selec

    def sair():
        global ventana_Principal, ventana_selección
        ventana_selección.withdraw()
        ventana_Principal.deiconify()
    vent_selec = 1
    ventana_autentificacion.destroy()
    # crea ventana y se le hacen configuraciones
    ventana_selección = tk.Toplevel()
    ventana_selección.title("Bienvenido")
    ventana_selección.configure(background="white")
    ventana_selección.geometry("704x396")
    ventana_selección.resizable(
        width=False, height=False)  # no se podra grandar
    fondo = tk.PhotoImage(file="seleccion.png")  # carga imagen
    lblFondo = tk.Label(ventana_selección, image=fondo)  # fondo
    bit = ventana_selección.iconbitmap('icono.ico')  # icono
    lblFondo.place(x=0, y=0, relwidth=1, relheight=1)  # centrar fondo
    # texto de bienvenida
    TEXT1 = tk.Label(ventana_selección, text="Escoga su juego:",
                     bg="#086E85", fg="white", font='Helvetica 30 bold', relief="flat")
    TEXT1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton2 = tk.Button(ventana_selección, text="Ahorcado", command=ventana_ahorcado, font='Helvetica 16 bold',
                       bg="#21BDE8", fg="white", activebackground="white", relief="solid")  # boton iniciar
    boton2.pack(side="top", expand="yes")
    boton3 = tk.Button(ventana_selección, text="Tic Tac Toe", command=ventana_tic, font='Helvetica 16 bold',
                       bg="#21BDE8", fg="white", activebackground="white", relief="solid")  # boton iniciar
    boton3.pack(side="top", expand="yes")
    boton4 = tk.Button(ventana_selección, text="Adivina", command=ventana_selección, font='Helvetica 16 bold',
                       bg="#21BDE8", fg="white", activebackground="white", relief="solid")  # boton iniciar
    boton4.pack(side="top", expand="yes")
    buton5 = tk.Button(ventana_selección, text="salir", font='Times 10 bold',
                       bg='red', fg='white', height=1, width=8, command=lambda: sair())
    buton5.pack(expand="yes")
    center(ventana_selección)  # centrar ventana

    ventana_selección.mainloop()


def mandarLetra(letra):
    global ventana_ahorcado,tectPerdAhorcado, botonesAhorcado,imagenAhorcado,letrasSeleccionadasBien, letrasSeleccionadas, palabras, palabra, palabrasRestantesAhorcado,intentosAhorcado,palabraAdivinar, TEXT1restantes, TEXT1intentos, TEXT1Ahor
    a = str(letra)
    for i in range(len(botonesAhorcado)):
        if(botonesAhorcado[i]["text"] == a):
            if(botonesAhorcado[i]["bg"] == "red"):
                tk.messagebox.showinfo(
                    "letra no disponible", "ya escogio esa letra!")
            else:
                if (a in palabra):
                    # coloreo la casilla de rojo
                    tk.messagebox.showinfo("Bien!", "la letra " +a+ " está en la palabra")
                    letrasSeleccionadas.append(a)
                    letrasSeleccionadasBien.append(a)
                    botonesAhor()
                    # redibujo letras
                    # letras restantes
                    for j in range(len(palabra)):
                        if(palabra[j] == a):
                            palabrasRestantesAhorcado -= 1 
                    ## armo la palabra d ela forma _ _ _ _ 
                    palabraAdivinar= ""
                    for j in range(len(palabra)):
                        if(palabra[j] in letrasSeleccionadasBien):
                            palabraAdivinar+= " "+palabra[j]+" "
                        else:
                            palabraAdivinar+=" _ "
                    TEXT1restantes["text"]= "letras restantes: "+str(palabrasRestantesAhorcado)
                    # intentos
                    TEXT1intentos["text"] = "intentos restantes: "+str(intentosAhorcado)
                    # letras
                    TEXT1Ahor["text"] = palabraAdivinar
                    
                    botonahor = tk.Button(ventana_ahorcado,image=imagenAhorcado)
                    botonahor.place(x=300, y=50)
                    ##gano!
                    if(palabrasRestantesAhorcado == 0):
                        disableBotonesAhorcado("disabled")     
                        tectPerdAhorcado["text"] = "Ganaste!"
                        tectPerdAhorcado["bg"] = "green"

                else:
                    # coloreo la casilla de rojo
                    letrasSeleccionadas.append(a)
                    botonesAhor()
                    # redibujo letras
                    # letras restantes
                    intentosAhorcado -= 1
                    TEXT1restantes["text"]= "letras restantes: "+str(palabrasRestantesAhorcado)
                    # intentos
                    TEXT1intentos["text"] = "intentos restantes: "+str(intentosAhorcado)
                    # letras
                    TEXT1Ahor["text"] = palabraAdivinar
                    if (intentosAhorcado==7):
                        imagenAhorcado = tk.PhotoImage(file="muñ2.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")
                    elif (intentosAhorcado==6):
                        imagenAhorcado = tk.PhotoImage(file="muñ3.png") 
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")                                          
                    elif (intentosAhorcado==5):
                        imagenAhorcado = tk.PhotoImage(file="muñ4.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")
                    elif (intentosAhorcado==4):
                        imagenAhorcado = tk.PhotoImage(file="muñ5.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")
                    elif (intentosAhorcado==3):
                        imagenAhorcado = tk.PhotoImage(file="muñ6.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")
                    elif (intentosAhorcado==2):
                        imagenAhorcado = tk.PhotoImage(file="muñ7.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra")
                    elif (intentosAhorcado==1):
                        imagenAhorcado = tk.PhotoImage(file="muñ8.png")
                        tk.messagebox.showinfo("Mal!", "la letra " +a+ " No está en la palabra") 
                    elif (intentosAhorcado==0):     
                        tk.messagebox.showinfo("Fin del juego!", "Game Over")
                        disableBotonesAhorcado("disabled")     
                        tectPerdAhorcado["text"] = "Perdiste!"   
                        tectPerdAhorcado["bg"] = "red"                                                                         
                    botonahor = tk.Button(ventana_ahorcado,image=imagenAhorcado)
                    botonahor.place(x=300, y=50)

    ventana_ahorcado.mainloop()

def disableBotonesAhorcado(comando):
    global ventana_ahorcado, botonesAhorcado
    for i in range(len(botonesAhorcado)):
        botonesAhorcado[i].configure(state=comando)

def botonesAhor():
    global ventana_ahorcado, botonesAhorcado, palabras, letrasSeleccionadas, letrasSeleccionadasBien
    # dibujo todos los botones que contienen las letras
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                  "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    formatoLetra = 'Helvetica 10 bold'
    botonesAhorcado = []
    colorFondo = "#F9EC47"
    colorLetra = "black"
    borde = "solid"
    posX = 24
    posY = 300
    # botones letras
    for i in range(len(abecedario)):
        if(i == 9):
            posX = 24
            posY += 55
        elif(i == 18):
            posX = 24
            posY += 55

        if (abecedario[i] in letrasSeleccionadas):
            colorFondo = "red"  # letras rojas ocupadas
        else:
            colorFondo = "white"  # letras verdes desocupadas

        exec('botonAhorcado{} = tk.Button(ventana_ahorcado,text="{}",command= lambda: mandarLetra("{}"),width=3,height=2, font=formatoLetra, bg=colorFondo, fg=colorLetra,relief=borde,bd= 2)'.format(
            abecedario[i], abecedario[i], abecedario[i]))
        exec('botonAhorcado{}.place(x=posX, y=posY)'.format(abecedario[i]))
        exec('botonesAhorcado.append(botonAhorcado{})'.format(
            abecedario[i]))
        posX += 41


def ventana_ahorcado():
    global ventana_Ahorcado_Seleccion,ventana_ahorcado,seleccionAhorcadoCategoria, ventana_selección,tectPerdAhorcado,imagenAhorcado, botonesAhorcado, palabras, palabra,letrasSeleccionadasBien, letrasSeleccionadas, palabrasRestantesAhorcado,intentosAhorcado,palabraAdivinar, TEXT1restantes, TEXT1intentos, TEXT1Ahor, marcasAhorcado,autosAhorcado,equiposAhorcado
    def reiniciar():
        global ventana_ahorcado,tectPerdAhorcado, ventana_selección,imagenAhorcado, botonesAhorcado, palabras, palabra,letrasSeleccionadasBien, letrasSeleccionadas, palabrasRestantesAhorcado,intentosAhorcado,palabraAdivinar, TEXT1restantes, TEXT1intentos, TEXT1Ahor
        imagenAhorcado = tk.PhotoImage(file="muñ1.PNG")
        letrasSeleccionadas = []
        letrasSeleccionadasBien = []
        tectPerdAhorcado["text"] = ""
        tectPerdAhorcado["bg"] = "white"
        palabra = palabras[random.randint(0, len(palabras)-1)]
        imagenAhorcado = tk.PhotoImage(file="muñ1.PNG")
        botonahor = tk.Button(ventana_ahorcado,image=imagenAhorcado)
        botonahor.place(x=300, y=50)
        TEXT1Ahor1 = tk.Label(ventana_ahorcado, text="Seleccione la letra:",
                         bg="white", fg="black", font='Helvetica 13 bold', relief="flat")
        TEXT1Ahor1.place(x=20, y=270)
        palabraAdivinar = ""
        #armar cadena de _ _ _ _ _ _
        for j in range(len(palabra)):
            if(palabra[j] in letrasSeleccionadasBien):
                palabraAdivinar+= " "+palabra[j]+" "
            else:
                palabraAdivinar+=" _ "
        intentosAhorcado = 8
        if(" " in palabra):
            palabrasRestantesAhorcado = len(palabra)-1
            letrasSeleccionadasBien.append(" ")
        else:
            palabrasRestantesAhorcado = len(palabra)
        TEXT1restantes["text"]= "letras restantes: "+str(palabrasRestantesAhorcado)
        # intentos
        TEXT1intentos["text"] = "intentos restantes: "+str(intentosAhorcado)
        # letras
        TEXT1Ahor["text"] = palabraAdivinar
        disableBotonesAhorcado("disabled")
        disableBotonesAhorcado("normal")
        botonesAhor()

    def salir():
        global ventana_ahorcado,ventana_selección
        reiniciar()
        ventana_ahorcado.withdraw()
        ventana_selección.deiconify()
    # Generar palabra
    def jugar(opcion):
        global ventana_ahorcado,seleccionAhorcadoCategoria, ventana_selección,tectPerdAhorcado,imagenAhorcado, botonesAhorcado, palabras, palabra,letrasSeleccionadasBien, letrasSeleccionadas, palabrasRestantesAhorcado,intentosAhorcado,palabraAdivinar, TEXT1restantes, TEXT1intentos, TEXT1Ahor, marcasAhorcado,autosAhorcado,equiposAhorcado
        if(opcion==1):
            seleccionAhorcadoCategoria = 1
            palabras = marcasAhorcado
            categoria = "Marcas internacionales"
            botonAhorcado1["bg"] = "white"
            botonAhorcado2["bg"] = "white"
            botonAhorcado3["bg"] = "red"
            
        elif(opcion==2):
            seleccionAhorcadoCategoria = 2
            palabras = autosAhorcado
            categoria = "Marcas de Autos"
            botonAhorcado1["bg"] = "red"
            botonAhorcado2["bg"] = "white"
            botonAhorcado3["bg"] = "white"

        elif(opcion==3):
            seleccionAhorcadoCategoria = 3
            palabras = equiposAhorcado
            categoria = "Equipos de futbol"
            botonAhorcado2["bg"] = "red"
            botonAhorcado1["bg"] = "white"
            botonAhorcado3["bg"] = "white"
        palabra = palabras[random.randint(0, len(palabras)-1)]
        #si la palabra tiene espacio
        if(" " in palabra):
            palabrasRestantesAhorcado = len(palabra)-1
            letrasSeleccionadasBien.append(" ")
        else:
            palabrasRestantesAhorcado = len(palabra)
        intentosAhorcado = 8
        palabraAdivinar = ""
        #armar cadena de _ _ _ _ _ _
        for j in range(len(palabra)):
            if(palabra[j] in letrasSeleccionadasBien):
                palabraAdivinar+= " "+palabra[j]+" "
            else:
                palabraAdivinar+=" _ "
        print(palabra)
        TEXT1restantes["text"]= "letras restantes: "+str(palabrasRestantesAhorcado)
        # intentos
        TEXT1intentos["text"] = "intentos restantes: "+str(intentosAhorcado)
        # letras
        TEXT1Ahor["text"] = palabraAdivinar
        TEXT1categoria["text"] = "Categoria: "+categoria
        #dibujar botones
        botonesAhor()
        botonAhorcadoREINICIAR.configure(state="normal")
    
    imagenAhorcado = tk.PhotoImage(file="muñ1.PNG")
    letrasSeleccionadas = []
    letrasSeleccionadasBien = []
    palabras = ""
    categoria = ""
    palabra = ""
    palabraAdivinar = ""
    #armar cadena de _ _ _ _ _ _
    for j in range(len(palabra)):
        if(palabra[j] in letrasSeleccionadasBien):
            palabraAdivinar+= " "+palabra[j]+" "
        else:
            palabraAdivinar+=" _ "
    intentosAhorcado = 8
    #si la palabra tiene espacio
    if(" " in palabra):
        palabrasRestantesAhorcado = len(palabra)-1
        letrasSeleccionadasBien.append(" ")
    else:
        palabrasRestantesAhorcado = len(palabra)
    # quito ventana seleccion categoria
    ventana_selección.withdraw()
    # crea ventana y se le hacen configuraciones
    ventana_ahorcado = tk.Toplevel()
    ventana_ahorcado.title("Ahorcado "+categoria)
    ventana_ahorcado.configure(background="white")
    fondo = tk.PhotoImage(file="fondoAhorcado.png")
    bit = ventana_ahorcado.iconbitmap('icono.ico')  # icono
    lblFondoAhorc = tk.Label(ventana_ahorcado, image=fondo).place(x=0, y=0)
    ventana_ahorcado.geometry("410x500")
    ventana_ahorcado.resizable(
        width=False, height=False)  # no se podra grandar
    bit = ventana_ahorcado.iconbitmap('icono.ico')  # icono
    #seleccion categoria
    TEXT1selecCategoria= tk.Label(ventana_ahorcado, text="Seleccione la Categoria: ",
                         bg="white", fg="black", font='Helvetica 12 bold', relief="flat")
    TEXT1selecCategoria.place(x=5, y=0)
    botonAhorcado1= tk.Button(ventana_ahorcado,text="autos",command= lambda: jugar(2),width=8,height=0, font="Helvetica 10 bold", bg="white", fg="black",relief="solid",bd= 1)
    botonAhorcado1.place(x=200, y=0)
    botonAhorcado2 = tk.Button(ventana_ahorcado,text="futbol",command= lambda: jugar(3),width=8,height=0, font="Helvetica 10 bold", bg="white", fg="black",relief="solid",bd= 1)
    botonAhorcado2.place(x=270, y=0)
    botonAhorcado3 = tk.Button(ventana_ahorcado,text="marcas",command= lambda: jugar(1),width=8,height=0, font="Helvetica 10 bold", bg="white", fg="black",relief="solid",bd= 1)
    botonAhorcado3.place(x=340, y=0)
    # categoria
    TEXT1categoria= tk.Label(ventana_ahorcado, text="Categoria: "+categoria,
                         bg="white", fg="black", font='Helvetica 12 bold', relief="flat")
    TEXT1categoria.place(x=20, y=30)
    # letras restantes
    TEXT1restantes= tk.Label(ventana_ahorcado, text="letras restantes: "+str(palabrasRestantesAhorcado),
                         bg="white", fg="black", font='Helvetica 12 bold', relief="flat")
    TEXT1restantes.place(x=20, y=80)
    # intentos
    TEXT1intentos = tk.Label(ventana_ahorcado, text="intentos restantes: "+str(intentosAhorcado),
                         bg="white", fg="black", font='Helvetica 12 bold', relief="flat")
    TEXT1intentos.place(x=20, y=100)
    # letras
    TEXT1Ahor1 = tk.Label(ventana_ahorcado, text="palabra:",
                         bg="white", fg="black", font='Helvetica 15 bold', relief="flat")
    TEXT1Ahor1.place(x=20, y=170)
    TEXT1Ahor = tk.Label(ventana_ahorcado, text=palabraAdivinar,
                         bg="white", fg="black", font='Helvetica 18 bold', relief="flat")
    TEXT1Ahor.place(x=20, y=200)
    ## muñeco
    botonahor = tk.Button(ventana_ahorcado,image=imagenAhorcado)
    botonahor.place(x=300, y=50)
    TEXT1Ahor1 = tk.Label(ventana_ahorcado, text="Seleccione la letra:",
                         bg="white", fg="black", font='Helvetica 13 bold', relief="flat")
    TEXT1Ahor1.place(x=20, y=270)
    ##botones reiniciar y salir
    botonAhorcadoSALIR = tk.Button(ventana_ahorcado,text="salir",command= lambda: salir(),width=8,height=1, font="Helvetica 10 bold", bg="blue", fg="black",relief="solid",bd= 2)
    botonAhorcadoSALIR.place(x=100, y=460)
    botonAhorcadoREINICIAR = tk.Button(ventana_ahorcado,text="Reiniciar",command= lambda: reiniciar(),width=8,height=1, font="Helvetica 10 bold", bg="red", fg="black",relief="solid",bd= 2)
    botonAhorcadoREINICIAR.place(x=250, y=460)
    botonAhorcadoREINICIAR.configure(state="disabled")
    #texto gano perdio
    tectPerdAhorcado = tk.Label(ventana_ahorcado, text="",
    bg="white", fg="black", font='Helvetica 16 bold', relief="flat")
    tectPerdAhorcado.place(x=20, y=200)  
    center(ventana_ahorcado)  # centrar ventana
    ventana_ahorcado.mainloop()


def ventana_tic():
    global ventana_Principal, ventana_selección, p1, p2, pa, playerb, buttons, flag, bclick
    p1 = tk.StringVar()
    p2 = tk.StringVar()
    pa = tk.StringVar()
    playerb = tk.StringVar()

    def disableButton():
        button1.configure(state="disabled")
        button2.configure(state="disabled")
        button3.configure(state="disabled")
        button4.configure(state="disabled")
        button5.configure(state="disabled")
        button6.configure(state="disabled")
        button7.configure(state="disabled")
        button8.configure(state="disabled")
        button9.configure(state="disabled")

    def enabledButton():
        button1.configure(state="normal")
        button2.configure(state="normal")
        button3.configure(state="normal")
        button4.configure(state="normal")
        button5.configure(state="normal")
        button6.configure(state="normal")
        button7.configure(state="normal")
        button8.configure(state="normal")
        button9.configure(state="normal")

    def btnClick(buttons):
        global bclick, flag, player2_name, player1_name, playerb, pa
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            label["text"] = "Player X:"
            label2["text"] = "Player O: -"
            bclick = False
            playerb = p2.get() + " Wins!"
            pa = p1.get() + " Wins!"
            checkForWin()
            flag += 1

        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            label["text"] = "Player X: -"
            label2["text"] = "Player O:"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tk.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    def checkForWin():
        global flag
        if(flag == 8):
            tk.messagebox.showinfo("Tic-Tac-Toe", "empate!")
            disableButton()
        elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
              button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
              button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
              button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
              button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
              button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
              button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
              button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
              button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
              button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
            label["text"] = "Player X:"
            label2["text"] = "Player O:"
            disableButton()
            tk.messagebox.showinfo("Tic-Tac-Toe", pa)

        elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
              button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
              button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
              button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
              button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
              button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
              button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
              button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
              button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
              button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'):
            label["text"] = "Player X:"
            label2["text"] = "Player O:"
            disableButton()
            tk.messagebox.showinfo("Tic-Tac-Toe", playerb)

    def reiniciar():
        global buttons, flag, bclick
        bclick = True
        flag = 0
        for i in range(len(buttons)):
            buttons[i]["text"] = " "
        label["text"] = "Player X: -"
        label2["text"] = "Player O:"
        enabledButton()

    def salir():
        reiniciar()
        ventana_tic.withdraw()
        ventana_selección.deiconify()

    # quito ventana seleccion
    ventana_selección.withdraw()
    # crea ventana y se le hacen configuraciones
    ventana_tic = tk.Toplevel()
    ventana_tic.title("Bienvenido")
    ventana_tic.configure(background="black")
    ventana_tic.geometry("410x500")
    ventana_tic.resizable(width=False, height=False)  # no se podra grandar

    bit = ventana_tic.iconbitmap('icono.ico')  # icono

    # elementos
    label = tk.Label(ventana_tic, text="Player X: -",
                     font='Times 13 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)
    label2 = tk.Label(ventana_tic, text="Player O:",
                      font='Times 13 bold', bg='white', fg='black', height=1, width=8)
    label2.grid(row=2, column=0)
    player1_name = tk.Entry(ventana_tic, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=1)
    player2_name = tk.Entry(ventana_tic, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=1)
    center(ventana_tic)  # centrar ventana

    buttonReiniTic = tk.Button(ventana_tic, text="Reiniciar", font='Times 10 bold',
                               bg='blue', fg='white', height=1, width=1, command=lambda: reiniciar())
    buttonReiniTic.grid(row=1, column=2, columnspan=1,
                        rowspan=1, sticky="wens", padx=5, pady=5)
    buttonReiniTic = tk.Button(ventana_tic, text="Salir", font='Times 10 bold',
                               bg='red', fg='white', height=1, width=1, command=lambda: salir())
    buttonReiniTic.grid(row=2, column=2, columnspan=1,
                        rowspan=1, sticky="wens", padx=5, pady=5)

    # cajas

    button1 = tk.Button(ventana_tic, text=" ", font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)
    buttons.append(button1)

    button2 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)
    buttons.append(button2)

    button3 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)
    buttons.append(button3)

    button4 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)
    buttons.append(button4)

    button5 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)
    buttons.append(button5)

    button6 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)
    buttons.append(button6)

    button7 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)
    buttons.append(button7)

    button8 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)
    buttons.append(button8)

    button9 = tk.Button(ventana_tic, text=' ', font='Times 20 bold', bg='white',
                        fg='black', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)
    buttons.append(button9)

    ventana_tic.mainloop()

# funcion que optimza y centra la ventana del programa a la ventana del computador


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


ventana_Principal()
