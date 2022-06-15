from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('filename.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print(doc.info)
