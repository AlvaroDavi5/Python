from reportlab.pdfgen import canvas # import canvas library from reportlab package (pdfgen module)

def generatePDF(lista):
    try:
        nome_pdf = input("Digite o nome do arquivo PDF a ser gerado...\n")
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Dados dos Pacientes')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf)) # define a file extention and placeholder to filename
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))



lista = {'Augusto': '38', 'Ana Clara': '19', 'Maria': '22','Cláudio':'24'}

generatePDF(lista)
