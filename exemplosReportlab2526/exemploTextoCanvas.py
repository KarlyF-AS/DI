import texto
from reportlab.pdfgen import canvas

text = ('Este texto é para exemplo', 'da utilizacion de canvas', 'para usar con texto.')

obxCanvas = canvas.Canvas("textoCanvas.pdf")

obxTexto = obxCanvas.beginText()
obxTexto.setTextOrigin(100,500)
obxTexto.setFont("Courier", 16)

for linha in text:
    obxTexto.textLine(linha)

obxTexto.setFillGray(0.5)
textoLongo = """Outro texto con varias
                liñas incorporadas,
                con rertornos de carro
                incluídos."""
obxTexto.textLines(textoLongo)

obxTexto.setTextOrigin(20, 800)
for tipo_letra in obxCanvas.getAvailableFonts():
    obxTexto.setFont(tipo_letra, 16)
    obxTexto.textLine("Texto de exemplo coa fonte: " + tipo_letra)

obxTexto.setFillColorRGB(0.2,0,0.6)
obxTexto.setFont("Helvetica", 18)
for linha in text:
    obxTexto.moveCursor(20,15)
    obxTexto.textOut(linha)


obxCanvas.drawText(obxTexto)

obxCanvas.showPage()
obxCanvas.save()