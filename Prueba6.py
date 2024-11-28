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
    MostrarCanvas(canvas, Cerrar, Mini, Sistema, Logo, Subtitulo1, Subtitulo2, Subtitulo3, Subtitulo4, Subtitulo5, Subtitulo6, Subtitulo7, Subtitulo8, Subtitulo9, Subtitulo10, Calendario)

    # coordenadas de los botones de cerrar y minimizar
    canvas.coords(Cerrar, Ancho - 20, 20)
    canvas.coords(Mini, Ancho - 45, 15)
    #canvas.coords(Limpiar, Ancho - 45, 50)

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
    global ancho, alto
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

def cargar_imagen():
    # Abrir un cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar imagen del producto",filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    # Si se selecciona un archivo, actualizar el cuadro de texto
    if ruta_archivo:
        cuadro_texto.config(state="normal")
        #cuadro_texto.delete(0, tk.END)  # Limpiar el cuadro de texto
        cuadro_texto.insert(0, ruta_archivo)  # Insertar la ruta del archivo
        cuadro_texto.config(state="readonly")
        mostrar_miniatura(ruta_archivo)

def mostrar_miniatura(ruta_archivo):
    # Mostrar la etiqueta solo si hay una imagen
    etiqueta_miniatura.place(x=ancho/1.18,y=alto/2.2) 
    # Abrir la imagen y crear una miniatura
    imagen = Image.open(ruta_archivo)
    imagen.thumbnail((80, 80))  # Cambiar el tamaño a 80x80 píxeles
    miniatura = ImageTk.PhotoImage(imagen)

    # Actualizar la etiqueta con la miniatura
    etiqueta_miniatura.config(image=miniatura)
    etiqueta_miniatura.image = miniatura  # Mantener una referencia a la imagen

def show_calendar(event):
    cal.place(x=ancho/2.2, y=alto/1.45)

def select_date(event):
    selected_date_str = cal.get_date()
    cuadro_texto2.config(state='normal')
    cuadro_texto2.delete(0, tk.END)
    cuadro_texto2.insert(0, selected_date_str)
    cuadro_texto2.config(state='readonly')
    cal.place_forget()

def limpiar_campos():
    # Limpiar los campos de entrada
    Codigo.delete(0, tk.END)
    Color.delete(0, tk.END)
    Serial.delete(0, tk.END)
    cuadro_texto.config(state='normal')
    cuadro_texto.delete(0, tk.END)
    cuadro_texto.config(state='readonly')
    
    # Limpiar los combobox
    Lista.set('')
    Lista2.set('')
    Lista3.set('')
    Lista4.set('')

    # Si tienes un Entry para mostrar la fecha seleccionada, también lo puedes limpiar
    cuadro_texto2.config(state='normal')
    cuadro_texto2.delete(0, tk.END)
    cuadro_texto2.config(state='readonly')

    # Limpiar la etiqueta de la imagen
    etiqueta_miniatura.config(image=None)
    etiqueta_miniatura.image = None  # Eliminar la referencia a la imagen
    etiqueta_miniatura.place_forget()  # Ocultar la etiqueta

ventanaP = tk.Tk()
ventanaP.title("Mi Prueba de Ventana personalizada")
anchoRe=0.8
altoRe=0.8
centrar_pan(ventanaP,anchoRe, altoRe)
ventanaP.resizable(False,False)
ventanaP.overrideredirect(True)

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
Logo= canvas.create_image(ancho/24,alto/18,image=AdaptarLogo, anchor="nw")

