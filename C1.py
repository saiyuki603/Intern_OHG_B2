from ctypes import addressof
import importlib
import traceback
# import slackweb
from PIL import Image
import base64
from email.mime.multipart import MIMEMultipart
import os
import PyPDF2
import sendmail

def mail(address,err):

    sender = "intern.summer.24b@gmail.com"
    to ="shun7109@icloud.com"

    # sender = "intern.ohg.24b@gmail.com"
    # to ="lidanyang633@gmail.com"


def mail(address_list, err, to):
    sender = "intern.summer.24b@gmail.com"

    merger = PyPDF2.PdfFileMerger()
    # slack = slackweb.Slack(url = "https://hooks.slack.com/services/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")

    # 両方とも取れない
    if err == 1:
        msg = "<font size='6px'>取得範囲外又は誤った住所入力、あるいはシステム上のエラーの疑いがあります。</font>"+"<br>住所をもう一度ご確認の上、再度お試しください。それでも取得できない場合はお問い合わせください。"
        message_text = msg


        subject = "エラー：データ取得失敗"
        sendmail.create_message(sender, to, subject, message_text, cc=None) 
        attach_file_path = None
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)
        # slack.notify(text="エラーが発生：入力不正又は範囲外")

    elif err == 2:
        # 千葉道路だけとれる
        Chiba_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B2.png'))
        CG2 = Chiba_Doro.convert("RGB")
        pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CD.pdf')
        CG2.save(pdfPath2)
        merger.append(pdfPath2)

        msg = "<h3>● 道路情報</h3>" + "<font size='6px'>※道路情報を取得できませんでした。</font>" + "<br>" + "<font size='4px'><span style='color: red;'>入力内容の見直し</span>をお願いいたします。</font>" + "<br>" + "<h3>● 下水情報</h3>" # open('err2.html', 'r', encoding='UTF-8')
        message_text = msg # msg.read()
        # msg.close()
        subject = "エラー：一部データ取得失敗"
        file_path = pdfPath2
        attach_file_path = file_path
        sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        # slack.notify(text="エラーが発生：一部のデータを取得できず")
    elif err == 3:
        # 千葉下水だけとれる
        Chiba_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B1.png'))
        CG1 = Chiba_Gesui.convert("RGB")
        pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG.pdf')
        CG1.save(pdfPath1)
        merger.append(pdfPath1)

        msg = "<h3>● 下水情報</h3>" + "<font size='6px'>※下水情報を取得できませんでした。</font>" + "<br>" + "<font size='4px'><span style='color: red;'>入力内容の見直し</span>をお願いいたします。</font>" + "<br>" + "<h3>● 道路情報</h3>"
        message_text = msg
        # msg.close()
        subject = "エラー：一部データ取得失敗"
        file_path = pdfPath1
        attach_file_path = file_path
        sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)
        # slack.notify(text="エラーが発生：一部のデータを取得できず")

        

    # 両方とも取れる
    elif err == 0:

        address = ''
        for i in range(3):
            address = address + address_list[i]
        for i in range(3, len(address_list)):
            if i == 3:
                address = address + address_list[i]
            else:
                address = address + '-' + address_list[i]

        if "千葉市" in address_list[0]:

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

            msg = str(address) + "<br>" + "<h3>● 道路・下水情報</h3>" + "<font size='6px'>" # open('ok.html', 'r', encoding='UTF-8')
            message_text = msg # msg.read()
            # msg.close()
            subject = "データ取得成功"
            file_path = pdfPath5
            attach_file_path =file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        elif "さいたま市" in address_list[0]:
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

            msg = str(address) + "<br>" + "<h3>● 道路・下水情報</h3>" + "<font size='6px'>" # open('ok.html', 'r', encoding='UTF-8')
            message_text = msg # msg.read()
            # msg.close()
            subject = "データ取得成功"
            file_path = pdfPath6
            attach_file_path= file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)


    merger.close()

# address=["千葉市","稲毛区","稲毛","３","７"]

# err = 0
# mail(address, err, 'shun7109@icloud.com')
# mailに住所を書く
# 色変更