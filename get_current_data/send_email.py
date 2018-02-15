import smtplib
import ConfigParser
import ast
from email.mime.multipart import MIMEMultipart


def read_config(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config


def send_email(subject, message):

    config = read_config("smtp_config.ini")
    my_address = config.get('credentials', 'my_address')
    # print my_address
    password = config.get('credentials', 'password')
    recipient_list = ast.literal_eval(config.get('recipient_list','nacc_recipients'))
    port = config.get('credentials', 'port')
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.ufl.edu', port=25)

    # For each contact, send the email:
    for recipient in recipient_list:
        print recipient
        msg = MIMEMultipart()       # create a message

        # setup the parameters of the message
        msg['From'] = my_address
        msg['To'] = recipient
        msg['Subject'] = subject

        # add in the message body
        msg.attach(message)

        # send the message via the server set up earlier.
        s.sendmail(my_address,recipient, msg.as_string())
        del msg
    s.quit()

    # Terminate the SMTP session and close the connection
