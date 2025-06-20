import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('shkroyas@gmail.com', 'eujw vrgq spax whiw')
subject = 'Test Email'
body = 'This is a test email sent using Python.'
message = f'Subject: {subject}\n\n{body}'
listadd=['shakyaroyas@gmail.com', 'royasshakya@gmail.com']
ob.sendmail('shkroyas@gmail.com', listadd, message)
print('Email sent successfully!')
ob.quit()