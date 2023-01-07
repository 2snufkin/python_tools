import os_tools
from PyPDF2 import PdfWriter, PdfReader


REVERSED_LOCATION =r'C:\Users\Pini\Pictures'

def get_pdf_reader(path):
    pdfFileObj = open(path, 'rb')
    return PdfReader(pdfFileObj)


def merge_after_scan(path1, path2, output_file_name, is_to_reverse):
    '''
    after scanning pages in duplex mode you need to manually merge them, alternating the pages from each pdf
    :param path1: the pdf file that contains the first page of the scanning doc(and all the odd pages)
    :param path2: the pdf with the even pages
    :param output_file_name: where do you xant to save the file
    :param is_to_reverse: True if you didn't change the order of the pages in the second scan
    :return:
    '''
    pdfFileObj1 = open(path1, 'rb')
    if is_to_reverse:
        new_path = reverse_pdf(path2)
        pdfFileObj2 = open(new_path, 'rb')
    else:
        pdfFileObj2 = open(path2, 'rb')
    output = PdfWriter()
    pdf1reader = PdfReader(pdfFileObj1)
    pdf2reader = PdfReader(pdfFileObj2)
    pdf1size = get_no_of_pages(pdf1reader)
    for i in range(pdf1size):
        page_to_save_odd = get_page(pdf1reader, i)
        page_duplex = get_page(pdf2reader, i)
        output.add_page(page_to_save_odd)
        output.add_page(page_duplex)
    pdfFileObj1.close()
    pdfFileObj2.close()
    outputFile = open(output_file_name, 'wb')
    output.write(outputFile)
    outputFile.close()


def reverse_pdf(pdf_path):
    '''
    Reverse the pages of a pdf
    :param pdf_path: the path of the pdf
    :return: a reversed version
    '''
    write_obj = PdfWriter()
    read_obj = PdfReader(pdf_path)
    for page in reversed(read_obj.pages):
        write_obj.add_page(page)
    filename = os_tools.get_filename_from_path(pdf_path, True)
    location = os_tools.extract_folder_from_path(pdf_path)
    new_filename = location + R'\reversed_%s' % filename
    write_obj.write(new_filename)
    return new_filename


def get_page(pdf_reader, page_no):

    return pdf_reader.pages[page_no]


def get_no_of_pages(pdf_reader):
    '''
    get the total number of pages of a specific pdf
    :param pdf_reader: the pdf reader object
    :return: nmber of total pages
    '''
    return len(pdf_reader.pages)


def extract_text_from_page(pdfReader, page_no):
    # extracting text from page
    return pdfReader.pages[page_no].extract_text()


reverse_pdf(r'D:\Books\itext7buildingblocks.pdf')