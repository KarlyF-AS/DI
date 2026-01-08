from reportlab.pdfgen import canvas

folla = canvas.Canvas ("primeiroDocumento.pdf")
folla.drawString (0,0, "Posición inicio (x,y) = (0,0)")
folla.drawString (50, 100, "Posición (x,y) = (50,100)")
folla.drawString (150, 20, "Posición (x,y) = (150,20)")

folla.drawImage("zanka.webp", 50, 250, 300, 300)

folla.showPage()
folla.save()