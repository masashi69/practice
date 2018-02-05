#! python3
# combinePdfs.py - Combines all the PDFs in the carrent working directory into
# into a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key/str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop throwgh all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # TODO: Loop throwgh all the pages (except the first)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getpage(pageNum)
        pdfWriter.addpage(pageObj)

# TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
