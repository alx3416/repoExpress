# hola mundo en python
import math
from fpdf import FPDF

def myFunction():
    print("Hola mundo")


def getSquareArea(side):
    return side ** 2


def getCircleArea(radius):
    return math.pi * (radius ** 2)


def getTriangleArea(side1, side2):
    return (side1 * side2) / 2.0


myFunction()
print(getSquareArea(3))
print(getCircleArea(20))
print(getTriangleArea(5, 7))






# Crea una clase que hereda de FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'MI PRIMER PDF', 0, 1, 'C')
        
    def footer(self):
        self.set_y(-15)  # Posiciona el pie de página 15 mm desde el final de la página
        self.set_font('Arial', 'I', 8)  # Establece la fuente del pie de página
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')  # Añade una celda con el número de página

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Crear una instancia de PDF
pdf = PDF()
pdf.add_page()

# Añadir contenido
pdf.chapter_title('PRACTICANDO INSERTAR UN STRING')
pdf.chapter_body('ESTE STRING ES EL INSERTADO')


# Guardar el archivo PDF
pdf.output('mi_documento.pdf')

print("PDF creado exitosamente")
