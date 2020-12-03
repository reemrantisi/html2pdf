import bs4
import re
from xhtml2pdf import pisa , parser

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    
    # load the file
    with open("template.html") as inf:
        html = inf.read()
        soup = bs4.BeautifulSoup(html)
        # print(soup)
        written = soup.find(string=re.compile("Written by"))
        print(written)
        name = written.find_next("p")  
        print(name)
        name.extract()
        #print(soup)
    source_html = soup.prettify()
    output_filename = "test.pdf"

    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)



