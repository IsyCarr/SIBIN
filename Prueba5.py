import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import ttk, filedialog
from tkcalendar import Calendar
from datetime import  datetime, timedelta


def MostrarCanvas(canvas, *elementos):
    for elemento in elementos:
        canvas.tag_raise(elemento)

def CambiarTamano(event):
    Ancho = ventanaP.winfo_width()
    Alto = ventanaP.winfo_height()
    
    Redimensionar = Tamano.resize((Ancho, Alto), Image.LANCZOS)
    Fondo = ImageTk.PhotoImage(Redimensionar)
    canvas.create_image(0, 0, image=Fondo, anchor=tk.NW)
    canvas.image = Fondo  # Guardamos la referencia de la imagen para evitar que se borre

    #Mostrar elementos en el canvas
    MostrarCanvas(canvas, Cerrar, Mini,Logo, linea, Degradado, Degradado2,Degradado3,Degradado4, Degradado5,
                  Degradado6, Sistema, Subtitulo1, Subtitulo2,Subtitulo3,Subtitulo4, Subtitulo5,Subtitulo6, Subtitulo7,Subtitulo8,Subtitulo9, 
                    Calendario)
    
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
    #canvas.create_window(ejeX, ejeY, window=Ingreso, height= 30)
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
    etiqueta_miniatura.place(x=1540, y=425) 
    # Abrir la imagen y crear una miniatura
    imagen = Image.open(ruta_archivo)
    imagen.thumbnail((80, 80))  # Cambiar el tamaño a 80x80 píxeles
    miniatura = ImageTk.PhotoImage(imagen)

    # Actualizar la etiqueta con la miniatura
    etiqueta_miniatura.config(image=miniatura)
    etiqueta_miniatura.image = miniatura  # Mantener una referencia a la imagen
    #canvas.create_image(1200, 800,  image=miniatura)

def show_calendar(event):
    cal.place(x=928, y=590+40)

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
    Producto.delete(0, tk.END)
    Color.delete(0, tk.END)
    Serial.delete(0, tk.END)
    cuadro_texto.config(state='normal')
    cuadro_texto.delete(0, tk.END)
    cuadro_texto.config(state='readonly')
    
    # Limpiar los combobox
    Lista.set('')
    Lista2.set('')
    Lista3.set('')

    # Limpiar el campo de fecha del calendario
    #cal.selection_clear()  # Esto no es necesario si solo se quiere limpiar el Entry asociado

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
anchoRe=0.9
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

# Ejemplo de widgets dentro del Frame 
#btn = tk.Button(ventanaP, text="Codigo") 
#canvas.create_window(100,100,window=btn)

linea=canvas.create_line(330,0,330,1000, fill="white", width=2, dash=(9,3))

text_photo4 = crear_text_image(24)
text_photo5 = crear_text_image(22)
text_photo6 = crear_text_image(20)
text_photo7 = crear_text_image(18)
text_photo8 = crear_text_image(16)
text_photo9 = crear_text_image(14)
Degradado = canvas.create_image(318, 0, anchor="nw", image=text_photo4)
Degradado2 = canvas.create_image(319, 0, anchor="nw", image=text_photo5)
Degradado3 = canvas.create_image(320, 0, anchor="nw", image=text_photo6)
Degradado4 = canvas.create_image(321, 0, anchor="nw", image=text_photo7)
Degradado5 = canvas.create_image(322, 0, anchor="nw", image=text_photo8)
Degradado6 = canvas.create_image(323, 0, anchor="nw", image=text_photo9)

#Cargar imagen de logo y redimensionarla para mostrar
Cargar_Logo=Image.open("Logo.jpg")
RedimensionarLogo= Cargar_Logo.resize((100,100), Image.LANCZOS)
AdaptarLogo= ImageTk.PhotoImage(RedimensionarLogo)
Logo= canvas.create_image(30,30,image=AdaptarLogo, anchor="nw")

