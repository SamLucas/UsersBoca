from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unicodedata import normalize

import smtplib
import csv

def remover_acentos(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

emailFrom = 'seu_emai@aqui.com'
usersitenumber = 1
usernumber = 2001
envia = "n"

arquivo = open('usuarios.csv')
pessoas = csv.DictReader(arquivo)

nomes = []
usuarios = []
senhas = []
emails = []

cont_usuarios = 0

for pessoa in pessoas:
  nomes.append(pessoa['nome'])
  usuarios.append(pessoa['usuario'].replace(" ", "_"))
  senhas.append(pessoa['senha'])
  emails.append(pessoa['email'])
  cont_usuarios += 1

a = open("dados/import.txt", "w")
a.write("[user]\n")
a.close()

envia = input("Deseja enviar o email com as informações do contest? (s/n) ")
envia = input("Tem certeza? autorizando, esse script vai enviar um email com as informações do contest. (s/n) ")

for k in range(0,cont_usuarios):
  
  email = emails[k]
  userdesc = nomes[k]
  username = usuarios[k]
  userpassword = senhas[k]
  usernumber += 1

  a = open("dados/import.txt", "a")
  a.write("usernumber={0}\n" .format(usernumber))
  a.write("usersitenumber={0}\n" .format(usersitenumber))
  a.write("username={0}\n" .format(username))
  a.write("userdesc={0}\n" .format(username))
  a.write("userenabled=t\n")
  a.write("userfullname={0}\n" .format(userdesc))
  a.write("userpassword={0}\n\n" .format(userpassword))
  a.close()

  if(envia == "s"):

    message = ""
    message += 'Boa Tarde, tudo certo? informações do contest:\n\n'
    message += 'IP: 3.15.45.108\n'
    message += 'Usuario: '+usuarios[k]+'\n'
    message += 'Senha: '+senhas[k]
    message += '\n\nOBSERVAÇÃO: o pdf da prova está na última questão.\n'
    message += '\nDúvidas, críticas, erros e sugestões: ' + emailFrom + '\n\nprintf("boa prova!");'


    msg = MIMEMultipart()

    password = 'Extraterrestre06'
    
    msg['From'] = emailFrom
    msg['To'] = emails[k]
    msg['Subject'] = 'Informações para o contest.'
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()