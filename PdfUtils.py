

##Program who count de numbers of page in pdf file
def count_pages(pdf_file):
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    return pdf_reader.numPages

#Program who cut a page from Pdf file
def cut_pdf(pdf_file, page_number):
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    #for page_number in range(pdf_reader.numPages):
    page_object = pdf_reader.getPage(page_number)
    pdf_reader.getPage(page_number)
    pdf_writer.addPage(page_object)
    return pdf_writer

#Program how save the pdf file
def save_pdf(pdf_writer, pdf_file):
    pdf_output = open(pdf_file, 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

def main():
    pdf_file = input("Enter the name of the pdf file: ")
    if (validate_file(pdf_file)==True):
        for i in range(1, count_pages(pdf_file)):
            pdf_writer = cut_pdf(pdf_file, i)
            save_pdf(pdf_writer, pdf_file+'_page_' + str(i) + '.pdf')
    else:
        print("The file is not a pdf file or it does not exist")

#program who validate if the file exist and is a pdf file  
def validate_file(pdf_file):
    import os.path
    if os.path.isfile(pdf_file) and pdf_file.endswith('.pdf'):
        return True
    else:
        return False


main()
