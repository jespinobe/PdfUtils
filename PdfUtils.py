

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

#program who paste two pdf file
def paste_pdf(pdf_file1, pdf_file2):
    import PyPDF2
    pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
    pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_number in range(pdf_reader1.numPages):
        page_object = pdf_reader1.getPage(page_number)
        pdf_writer.addPage(page_object)
    for page_number in range(pdf_reader2.numPages):
        page_object = pdf_reader2.getPage(page_number)
        pdf_writer.addPage(page_object)
    return pdf_writer

def filesToPaste():
    pdf_file1 = input("Enter the name of the first pdf file: ")
    if (validate_file(pdf_file1)==True):
        pdf_file2 = input("Enter the name of the second pdf file: ")
        pdf_file_paste = input("Enter the name of the paste pdf file: ")
        if (validate_file(pdf_file2)==True):
            pdf_writer = paste_pdf(pdf_file1, pdf_file2)
            save_pdf(pdf_writer, pdf_file_paste)
            return True
        else:
            print("The file is not a pdf file or it does not exist")
            return False
    

