import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

class RoundedRectangleDrawer:
    def __init__(self, canvas, xy, radius, outline, width=300, height=200, line_width=1, position=(0, 0)):
        self.canvas = canvas
        self.xy = xy
        self.radius = radius
        self.outline = outline
        self.width = width
        self.height = height
        self.line_width = line_width
        self.position = position  # Nueva propiedad para la posición
        self.img = Image.new('RGBA', (self.width, self.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.img)
        self.img_tk = None
        self.image_id = None  # ID del objeto de imagen en el canvas

    def draw_rounded_rectangle_outline(self):
        
        x1, y1, x2, y2 = self.xy

        # Dibujar las cuatro esquinas redondeadas
        self.draw.arc([x1, y1, x1 + 2 * self.radius, y1 + 2 * self.radius], 180, 270, fill=self.outline, width=self.line_width)
        self.draw.arc([x2 - 2 * self.radius, y1, x2, y1 + 2 * self.radius], 270, 360, fill=self.outline, width=self.line_width)
        self.draw.arc([x1, y2 - 2 * self.radius, x1 + 2 * self.radius, y2], 90, 180, fill=self.outline, width=self.line_width)
        self.draw.arc([x2 - 2 * self.radius, y2 - 2 * self.radius, x2, y2], 0, 90, fill=self.outline, width=self.line_width)

        # Dibujar los lados del rectángulo
        self.draw.line([x1 + self.radius, y1, x2 - self.radius, y1], fill=self.outline, width=self.line_width)  # Línea superior
        self.draw.line([x1 + self.radius, y2, x2 - self.radius, y2], fill=self.outline, width=self.line_width)  # Línea inferior
        self.draw.line([x1, y1 + self.radius, x1, y2 - self.radius], fill=self.outline, width=self.line_width)  # Línea izquierda
        self.draw.line([x2, y1 + self.radius, x2, y2 - self.radius], fill=self.outline, width=self.line_width)  # Línea derecha

    def display_on_canvas(self):
        self.draw_rounded_rectangle_outline()
        self.img_tk = ImageTk.PhotoImage(self.img)
        # Crear la imagen en el canvas y guardar el ID
        self.image_id = self.canvas.create_image(self.position[0], self.position[1], anchor="nw", image=self.img_tk)

    def update_color(self, new_color):
        self.outline = new_color  # Actualizar el color del contorno
        self.img = Image.new('RGBA', (self.width, self.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.img)
        self.draw_rounded_rectangle_outline()
        self.img_tk = ImageTk.PhotoImage(self.img)
        # Actualizar la imagen en el canvas
        if self.image_id is not None:
            self.canvas.itemconfig(self.image_id, image=self.img_tk)