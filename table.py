from reportlab.lib.pagesizes import landscape, A4, portrait
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Frame

styles = getSampleStyleSheet()
c = canvas.Canvas('example.pdf', pagesize=landscape(A4))  # alternatively use bottomup=False
width, height = A4

colWidth = 100
rowHeight = 100

thead = [
    ('Produto', 'Valor', 'Peso', 'data','Produto', 'Valor', 'Peso', 'data',),
]

maxLenght = 0

def setText(text:str):
    global maxLenght
    maxLenght = len(text) if maxLenght < len(text) else maxLenght
    return Paragraph(text, styles['Normal'])

def getColSize():
    return height / len(thead[0])

def getRowHeight():
    global colWidth, maxLenght
    return ((maxLenght / colWidth) * 100) + 10


tbody = [
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '2'),
    ('iPhone', '22','iPhone', '5252525252525252525252'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', '5252525252525252525252'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', '5252525252525252525252'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', '5252525252525252525252'),
     ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', '5252525252525252525252'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', 'kk'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', 'dd'),
    ('Panetone', '20'),
    ['iPhone', '1','iPhone', 'ssss','iPhone', 'ddd','iPhone', 'ss'],
    ('Feijão', '5'),
    ('iPhone', '22','iPhone', 'hhh'),
    ('FIM', '22','iPhone', 'hhh'),
]

aux = []
for line in tbody:
    aux.append(list(map(setText, line)))


colWidth = getColSize()
rowHeight = getRowHeight()
if rowHeight < 20:
    rowHeight = 20  

tbody = aux

table_height = (len(tbody) * rowHeight )

data = []

if table_height+20 > width:
    max_page = 0
    bsize = len(tbody)
    for i in range(0, bsize):
        if ((bsize - i) * rowHeight) + rowHeight +20 < width:
            max_page = bsize-i
            print('de',bsize, "So cabem na pagina", len(tbody[:bsize - i]), "elementos")
            break
    while len(aux) > max_page:
        data.append(aux[:max_page])
        aux = aux[max_page:]
    data.append(aux)


for d in data:
    table_height = (len(d) * rowHeight )
    table = Table(thead, colWidths=colWidth, rowHeights=20)
    table.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.red),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TEXTCOLOR', (0, 0),(-1, 0), colors.red),
        ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 0, 200*mm - 20)
    
    table = Table(d, colWidths=colWidth, rowHeights=rowHeight)
    table.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TEXTCOLOR', (0, 0),(-1, 0), colors.red),
        ]))

    table.wrapOn(c, height, width)
    table.drawOn(c, 0, 200*mm - table_height - 20)

    c.drawString(2*mm, 205*mm ,"Welcome to Reportlab!")
    c.showPage()
c.save()