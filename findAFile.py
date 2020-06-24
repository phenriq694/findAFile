import os, sys, smtplib, socket

def find(fileNames, path):
    response = []
    for file in fileNames:
        for root, dirs, files in os.walk(path):
            if file in files: 
                response.append(os.path.join(root, file))
        
    return response


def sendMail(fromEmail, password, toEmail, emailMessage):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    print("Loggin...")
    connection.login(fromEmail, password)

    print("Sending e-mail")
    connection.sendmail(fromEmail, toEmail, emailMessage.encode('utf8'))


fileNames = sys.argv[4].split(',')
hostname = socket.gethostname()

print("Searching for the file...")
fileNamesExists = find(fileNames, "C:\\")

emailMessage = 'Subject: Arquivo suspeito na máquina '  + hostname + '\n\n' + 'Foi encontrado um arquivo suspeito na máquina ' + hostname + '\nLocal do arquivo: ' + str(fileNamesExists)

if suspiciousFileExists != []:
    fromEmail = sys.argv[1]
    password = sys.argv[2]
    toEmail = sys.argv[3]
    print("File found!")
    sendMail(fromEmail, password, toEmail, emailMessage)
    password = ""
