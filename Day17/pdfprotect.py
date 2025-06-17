from PyPDF2 import PdfReader, PdfWriter

#open the pdf file
file_pdf=PdfReader("mathworks_installation_help.pdf")
#Object for pdf writer
out_pdf=PdfWriter()

# print(file_pdf.numPages)

for page in file_pdf.pages:
    out_pdf.add_page(page)

password="Royas@123"

out_pdf.encrypt(password)

with open("mathworks_installation_help_encrypted.pdf","wb") as filename:
    out_pdf.write(filename)