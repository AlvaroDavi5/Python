from reportlab.pdfgen import canvas


def insertContentOnPDF(pdf, filename):
	pdf.setTitle(filename)
	pdf.setFont('Helvetica-Bold', 16)
	pdf.setFillColor('gold')
	pdf.drawString(200, 800, "The One Ring")
	pdf.setFont('Helvetica-Oblique', 12)
	pdf.setFillColor('orange')
	pdf.drawString(100, 600, "Three Rings for the Elven Lords under the Sky")
	pdf.drawString(100, 588, "Seven for the Dwarf Lords in their halls of Stone")
	pdf.drawString(100, 576, "Nine for Mortal Men doomed to die")
	pdf.drawString(100, 564, "One for the Dark Lord on his dark throne")
	pdf.drawString(100, 552, "In the Land of Mordor where the Shadows lie")
	pdf.drawString(100, 540, "One Ring to rule them all, One Ring to find them")
	pdf.drawString(100, 528, "One Ring to bring them all and in the darkness bind them")
	pdf.drawString(100, 516, "In the Land of Mordor where the shadows lie…")


def generatePDF():
	try:
		filename = input("Enter the name of the file: ") # input filename
		pdf = canvas.Canvas('{}.pdf'.format(filename))
		insertContentOnPDF(pdf, filename)
		pdf.save()
		print("Sucessfully to generate {}.pdf".format(filename))
	except:
		print("Error to generate PDF file!")


generatePDF()

'''

arq = open("./LOTR_poem.txt", 'r')
pdfF = canvas.Canvas('test.pdf')
pdfF.setTitle('test')
pdfF.setFont('Helvetica-Bold', 16)
contentTXT = arq.read()
lines = contentTXT.split('\n')
lines = str(lines)
lines = lines.replace("', '", '\n')
lines = lines.replace("'", '\n')
lines = lines.replace('[', '\n')
lines = lines.replace(']', '\n')
pdfF.drawString(100, 500, lines)
pdfF.save()
arq.close()

'''
