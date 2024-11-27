import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import ttk, filedialog,  Menu
from tkcalendar import Calendar
from datetime import  datetime, timedelta
from rounded_rectangle_drawer import RoundedRectangleDrawer



def MostrarCanvas(canvas, *elementos):
    for elemento in elementos:
        canvas.tag_raise(elemento)

def CambiarTamano(event):
    Ancho = ventanaP.winfo_width()
    Alto = ventanaP.winfo_height()
    #global Fondo
    Redimensionar = Tamano.resize((Ancho, Alto), Image.LANCZOS)
    Fondo = ImageTk.PhotoImage(Redimensionar)
    canvas.create_image(0, 0, image=Fondo, anchor=tk.NW)
    canvas.image = Fondo  # Guardamos la referencia de la imagen para evitar que se borre
    
    #Mostrar elementos en el canvas
    MostrarCanvas(canvas, Cerrar, Mini, Sistema, Logo, Subtitulo1, Subtitulo2, Subtitulo3, Subtitulo4, Subtitulo5, Subtitulo6, Subtitulo7, Subtitulo8, Subtitulo9, Subtitulo10)

    # coordenadas de los botones de cerrar y minimizar
    canvas.coords(Cerrar, Ancho - 20, 20)
    canvas.coords(Mini, Ancho - 45, 15)

def cerrarVen(event):
    ventanaP.destroy()

def miniVen(event):
    ventanaP.iconify()

def Maximizar(event):
    ventanaP.overrideredirect(True)

def centrar_pan(ventanaP, anchoRe, altoRe):
    #Obtener las dimensiones de la pantalla
    panancho = ventanaP.winfo_screenwidth()
    panalto = ventanaP.winfo_screenheight()
    # Calcular las dimensiones de la ventana
    ancho = int(panancho * anchoRe)
    alto = int(panalto * altoRe)
    # Calcular la posición x, y para centrar la ventana
    x = (panancho // 2) - (ancho // 2)
    y = (panalto // 2) - (alto // 2)

    # Establecer el tamaño y la posición de la ventana
    ventanaP.geometry(f"{ancho}x{alto}+{x}+{y}")

def miniVen(event):
    ventanaP.overrideredirect(False)
    ventanaP.iconify()

def on_state_change(event):
    if ventanaP.wm_state() == 'normal':
        ventanaP.overrideredirect(True)

def crear_text_image(width):
    text_image = Image.new("RGBA", (width, 1900), (255, 112, 0, 10))
    return ImageTk.PhotoImage(text_image)

def CrearCuadroTxt (ejeX, ejeY, ancho):
    #Crear un cuadro de texto para ingresar datos
    Ingreso=tk.Entry(width=ancho, font=("Arial", 14))
    Ingreso.place(x=ejeX, y=ejeY, height=30)
    return Ingreso

ventanaP = tk.Tk()
ventanaP.title("Mi Prueba de Ventana personalizada")
anchoRe=0.8
altoRe=0.8
centrar_pan(ventanaP,anchoRe, altoRe)
ventanaP.resizable(False,False)
ventanaP.overrideredirect(True)

Anchoya = ventanaP.winfo_screenwidth()
Altoya = ventanaP.winfo_screenheight()
Tamano = Image.open("Fondo.png")
canvas = tk.Canvas(ventanaP, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

#Crear un texto "X" para el boton de cerrar
Cerrar= canvas.create_text(0,0,text="X",fill="white", font=("arial", 14, "bold"))
canvas.tag_bind(Cerrar, "<Button-1>", cerrarVen) # Vincular la acción de cerrar ventana al hacer clic en la "X"
#Crear un texto "-" para el boton de minimizar
Mini = canvas.create_text(0,0,text="_",fill="white", font=("arial", 14, "bold"))
canvas.tag_bind(Mini, "<Button-1>", miniVen) # Vincular la acción de cerrar ventana al hacer clic en la "-"

ventanaP.bind("<Configure>", CambiarTamano)
ventanaP.bind("<Map>", on_state_change)
ventanaP.bind("<Unmap>", on_state_change)

#Cargar imagen de logo y redimensionarla para mostrar
Cargar_Logo=Image.open("Logo.jpg")
RedimensionarLogo= Cargar_Logo.resize((100,100), Image.LANCZOS)
AdaptarLogo= ImageTk.PhotoImage(RedimensionarLogo)
Logo= canvas.create_image(Anchoya/28,Altoya/25,image=AdaptarLogo, anchor="nw")

#Crear titulo del sistema
Sistema= canvas.create_text(Anchoya/15.5,Altoya/5.5,text="SISTEMA DE \nINVENTARIO PARA \nBIENES NACIONALES \n(SIBIN)",fill="white", font=("arial", 13, "bold"), justify='center')
#Crear los sub-titulos
Subtitulo1= canvas.create_text(Anchoya/5,Altoya/4.5,text="CODIGO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo2= canvas.create_text(Anchoya/2.5,Altoya/4.5,text="CANTIDAD: ",fill="white", font=("arial", 18, "bold"))
Subtitulo3= canvas.create_text(Anchoya/1.65,Altoya/4.5,text="MARCA: ",fill="white", font=("arial", 18, "bold"))
Subtitulo4= canvas.create_text(Anchoya/5,Altoya/3,text="PRODUCTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo5= canvas.create_text(Anchoya/2,Altoya/3,text="COLOR: ",fill="white", font=("arial", 18, "bold"))
Subtitulo6= canvas.create_text(Anchoya/5,Altoya/2.3,text="SERIAL: ",fill="white", font=("arial", 18, "bold"))
Subtitulo7= canvas.create_text(Anchoya/2,Altoya/2.3,text="FOTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo8= canvas.create_text(Anchoya/5,Altoya/1.8,text="FECHA DE \nREGISTRO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo9= canvas.create_text(Anchoya/2,Altoya/1.8,text="CATEGORIA: ",fill="white", font=("arial", 18, "bold"))
Subtitulo10= canvas.create_text(Anchoya/2.5,Altoya/13,text="REGISTRO DE BIENES NACIONALES",fill="white", font=("arial", 24, "bold"))

#Crear los campos de texto, mediante llamado a la función "CrearCuadroText"
#Producto =CrearCuadroTxt(Anchoya/5,Altoya/3, 33)
Codigo=CrearCuadroTxt(Anchoya/4.15,Altoya/4.77,15)
Color=CrearCuadroTxt(Anchoya/1.86,Altoya/3.12,15)
Serial=CrearCuadroTxt(Anchoya/4.18,Altoya/2.368,15)

# Crear lista desplegable de la marca y la cantidad
opcionesCantidad=list(range(1,101))
estilo = ttk.Style()
estilo.theme_use('clam')
Lista=ttk.Combobox(canvas,values=opcionesCantidad, font=("Arial", 18), width=8, state="readonly")
Lista.place(x=Anchoya/2.24, y=Altoya/4.79)
opcionesMarcas=["VIT", "HP", "CANON", "LG"]
Lista2=ttk.Combobox(canvas,values=opcionesMarcas,  font=("Arial", 18), width=12, state="readonly")
Lista2.place(x=Anchoya/1.55, y=Altoya/4.79)
opciones_Categoria=("Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5")
Lista3=ttk.Combobox(canvas, values=opciones_Categoria,  font=("Arial", 18), width=16, state="readonly")
Lista3.place(x=Anchoya/1.8, y=Altoya/1.8)

ventanaP.mainloop()