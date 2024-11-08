import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

def CambiarTamano(event): 
    Ancho= event.width  #obtiene el ancho de la ventana
    Alto=event.height   #obtiene el alto de la ventana

    #Redimensionar la imagen
    Redimensionar=Tamano.resize((Ancho,Alto), Image.LANCZOS)  #redimensiona la imagen
    #Crear una imagen PhotoImage y mostrarla en el canvas
    Fondo=ImageTk.PhotoImage(Redimensionar)
    canvas.create_image(0,0, image=Fondo, anchor=tk.NW)
    canvas.image = Fondo

def cerrarVen(event):
    ventanaP.destroy()  

ventanaP = tk.Tk()
ventanaP.title ("Mi Prueba de Ventana personalizada")
ventanaP.geometry("300x500")

Tamano=Image.open("Fondo.png")
canvas=tk.Canvas(ventanaP)

Fondo=ImageTk.PhotoImage(Tamano)
canvas.create_image(0,0,image=Fondo, anchor=tk.NW)

ventanaP.bind("<Configure>", CambiarTamano)

width,height=20,20
img=Image.new('RGBA',(width,height),(255,255,255,0))
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("arial.ttf",16)
draw.text((10,10),"X", font=font, fill=(255,255,255,255))
Foto=ImageTk.PhotoImage(img)
Alfin=canvas.create_image(300,5,anchor="nw", image=Foto)
canvas.tag_bind(Alfin, "<Button-1>", cerrarVen)
canvas.pack(fill=tk.BOTH, expand=True)

ventanaP.mainloop()