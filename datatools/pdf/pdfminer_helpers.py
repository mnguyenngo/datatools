from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTChar, LTFigure
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


def get_layouts(fp):
    """Returns the LTPage objects for a PDF

    Parameters:
        fp (str): file path to PDF

    Returns:
        layout_container (list): List of layouts for each page to be parsed
    """

    # initiate empty container
    layout_container = []

    with open(fp, "rb") as fp:
        # set parameters for pdf mining
        parser = PDFParser(fp)
        document = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        # codec = 'utf-8'

        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for num, page in enumerate(PDFPage.create_pages(document)):
            interpreter.process_page(page)
            layout = device.get_result()
            layout_container.append(layout)

    return layout_container


def parse_layout(layout):
    """Function to recursively parse the layout tree.

    Code copied from:
        https://stackoverflow.com/questions/25248140/how-does-one-obtain-the-location-of-text-in-a-pdf-with-pdfminer
    """
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recursive
