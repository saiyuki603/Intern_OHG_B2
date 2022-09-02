import importlib
from PIL import Image
import base64
from email.mime.multipart import MIMEMultipart
import os
import PyPDF2
import sendmail

def mail(address,err):
    sender = "intern.ohg.24b@gmail.com"
    to ="lidanyang633@gmail.com"
    merger = PyPDF2.PdfFileMerger()
    err =1

    # 両方とも取れない
    if err == 1:
        message_text = "err1.txt"
        subject = "エラーが発生：入力不正又は範囲外"
        sendmail.create_message(sender, to, subject, message_text, cc=None) 
        attach_file_path = None
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)
        
        

    elif err == 2:
        # 千葉道路だけとれる
        Chiba_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B2.png'))
        CG2 = Chiba_Doro.convert("RGB")
        pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CD.pdf')
        CG2.save(pdfPath2)
        merger.append(pdfPath2)

        message_text = "err2.txt"
        subject = "エラーが発生：一部のデータを取得できず"
        file_path = pdfPath2
        attach_file_path = file_path
        sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)
    elif err == 3:
        # 千葉下水だけとれる
        Chiba_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B1.png'))
        CG1 = Chiba_Gesui.convert("RGB")
        pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG.pdf')
        CG1.save(pdfPath1)
        merger.append(pdfPath1)

        message_text = "err3.txt"
        subject = "エラーが発生：一部のデータを取得できず"
        file_path = pdfPath1
        attach_file_path = file_path
        sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        

    # 両方とも取れる
    elif err == 0:
        if "千葉市" in address[0]:
            Chiba_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B1.png'))
            CG1 = Chiba_Gesui.convert("RGB")
            pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG.pdf')
            CG1.save(pdfPath1)

            Chiba_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B2.png'))
            CG2 = Chiba_Doro.convert("RGB")
            pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CD.pdf')
            CG2.save(pdfPath2)

            merger.append(pdfPath1)
            merger.append(pdfPath2)

            pdfPath5 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/info.pdf')

            merger.write(pdfPath5)

            message_text = "ok.txt"
            subject = "データ取得成功"
            file_path = pdfPath5
            attach_file_path =file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        elif "さいたま市" in address[0]:
            Saitama_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B3.png'))
            CG3 = Saitama_Gesui.convert("RGB")
            pdfPath3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/SG.pdf')
            CG3.save(pdfPath3)

            Saitama_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B4.png'))
            CG4 = Saitama_Doro.convert("RGB")
            pdfPath4 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/SD.pdf')
            CG4.save(pdfPath4)

            merger.append(pdfPath3)
            merger.append(pdfPath4)

            pdfPath6 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/info.pdf')
            merger.write(pdfPath6)

            message_text = "ok.txt"
            subject = "データ取得成功"
            file_path = pdfPath6
            attach_file_path= file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

    merger.close()
