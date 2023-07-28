import pdfreader

file_object = open("C:\\Users\\mhmts\\PycharmProjects\\pdf-audio-reader-app\\twopage.pdf", "rb")
pdf_file_reader = pdfreader.PdfFileReader(file_object)

extracted_text = ""

for page_number in range(pdf_file_reader.numPages):
    pdf_page_obj = pdf_file_reader.getPage(page_number)

    extracted_text += pdf_page_obj.extractText()

file_object.close()
print(extracted_text)