#Crear titulo del sistema
Sistema= canvas.create_text(230,80,text="SISTEMA DE \nINVENTARIO PARA \nBIENES NACIONALES \n(SIBIN)",fill="white", font=("arial", 13, "bold"), justify='center')
#Crear los sub-titulos
Subtitulo1= canvas.create_text(550,250,text="CODIGO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo2= canvas.create_text(1000,250,text="CANTIDAD: ",fill="white", font=("arial", 18, "bold"))
Subtitulo3= canvas.create_text(1370,250,text="MARCA: ",fill="white", font=("arial", 18, "bold"))
Subtitulo4= canvas.create_text(550,370,text="PRODUCTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo5= canvas.create_text(1100,370,text="COLOR: ",fill="white", font=("arial", 18, "bold"))
Subtitulo6= canvas.create_text(550,490,text="SERIAL: ",fill="white", font=("arial", 18, "bold"))
Subtitulo7= canvas.create_text(1050,490,text="FOTO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo8= canvas.create_text(550,610,text="FECHA DE \nREGISTRO: ",fill="white", font=("arial", 18, "bold"))
Subtitulo9= canvas.create_text(1150,610,text="CATEGORIA: ",fill="white", font=("arial", 18, "bold"))

#Crear los campos de texto, mediante llamado a la función "CrearCuadroText"
Producto =CrearCuadroTxt(653,355, 33)
Codigo=CrearCuadroTxt(630,235,24)
Color=CrearCuadroTxt(1175,355,25)
Serial=CrearCuadroTxt(620,475,30)

# Crear lista desplegable de la marca y la cantidad
opcionesCantidad=list(range(1,101))
estilo = ttk.Style()
estilo.theme_use('clam')
Lista=ttk.Combobox(canvas,values=opcionesCantidad,  font=("Arial", 18), width=12, state="readonly")
Lista.place(x=1100, y=235)
opcionesMarcas=["VIT", "HP", "CANON", "LG"]
Lista2=ttk.Combobox(canvas,values=opcionesMarcas,  font=("Arial", 18), width=12, state="readonly")
Lista2.place(x=1450, y=235)
opciones_Categoria=("Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5")
Lista3=ttk.Combobox(canvas, values=opciones_Categoria,  font=("Arial", 18), width=16, state="readonly")
Lista3.place(x=1250, y=595)


# Crear un cuadro de texto
cuadro_texto = tk.Entry(canvas, width=35, font=("Arial",10))
cuadro_texto.place(x=1110, y=475, height=30)  # Añadir un poco de espacio vertical
cuadro_texto.config(state="readonly")
# Crear un botón para cargar la imagen
boton_cargar = tk.Button(canvas, text="Cargar Imagen", command=cargar_imagen, width=14, bg="red4",  fg="white", font=("Arial", 14), cursor="hand2", relief="sunken", border=5)
boton_cargar.place(x=1360, y=471, height=38)  # Añadir un poco de espacio vertical
# Crear una etiqueta para mostrar la miniatura
etiqueta_miniatura = tk.Label(ventanaP, height=80, width=80, bg="gray71")


#Ingreso=tk.Entry(width=45)
#canvas.create_window(750, 250, window=Ingreso, height= 28)
#canvas.create_window(950, 250, window=Ingreso, height= 28)

# Crear un cuadro de texto
cuadro_texto2 = tk.Entry(canvas, width=23, font=("Arial",16))
cuadro_texto2.place(x=635, y=595, height=30)  # Añadir un 
cuadro_texto2.config(state="readonly")
#Cargar imagen de calendario y redimensionarla para mostrar
Cargar_Cal=Image.open("Calendario.png")
RedimensionarCal= Cargar_Cal.resize((45,45), Image.LANCZOS)
AdaptarCal= ImageTk.PhotoImage(RedimensionarCal)
Calendario= canvas.create_image(928,588,image=AdaptarCal, anchor="nw")
#  Crea un calendario
#hoy= datetime.today()
#maximo= hoy.replace(year=hoy.year + 5)
cal = Calendar(canvas, selectmode='day', year=2024, month=11, day=1, date_pattern="dd/mm/yyy", cursor="hand2")
canvas.tag_bind(Calendario, "<Button-1>", show_calendar)
cal.bind("<<CalendarSelected>>", select_date)

#Crea un boton quwe limpia las casillas de la ventana
Limpiar= tk.Button(canvas, text="Limpiar", command=limpiar_campos, width=14, bg="red4",  fg="white", font=("Arial", 16), cursor="hand2", relief="sunken", border=5)
Limpiar.place(x=1200, y=720, height=40)



ventanaP.mainloop()

