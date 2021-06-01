from IPython.display import display, HTML
from xhtml2pdf import pisa


""" ----------------------- Graph Generate ----------------------- """

# graficos publicos do Plotly
graphs = [
    'https://plotly.com/~christopherp/308',
    'https://plotly.com/~christopherp/306',
    'https://plotly.com/~christopherp/300',
    'https://plotly.com/~christopherp/296'
]


# template do relatorio
def report_block_template(report_type, graph_url, caption=''):
	report_block = ''

	if report_type == 'interactive': # se o relatorio for interativo...
		graph_block = '<iframe style="border: none;" src="{graph_url}.embed" width="100%" height="600px"></iframe>'

	elif report_type == 'static': # se for estatico...

		graph_block = ('' +
			'<a href="{graph_url}" target="_blank">' + # abrir o grafico interativo ao clicar na imagem
				'<img style="height: 400px;" src="{graph_url}.png">' +
			'</a>')

		report_block = ('' +
		graph_block +
			'{caption}' + # rubrica opcional para incluir no grafico
			'<br>' + # quebra de linha
			'<a href="{graph_url}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">' +
				'Click to comment and see the interactive graph' + # leitores para comentarios
			'</a>' +
			'<br>' +
			'<hr>') # linha horizontal

	return report_block.format(graph_url=graph_url, caption=caption)


interactive_report = ''
static_report = ''

for graph_url in graphs:
	_static_block = report_block_template(report_type='static', graph_url=graph_url, caption='')
	_interactive_block = report_block_template('interactive', graph_url, caption='')

	static_report += _static_block
	interactive_report += _interactive_block


#display(HTML(interactive_report))
#display(HTML(static_report))


""" ----------------------- PDF Generate ----------------------- """


def convert_html_to_pdf(source_html, output_filename):
	# abrir arquivo de output para escrita (truncando binario)
	result_file = open(output_filename, "w+b")

	# converter HTML para PDF
	pisa_status = pisa.CreatePDF(
		source_html,
		dest=result_file)

	# fechar arquivo de output
	result_file.close()

	# return True on success and False on errors
	return pisa_status.err



convert_html_to_pdf(static_report, "relatorio.pdf")
