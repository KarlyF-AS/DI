from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

guion = []

imagen = Image("800px-Cleffa.png", width=50,height=50)
img = [imagen]
titulo = []
cab = ['Descripción', 'Importe', 'Cantidad', 'Total']
fila1 = ['Producto 1', 'Correr', '-', '-']
fila2 = ['Producto 2', 'Clases', 'Clases', 'Trabajar']
fila3 = ['Producto 3', 'Trabajar', 'Trabajar', 'Trabajar']
fila4 = ['Producto 4', 'Trabajar', 'Trabajar', 'Trabajar']
fila5 = ['Producto 5', 'Trabajar', 'Trabajar', 'Trabajar']
fila6 = ['Producto 6', 'Trabajar', 'Trabajar', 'Trabajar']


tabla = Table ([titulo, cab, fila1, fila2, fila3, fila4, fila5, fila6])
tabla.setStyle([('TEXTCOLOR', (1,-4), (7,-4), colors.white),
                ('TEXTCOLOR', (0,0), (0,3), colors.black),
                ('BACKGROUND', (1,-4), (-1,-4), colors.green),
                ('INNERGRID', (0,1), (-1,-1), 0.25, colors.white),
                ('LINEAFTER', (0,1), (0,-1), 0.25, colors.white),
                ("BOX", (0,0), (-1,-1), 1, colors.white),
                ('SPAN', (0, 0), (-1, 0)),
                ('ALIGN', (0,0), (-1,0), 'CENTER'),
                ])


guion.append(tabla)
doc = SimpleDocTemplate("Factura.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)