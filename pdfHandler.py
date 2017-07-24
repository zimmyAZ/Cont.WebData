import PyPDF2
from pdf2jpg import pdf2jpg


pdf_file = open('test.pdf')
read_pdf = PyPDF2.PdFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
print number_of_pages
page = read_pdf.getPage(range(0, number_of_pages))
pdf2jpg(pdf_file)


