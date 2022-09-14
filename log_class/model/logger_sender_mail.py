import smtplib 
from email.message import EmailMessage
import datetime

class LogMail():

   def __init__(self,receiver_email_address,level, message, object):
      self.receiver_email_address=receiver_email_address
      self.level = level
      self.message = message
      self.object = object
      self.sender_email_address = "davidalejandro0903@gmail.com" 

   def set_color(self):
         background = 'RED'
         color = 'BLUE'
         if self.level == 'INFO':
            pass
         elif self.level == 'WARNING':
            background = 'BLACK'
            color = 'YELLOW'
         elif self.level == 'ERROR':
            background = 'BLUE'
            color = 'RED'
         else:
            background = 'BLACK'
            color = 'MAGENTA'
         return background,color

   def get_wrapper(self,background_color,date):
      wrapper  = """
      <!DOCTYPE html> 
      <head> 
      </head>    
         <body>        
            <h1>Log Aplicación</h1>        
            <p style="background-color:%s; color:%s;">%s %s %s %s</p>        
         </body> 
      </html>
      """
      file_content =  wrapper % (background_color[0],background_color[1],date,self.level,self.message,self.object)
      return file_content

   def get_protocol(self,email_smtp,email_password,message):
      server = smtplib.SMTP(email_smtp, '587') 
      server.ehlo() 
      server.starttls() 
      server.login(self.sender_email_address, email_password) 
      server.send_message(message) 
      server.quit()

   def set_email_data(self):
      message = EmailMessage() 
      message['Subject'] = 'Log aplicación ...'
      message['From'] =  self.sender_email_address
      message['To'] = self.receiver_email_address
      email_smtp = "smtp.gmail.com" 
      email_password = "jnktqyhauklxjgis"
      return message,email_smtp,email_password

   def send_email(self):
      email_data = self.set_email_data()
      now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
      background_color = self.set_color()
      email_data[0].set_content(self.get_wrapper(background_color,now), subtype='html')
      self.get_protocol(email_data[1],email_data[2],email_data[0])
