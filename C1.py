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

address=["千葉市","稲毛区","稲毛","３","７"]

err = 0

merger = PyPDF2.PdfFileMerger()


def pdfChanger(imagePath, pdfPath):
    image = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), imagePath))
    image1 = image.convert("RGB")
    PdfPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), pdfPath)
    image1.save(PdfPath)
    merger.append(PdfPath)


def mail(address_list, err, to):
    sender = "intern.summer.24b@gmail.com"

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
        pdfChanger('image/B2.png', 'pdf/CD.pdf')

        msg = "<h3>● 道路情報</h3>" + "<font size='6px'>※道路情報を取得できませんでした。</font>" + "<br>" + "<font size='4px'><span style='color: red;'>入力内容の見直し</span>をお願いいたします。</font>" + "<br>" + "<h3>● 下水情報</h3>" # open('err2.html', 'r', encoding='UTF-8')
        message_text = msg # msg.read()
        # msg.close()
        subject = "エラー：一部データ取得失敗"
        file_path = pdfChanger.PdfPath
        attach_file_path = file_path
        sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
        sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        # slack.notify(text="エラーが発生：一部のデータを取得できず")
    elif err == 3:
        # 千葉下水だけとれる
        pdfChanger('image/B1.png', 'pdf/CG.pdf')

        msg = "<h3>● 下水情報</h3>" + "<font size='6px'>※下水情報を取得できませんでした。</font>" + "<br>" + "<font size='4px'><span style='color: red;'>入力内容の見直し</span>をお願いいたします。</font>" + "<br>" + "<h3>● 道路情報</h3>"
        message_text = msg
        # msg.close()
        subject = "エラー：一部データ取得失敗"
        file_path = pdfChanger.PdfPath
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

            pdfChanger('image/B1.png', 'pdf/CG.pdf')
            pdfChanger('image/B2.png', 'pdf/CD.pdf')

            pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/info.pdf')

            merger.write(pdfPath1)

            msg = str(address) + "<br>" + "<h3>● 道路・下水情報</h3>" + "<font size='6px'>" # open('ok.html', 'r', encoding='UTF-8')
            message_text = msg # msg.read()
            # msg.close()
            subject = "データ取得成功"
            file_path = pdfPath1
            attach_file_path =file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)

        elif "さいたま市" in address_list[0]:
            pdfChanger('image/B3.png', 'pdf/SG.pdf')
            pdfChanger('image/B4.png', 'pdf/SD.pdf')
            
            pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/info.pdf')
            merger.write(pdfPath2)

            msg = str(address) + "<br>" + "<h3>● 道路・下水情報</h3>" + "<font size='6px'>" # open('ok.html', 'r', encoding='UTF-8')
            message_text = msg # msg.read()
            # msg.close()
            subject = "データ取得成功"
            file_path = pdfPath2
            attach_file_path= file_path
            sendmail.create_message_with_attachment(sender, to, subject, message_text, file_path, cc=None)
            sendmail.main(sender, to, subject, message_text, attach_file_path, cc=None)


    merger.close()


# mail(address, err, 'lidanyang633@gmail.com')
# mailに住所を書く
# 色変更