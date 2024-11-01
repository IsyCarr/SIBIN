import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

def MostrarCanvas(canvas, *elementos):
    for elemento in elementos:
        canvas.tag_raise(elemento)

def CambiarTamano(event):
    Ancho = ventanaP.winfo_width()
    Alto = ventanaP.winfo_height()
    
    Redimensionar = Tamano.resize((Ancho, Alto), Image.LANCZOS)
    Fondo = ImageTk.PhotoImage(Redimensionar)
    canvas.create_image(0, 0, image=Fondo, anchor=tk.NW)
    canvas.image_fondo = Fondo  # Guardamos la referencia de la imagen para evitar que se borre

    """
    #Metodo para sobreescribir encima del canvas"
    canvas.tag_raise (Cerrar) 
    canvas.tag_raise (Mini) 
    #canvas.tag_raise(Codigo)
    canvas.tag_raise(linea)
    canvas.tag_raise(Degradado)
    canvas.tag_raise(Degradado2)
    canvas.tag_raise(Degradado3)
    canvas.tag_raise(Degradado4)
    canvas.tag_raise(Degradado5)
    canvas.tag_raise(Degradado6)
    #canvas.tag_raise(Logo)
    """
    #Mostrar elementos  en el canvas
    MostrarCanvas(canvas, Cerrar, Mini, linea, Degradado, Degradado2, Degradado3, Degradado4,Degradado5,Degradado6,Logo)

    # coordenadas de los botones de cerrar y minimizar
    canvas.coords(Cerrar, Ancho - 30, 10)
    canvas.coords(Mini, Ancho - 55, 5)

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

# Crear imagen de texto "X" para el botón de cerrar
text_image = Image.new("RGBA", (20, 50), (255, 0, 0, 0))
draw = ImageDraw.Draw(text_image)
font = ImageFont.truetype("arialbd.ttf", 20)
draw.text((5, 0), "X", font=font, fill=(255, 255, 255, 255))
text_photo = ImageTk.PhotoImage(text_image)
Cerrar = canvas.create_image(0, 0, anchor="nw", image=text_photo)
# Vincular la acción de cerrar ventana al hacer clic en la "X"
canvas.tag_bind(Cerrar, "<Button-1>", cerrarVen)

# Crear imagen de texto "-" para el botón de minimizar
text_image2 = Image.new("RGBA", (20, 50), (255, 0, 0, 0))
draw2 = ImageDraw.Draw(text_image2)
draw2.text((5, 0), "_", font=font, fill=(255, 255, 255, 255))
text_photo2 = ImageTk.PhotoImage(text_image2)
Mini = canvas.create_image(0, 0, anchor="nw", image=text_photo2)
# Vincular la acción de cerrar ventana al hacer clic en la "-"
canvas.tag_bind(Mini, "<Button-1>", miniVen)


ventanaP.bind("<Configure>", CambiarTamano)
ventanaP.bind("<Map>", on_state_change)
ventanaP.bind("<Unmap>", on_state_change)

# Ejemplo de widgets dentro del Frame 
#btn = tk.Button(ventanaP, text="Codigo") 
#canvas.create_window(100,100,window=btn)

linea=canvas.create_line(330,0,330,1000, fill="white", width=2, dash=(9,3))

"""
text_image4 = Image.new("RGBA", (24, 1900), (255, 112, 0, 10))
text_photo4 = ImageTk.PhotoImage(text_image4)
Degradado = canvas.create_image(318, 0, anchor="nw", image=text_photo4)

text_image5 = Image.new("RGBA", (22, 1900), (255, 112, 0, 10))
text_photo5 = ImageTk.PhotoImage(text_image5)
Degradado2 = canvas.create_image(319, 0, anchor="nw", image=text_photo5)

text_image6 = Image.new("RGBA", (20, 1900), (255, 112, 0, 10))
text_photo6 = ImageTk.PhotoImage(text_image6)
Degradado3 = canvas.create_image(320, 0, anchor="nw", image=text_photo6)

text_image7 = Image.new("RGBA", (18, 1900), (255, 112, 0, 10))
text_photo7 = ImageTk.PhotoImage(text_image7)
Degradado4 = canvas.create_image(321, 0, anchor="nw", image=text_photo7)

text_image8 = Image.new("RGBA", (16, 1900), (255, 112, 0, 10))
text_photo8 = ImageTk.PhotoImage(text_image8)
Degradado5 = canvas.create_image(322, 0, anchor="nw", image=text_photo8)

text_image9 = Image.new("RGBA", (14, 1900), (255, 112, 0, 10))
text_photo9 = ImageTk.PhotoImage(text_image9)
Degradado6 = canvas.create_image(323, 0, anchor="nw", image=text_photo9)
"""
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

Cargar_Logo=Image.open("Logo.jpg")
RedimensionarLogo= Cargar_Logo.resize((100,100), Image.LANCZOS)
AdaptarLogo= ImageTk.PhotoImage(RedimensionarLogo)
Logo= canvas.create_image(30,30,image=AdaptarLogo, anchor="nw")

"""
# Crear imagen de texto codigo
Imgtxt = Image.new("RGBA", (100, 50), (255, 0, 0, 0))
draw3 = ImageDraw.Draw(Imgtxt)
font3 = ImageFont.truetype("arialbd.ttf", 16)
draw3.text((5, 0), "Codigo", font=font3, fill=(255, 255, 255, 255))
Fototxt = ImageTk.PhotoImage(Imgtxt)
Codigo = canvas.create_image(300, 300, anchor="nw", image=Fototxt)
"""

ventanaP.mainloop()
