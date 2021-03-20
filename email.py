import smtplib
import ssl
from datetime import datetime
import time

# Before implementing this function into your code, make sure you turn "allow less secure apps" on
# Please know that this will make it easier for others to gain access to your account

class Email:
    # initialize an email object by putting in the email address you want to send from and the password to that account
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


if __name__ == '__main__':
    emailaddress = 'FILL THIS IN@gmail.com' # must be a gmail address, also look at line line 4 for extra instructions
    password = 'FILL THIS IN TOO'

    email = Email(emailaddress, password)

    while True:
        seconds = int(datetime.now().strftime('%S'))
        minutes = int(datetime.now().strftime('%M'))

        time.sleep(60 * (4 - (minutes % 5)) + 60 - seconds)

        text = 'FILL IN WHAT YOU WANT YOUR EMAIL TO SAY'

        email.send('itap@purdue.edu', text)  # idk how to put a subject but i think it's fine without one

