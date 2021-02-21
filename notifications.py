import smtplib
import ssl

# Before implementing this function into your code, make sure you turn "allow less secure apps" on
# Please know that this will make it easier for others to gain access to your account

class Email:
    # initialize an email object by putting in the emailaddress you want to send from and the password to that account
    def __init__(self, emailaddress, password):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.sender_email = emailaddress
        self.password = password

        # Create a secure SSL context
        self.context = context = ssl.create_default_context()

        #server variable
        self.server = -1

    # Send an email
    # Sample call: email.send('test@gmail.com', 'don\'t be alarmed, this is a test')
    def send(self, recipient_email, message):
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.port)
            self.server.starttls() # Secure the connection
            self.server.login(self.sender_email, self.password)
            # Send email here
            self.server.sendmail(self.sender_email, recipient_email, message)
        except Exception as e:
            # Print any error messages to the console
            print(e)
        finally:
            self.server.quit()
            self.server = -1