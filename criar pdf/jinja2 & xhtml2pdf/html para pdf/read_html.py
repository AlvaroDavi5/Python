from xhtml2pdf import pisa # import module

source_html = open("./LotR page.html", 'r')
output_filename = "LotR.pdf"

def convert_html_to_pdf(source, output):
	# open output file and write like binary
	result_file = open(output, "w+b")

	# convert HTML to PDF
	pisa_status = pisa.CreatePDF(src=source, dest=result_file)

	result_file.close()

	# returns True or False to errors
	return pisa_status.error


# MAIN
if __name__ == "__main__":
	pisa.showLogging()
	convert_html_to_pdf(source_html, output_filename)

source_html.close()
