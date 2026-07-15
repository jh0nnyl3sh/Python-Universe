from pdf2docx import Converter


pdf_path = 'ugurpdf.pdf'

docx_path = "ugurpdf.docx"

cv = Converter(pdf_file = pdf_path)
cv.convert(docx_file=docx_path, start=0, end=None)

cv.close()