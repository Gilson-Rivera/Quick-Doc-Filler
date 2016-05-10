from docx import Document
from openpyxl import load_workbook
import os
import comtypes.client
from DB.Database import*

#Creates and handles documents, as well as print and email them.
class TempHandler:

    def Generate(self,Efield,Eid,DocName):
        '''
        Generates the specified document Efield with the information of a person with ID Eid.
        :param Efield:  Type of document to generate.
        :param Eid: ID of the person whose information will be used in the document.
        :param DocName: The name of the generated document.
        :return: The document specified with the person's information.
        '''
        if Efield == 'eCert'or Efield == 'eCont' or Efield == 'eEval'or Efield == 'eDism' or \
                        Efield == 'eWarn' or Efield == 'eTrain':
            id=0
            name=''
            sal=0
            pos=''
            date=''
            sup=''

            #Dictionary of the document templates and their filename
            templates={'eCert':'vf empleo.docx',
                       'eCont':'employment-agreement.docx',
                       'eEval':'Employment_Eval.docx',
                       'eDism':'Sample-Letter-of-Dismissal.docx',
                       'eWarn':'employee-warning-notice.docx',
                       'eTrain':'Completion-Certificate-Template.docx'}

            doc = Document(templates[Efield])

            wb = load_workbook(os.path.dirname(os.path.dirname( __file__ )) +'/Database.xlsx')
            ws = wb['Sheet1']

            empinfo=Database.getEmployeeInfo(Database,Eid)

           #Replaces template words with the person's information
            for info in doc.paragraphs:
                new = info.text.replace('NNNN', empinfo['Name'])
                info.text = new
                new = info.text.replace('SSSS', str(empinfo['Salary']))
                info.text = new
                new = info.text.replace('IIII', str(empinfo['ID']))
                info.text = new
                new = info.text.replace('PPPP', empinfo['Position'])
                info.text = new
                new = info.text.replace('DDDD', empinfo['Date'])
                info.text = new
                new = info.text.replace('UUUU', empinfo['Supervisor'])
                info.text = new
                new = info.text.replace('CCCC', str(float(empinfo['Salary'])*40))
                info.text = new

            doc.save((os.path.dirname( __file__ ))+'/NewTempFile.docx')
            outfile = (os.path.dirname( __file__ ))+'/NewTempFile.docx'

            wdFormatPDF = 17

            #Converts the filled document to pdf.
            word = comtypes.client.CreateObject('Word.Application')
            doc = word.Documents.Open(outfile)
            doc.SaveAs(DocName, FileFormat=wdFormatPDF)
            doc.Close()
            word.Quit()
            wb.save(os.path.dirname(os.path.dirname( __file__ )) +'/Database.xlsx')
            os.remove(outfile)
            return 'Document '+ Efield + ' named: ' + DocName + ' generated successfully'

        else:
            return 'Document selected not valid'

    def printDoc(self, filename):
        '''
        Prints a physical copy of the specifeid file "filename".
        :param filename: File to be printed
        :return: Successfulness of the print command.
        '''
        from subprocess import call
        try:
            reader = "C:/Program Files (x86)/Adobe/Reader 11.0/Reader/AcroRd32.exe"
            file = os.path.dirname(os.path.dirname(os.path.dirname( __file__ )))+ filename + '.pdf'
            printer = "Microsoft XPS Document Writer"
            call([reader, "/T", file, printer])
            return 'Printed document: ' + filename
        except Exception:
            return 'File not found'


    def emailDoc(self, email, file):
        '''
        Emails the specified file to the email address provided.
        :param email: Email address which the file will be sent to.
        :param file: File to send in email.
        :return: Email sent comfirmation.
        '''
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import  MIMEText
        from email.mime.base import MIMEBase
        from email.utils import formatdate
        from email import encoders
        password = "plspring2016"
        fromaddr = "quickdocfiller@gmail.com"
        toaddr = email

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "QDF Document"
        msg['Date'] = formatdate(localtime=True)

        body = "The file you created using QDF."

        msg.attach(MIMEText(body, 'plain'))

        filename = file + '.pdf'
        attachment = open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) +'/Documents/' + file + '.pdf', "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        return 'Email with file sent to: ' + email