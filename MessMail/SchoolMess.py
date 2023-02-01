#
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import pandas as pd
import configure

import smtplib

def send_email(message, mailp):
    sender = configure.configure['sender']
    password = configure.configure['password']

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEMultipart()
        msg['Subject'] = 'Время прибытия на единую городскую контрольную работу в формате ЕГЭ'
        msg.attach(MIMEText(message))

        with open('adress.jpg', 'rb') as f:
            file = MIMEImage(f.read())


        message1 =   '''



С уважением, Виктория Васильевна Бойчук
+7 (903) 562 -28-39'''
        msg.attach(MIMEText(message1))
        msg.attach(file)

        server.sendmail(sender, mailp, msg.as_string())

        return 'Message ok'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password'
def main():




    metapeople = pd.read_csv('datafr.csv',
                             usecols=['adress', 'Наименование ППЭ', 'Наименование экзамена', 'Код ОО участника',
                                      'Краткое наименование ОО участника', 'ФИО участника', 'Время прибытия в ОО'])

    for i in range(3):  #Здесь надо поменять количество!!! len(metapeople)
       # print(metapeople.iloc[i])
        mailpeople = metapeople.iloc[i][5]
        message = f'''Добрый день! Это время прибытия на единую городскую контрольную работу в формате ЕГЭ по {metapeople.iloc[i][1]} 4 февраля. 

    При себе необходимо иметь паспорт, черные гелевые ручки.

    Адрес ППЭ: г. Москва, м. Пролетарская, ул.  2-ая Дубровская, д.3.

№ П.П: 498

Фамилия участника: {metapeople.iloc[i][4]}

Время прибытия в ОО: {metapeople.iloc[i][6]}

Код ОО Участника: {metapeople.iloc[i][2]}

Краткое наименование ОО: {metapeople.iloc[i][3]}

Номер входа: № 1
'''

        print(send_email(message=message, mailp=mailpeople))

if __name__ == "__main__":
    main()