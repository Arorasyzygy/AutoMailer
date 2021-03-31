import csv, smtplib, ssl, email
from getpass import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
name=[]
mail=[]
with open('test.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count=0
    for i in csv_reader:
        if line_count==0:
            print(f'Column names are {" ".join(i)}')
            line_count+=1
        else:
            name.append(i[0])
            mail.append(i[1])
            line_count+=1
    print(f'Processed {line_count} lines')
    print(name)
    print(mail)

subject= "Space App Organizational Certificates"
body= "Apologies for the delayed response. Please find the attachment below."
sender_email = input("Enter your mail id: ")
password = getpass("Enter your password: ")

message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
text = message.as_string()

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email 
, password)
    with open("test.csv") as file:
        reader=csv.reader(file)
        next(reader)
        for name, mail in reader:
            server.sendmail(sender_email, mail, text)




