from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

guion = []
imaxe = Image(50, 250, 300, 250, "rudo.png")

debuxo = Drawing(400,250)
debuxo.add(imaxe)
guion.append(debuxo)

debuxo2 = Drawing()
debuxo2.add(imaxe)
debuxo2.translate(150,350)
guion.append(debuxo2)

debuxo3 = Drawing()
debuxo3.add(imaxe)
debuxo3.rotate(9)
debuxo3.translate(150, 150)
guion.append(debuxo3)

debuxo4 = Drawing()
debuxo4.add(imaxe)
debuxo4.translate(150, 500)
debuxo4.scale(0.5, 0.5)
guion.append(debuxo4)


folla = Drawing (A4[0], A4[1])
for elemento in guion:
    folla.add(elemento)

renderPDF.drawToFile(folla, "exemploConDrawing.pdf", "Documento de exemplo usando Drawing")