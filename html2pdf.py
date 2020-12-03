import bs4
import re
from xhtml2pdf import pisa , parser
import dropbox

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

#transfer data to dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, output_filename, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(output_filename, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

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
    
    # upload to dropbox 
    access_token = '3frTW7nRcYEAAAAAAAAAAebk3A4KAbarudYTc1DLEEUDJuYq-K4HEj2su-cNsA2q'
    transferData = TransferData(access_token)
    file_to = '/htmltopdf/test.pdf'  # The full path to upload the file to, including the file name
    transferData.upload_file(output_filename, file_to)



