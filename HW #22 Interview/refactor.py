import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:
    GMAIL_IMAP = "imap.gmail.com"
    GMAIL_SMTP = "smtp.gmail.com"
    PASSWORD = 'qwerty'
    SUBJECT = 'Subject'
    RECIPIENTS = ['vasya@email.com', 'petya@email.com']
    MESSAGE = 'Message'
    HEADER = None
    LOGIN = 'login@gmail.com'

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.LOGIN
        msg['To'] = ', '.join(self.RECIPIENTS)
        msg['Subject'] = self.SUBJECT
        msg.attach(MIMEText(self.MESSAGE))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()  # identify ourselves to smtp gmail client
        ms.starttls()  # secure our email with tls encryption
        ms.ehlo()  # re-identify ourselves as an encrypted connection
        ms.login(self.LOGIN, self.PASSWORD)
        ms.sendmail(self.LOGIN, ms, msg.as_string())
        ms.quit()

    def receive(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.LOGIN, self.PASSWORD)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.HEADER if self.HEADER else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    mailer = Mail()
    mailer.send_message()
    mailer.receive()
