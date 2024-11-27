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
    MostrarCanvas(canvas, Home, Cerrar, Mini,Logo, linea, Degradado, Degradado2,Degradado3,Degradado4, Degradado5,
                  Degradado6, Sistema, Subtitulo1, Subtitulo2,Subtitulo3,Subtitulo4, Subtitulo5,Subtitulo6, Subtitulo7,Subtitulo8,Subtitulo9, 
                    Calendario, Subtitulo10, Login, rep, rep1, rep2, rep3, rep4)
    
    drawer.display_on_canvas()
    drawer1.display_on_canvas()
    drawer2.display_on_canvas()
    drawer3.display_on_canvas()
    drawer4.display_on_canvas()

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

#Cargar imagen de home y redimensionarla para mostrar
Cargar_Home=Image.open("Home.png")
RedimensionarHome= Cargar_Home.resize((30,30), Image.LANCZOS)
AdaptarHome= ImageTk.PhotoImage(RedimensionarHome)
Home = canvas.create_image(450,26,image=AdaptarHome, anchor="nw")

#Cargar imagen de Login y redimensionarla para mostrar
Cargar_Login=Image.open("Usuario2.png")
RedimensionarLogin= Cargar_Login.resize((30,30), Image.LANCZOS)
AdaptarLogin= ImageTk.PhotoImage(RedimensionarLogin)
Login= canvas.create_image(1600,20,image=AdaptarLogin, anchor="nw")


# CREAR LISTA DE BOTONES LATERALES

text_image2 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw2 = ImageDraw.Draw(text_image2)
font2 = ImageFont.truetype("arialbd.ttf", 26)
draw2.text((10, 10), "REGISTRO", font=font2, fill=(255, 255, 255, 255), align="center")
text_photo2 = ImageTk.PhotoImage(text_image2)
rep4= canvas.create_image(332, 250, anchor=tk.CENTER, image=text_photo2)

xy = (20, 20, 285, 80)
radius = 10
line_width = 2  # Grosor de la línea
position = (6, 200)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer = RoundedRectangleDrawer(canvas, xy, radius, outline='white', line_width=line_width, position=position)


text_image3 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw3 = ImageDraw.Draw(text_image3)
font3 = ImageFont.truetype("arialbd.ttf", 26)
draw3.text((10, 10), "ASIGNACIÓN", font=font2, fill=(255, 255, 255, 255), align="center")
text_photo3 = ImageTk.PhotoImage(text_image3)
rep3= canvas.create_image(320, 350, anchor=tk.CENTER, image=text_photo3)

xy1 = (20, 20, 285, 80)
radius1 = 10
line_width1 = 2  # Grosor de la línea
position1 = (6, 300)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer1 = RoundedRectangleDrawer(canvas, xy1, radius1, outline='white', line_width=line_width1, position=position1)


text_image4 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw4 = ImageDraw.Draw(text_image4)
font4 = ImageFont.truetype("arialbd.ttf", 26)
draw4.text((10, 10), "CONSULTA", font=font4, fill=(255, 255, 255, 255), align="center")
text_photo4 = ImageTk.PhotoImage(text_image4)
rep2=canvas.create_image(331, 450, anchor=tk.CENTER, image=text_photo4)

xy2 = (20, 20, 285, 80)
radius2 = 10
line_width2 = 2  # Grosor de la línea
position2 = (6, 400)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer2 = RoundedRectangleDrawer(canvas, xy2, radius2, outline='white', line_width=line_width2, position=position2)

text_image20 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw20 = ImageDraw.Draw(text_image20)
font20 = ImageFont.truetype("arialbd.ttf", 24)
draw20.text((10, 10), "DESINCORPORACIÓN", font=font20, fill=(255, 255, 255, 255), align="center")
text_photo20 = ImageTk.PhotoImage(text_image20)
rep1= canvas.create_image(270, 550, anchor=tk.CENTER, image=text_photo20)

xy3 = (20, 20, 285, 80)
radius3 = 10
line_width3 = 2  # Grosor de la línea
position3 = (6, 500)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer3 = RoundedRectangleDrawer(canvas, xy3, radius3, outline='white', line_width=line_width3, position=position3)

text_image21 = Image.new("RGBA", (500, 50), (255, 255, 255, 0))
draw21 = ImageDraw.Draw(text_image21)
font21 = ImageFont.truetype("arialbd.ttf", 26)
draw21.text((10, 10), "REPORTE", font=font21, fill=(255, 255, 255, 255), align="center")
text_photo21 = ImageTk.PhotoImage(text_image21)
rep = canvas.create_image(336, 650, anchor=tk.CENTER, image=text_photo21)