#Crear titulo del sistema
Sistema= canvas.create_text(ancho/13, alto/4.2,text="SISTEMA DE \nINVENTARIO PARA \nBIENES NACIONALES \n(SIBIN)",fill="white", font=("arial", 13, "bold"), justify='center')
#Crear los sub-titulos
Subtitulo1= canvas.create_text(ancho/4,alto/3.5,text="CODIGO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo2= canvas.create_text(ancho/2,alto/3.5,text="CANTIDAD: ",fill="white", font=("arial", 18, "bold"))
Subtitulo3= canvas.create_text(ancho/1.4,alto/3.5,text="MARCA: ",fill="white", font=("arial", 18, "bold"))
Subtitulo4= canvas.create_text(ancho/4,alto/2.5,text="PRODUCTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo5= canvas.create_text(ancho/1.7,alto/2.5,text="COLOR: ",fill="white", font=("arial", 18, "bold"))
Subtitulo6= canvas.create_text(ancho/4,alto/1.9,text="SERIAL: ",fill="white", font=("arial", 18, "bold"))
Subtitulo7= canvas.create_text(ancho/1.9,alto/1.9,text="FOTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo8= canvas.create_text(ancho/4,alto/1.5,text="FECHA DE \nREGISTRO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo9= canvas.create_text(ancho/1.7,alto/1.5,text="CATEGORIA: ",fill="white", font=("arial", 18, "bold"))
Subtitulo10= canvas.create_text(ancho/2,alto/13,text="REGISTRO DE BIENES NACIONALES",fill="white", font=("arial", 24, "bold"))

#Crear los campos de texto, mediante llamado a la función "CrearCuadroText"
#Producto =CrearCuadroTxt(Anchoya/5,Altoya/3, 33)
Codigo=CrearCuadroTxt(ancho/3.4,alto/3.7,15)
Color=CrearCuadroTxt(ancho/1.58,alto/2.6,15)
Serial=CrearCuadroTxt(ancho/3.4,alto/1.958,15)

# Crear lista desplegable de la marca y la cantidad
opcionesCantidad=list(range(1,101))
estilo = ttk.Style()
estilo.theme_use('clam')
Lista=ttk.Combobox(canvas,values=opcionesCantidad, font=("Arial", 18), width=8, state="readonly")
Lista.place(x=ancho/1.8, y=alto/3.75)
opcionesMarcas=["VIT", "HP", "CANON", "LG"]
Lista2=ttk.Combobox(canvas,values=opcionesMarcas,  font=("Arial", 18), width=12, state="readonly")
Lista2.place(x=ancho/1.32, y=alto/3.75)
opciones_Categoria=("Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5")
Lista3=ttk.Combobox(canvas, values=opciones_Categoria,  font=("Arial", 18), width=16, state="readonly")
Lista3.place(x=ancho/1.53, y=alto/1.545)
opciones_Producto=("Computadora", "Laptop", "Escritorio", "Silla", "Televisor")
Lista4=ttk.Combobox(canvas, values=opciones_Producto,  font=("Arial", 18), width=16, state="readonly")
Lista4.place(x=ancho/3.25, y=alto/2.62)

# Crear un cuadro de texto
cuadro_texto = tk.Entry(canvas, width=35, font=("Arial",10))
cuadro_texto.place(x=ancho/1.77,y=alto/1.958, height=30)  # Añadir un poco de espacio vertical
cuadro_texto.config(state="readonly")
# Crear un botón para cargar la imagen
boton_cargar = tk.Button(canvas, text="Cargar Imagen", command=cargar_imagen, width=14, bg="red4",  fg="white", font=("Arial", 14), cursor="hand2", relief="raised", border=5)
boton_cargar.place(x=ancho/1.367,y=alto/1.97, height=38)  # Añadir un poco de espacio vertical
# Crear una etiqueta para mostrar la miniatura
etiqueta_miniatura = tk.Label(ventanaP, height=80, width=80, bg="gray71")

# Crear un cuadro de texto
cuadro_texto2 = tk.Entry(canvas, width=18, font=("Arial",16))
cuadro_texto2.place(x=ancho/3.29,y=alto/1.54, height=30)  # Añadir un 
cuadro_texto2.config(state="readonly")
#Cargar imagen de calendario y redimensionarla para mostrar
Cargar_Cal=Image.open("Calendario.png")
RedimensionarCal= Cargar_Cal.resize((45,45), Image.LANCZOS)
AdaptarCal= ImageTk.PhotoImage(RedimensionarCal)
Calendario= canvas.create_image(ancho/2.2,alto/1.559,image=AdaptarCal, anchor="nw")
#  Crea un calendario
#hoy= datetime.today()
#maximo= hoy.replace(year=hoy.year + 5)
cal = Calendar(canvas, selectmode='day', year=2024, month=11, day=1, date_pattern="dd/mm/yyy", cursor="hand2")
canvas.tag_bind(Calendario, "<Button-1>", show_calendar)
cal.bind("<<CalendarSelected>>", select_date)

#Crea un boton que limpia las casillas de la ventana
Limpiar= tk.Button(canvas, text="Limpiar", command=limpiar_campos, width=14, bg="red4",  fg="white", font=("Arial", 16), cursor="hand2", relief="raised", border=5)
Limpiar.place(x=ancho/1.5, y=alto/1.2, height=40)

def mostrar_agregado():
    MensajeExitoso.place(x=ancho/2.15, y=alto/1.195)
    ventanaP.after(1500, ocultar_etiqueta)

def ocultar_etiqueta():
    MensajeExitoso.place_forget()

#Crea un boton que agregue la informacion de las casillas
Agregar= tk.Button(canvas, text="Agregar", command=mostrar_agregado, width=14, bg="red4",  fg="white", font=("Arial", 16), cursor="hand2", border=5, relief="raised")
Agregar.place(x=ancho/1.25, y=alto/1.2, height=40)
# Crear el mensaje del guardado con exito
MensajeExitoso= tk.Label(canvas, text="Se ha agregado correctamente", font=("Arial", 14), bg="thistle1", border=5, width=25)

ventanaP.mainloop()