xy4 = (20, 20, 285, 80)
radius4 = 10
line_width4 = 2  # Grosor de la línea
position4 = (6, 600)
# Crear el objeto RoundedRectangleDrawer y dibujar en el canvas
drawer4 = RoundedRectangleDrawer(canvas, xy4, radius4, outline='white', line_width=line_width4, position=position4)


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
Subtitulo10= canvas.create_text(1000,100,text="REGISTRO DE BIENES NACIONALES",fill="white", font=("arial", 24, "bold"))

#Crear los campos de texto, mediante llamado a la función "CrearCuadroText"
Producto =CrearCuadroTxt(653,355, 33)
Codigo=CrearCuadroTxt(630,235,24)
Color=CrearCuadroTxt(1175,355,25)
Serial=CrearCuadroTxt(620,475,30)

# Crear lista desplegable de la marca y la cantidad
opcionesCantidad=list(range(1,101))
estilo = ttk.Style()
estilo.theme_use('clam')
Lista=ttk.Combobox(canvas,values=opcionesCantidad, font=("Arial", 18), width=12, state="readonly")
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
boton_cargar = tk.Button(canvas, text="Cargar Imagen", command=cargar_imagen, width=14, bg="red4",  fg="white", font=("Arial", 14), cursor="hand2", relief="raised", border=5)
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

#Crea un boton que limpia las casillas de la ventana
Limpiar= tk.Button(canvas, text="Limpiar", command=limpiar_campos, width=14, bg="red4",  fg="white", font=("Arial", 16), cursor="hand2", relief="raised", border=5)
Limpiar.place(x=1200, y=720, height=40)

def mostrar_agregado():
    MensajeExitoso.place(x=870, y=725)
    ventanaP.after(1500, ocultar_etiqueta)

def ocultar_etiqueta():
    MensajeExitoso.place_forget()

#Crea un boton que agregue la informacion de las casillas
Limpiar= tk.Button(canvas, text="Agregar", command=mostrar_agregado, width=14, bg="red4",  fg="white", font=("Arial", 16), cursor="hand2", border=5, relief="raised")
Limpiar.place(x=1430, y=720, height=40)
# Crear el mensaje del guardado con exito
MensajeExitoso= tk.Label(canvas, text="Se ha agregado correctamente", font=("Arial", 14), bg="thistle1", border=5, width=25)

#Cargar imagen de candado y redimensionarla para mostrar
Cargar_candado=Image.open("Seguridad.png")
Redimensionarcandado= Cargar_candado.resize((15,15), Image.LANCZOS)
AdaptarCandado= ImageTk.PhotoImage(Redimensionarcandado)
#Cargar imagen de cerrar sesión y redimensionarla para mostrar
Cargar_sesion=Image.open("Cerrar_Sección.png")
Redimensionarsesion= Cargar_sesion.resize((15,15), Image.LANCZOS)
AdaptarSesion= ImageTk.PhotoImage(Redimensionarsesion)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

def on_select(option):
    if option == "Opción 1":
        print("Seleccionaste la uno")
    elif option == "Opción 2":
        print("Seleccionaste la dos")
    else:
        print("Seleccionaste la tres")

menu = Menu(ventanaP, tearoff=0)
menu.add_command(label="Opción 1", command=lambda: on_select("Opción 1"),)
menu.add_command(label="Contraseña", command=lambda: on_select("Opción 2"), image=AdaptarCandado, compound=tk.LEFT)
menu.add_separator()
menu.add_command(image=AdaptarSesion, compound="left", label="Cerrar Sesión", foreground="red")
canvas.tag_bind(Login, "<Button-1>", show_menu) # Vincula el evento de click en el boton de login con la función para mostrar el menú

"""
def menu_Login(event):
    frame.place(x=1600-105, y=60)
    Contrasena= tk.Label (frame, image=AdaptarCandado, text="Cambiar Contraseña", compound="left", cursor="hand2" )
    Contrasena.pack()
    Sesion= tk.Label (frame, image=AdaptarSesion, text="Cerrar Sesión", compound="left", cursor="hand2")
    Sesion.pack()

# Crear un Frame para las opciones
frame = tk.Frame(canvas)

canvas.tag_bind(Login, "<Leave>", lambda event: canvas.delete(menu_Login))
"""





ventanaP.mainloop()

