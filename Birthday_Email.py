import csv # This module is used to read from and write to CSV files in a Pythonic way.
import datetime # This module is used to work with dates and times. It's used here to get the current date.
import smtplib # This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
from email.mime.text import MIMEText # Used for creating messages that are plain text
from email.mime.multipart import MIMEMultipart # Useful for creating emails that could have multiple parts, like text and attachments.
from email.mime.image import MIMEImage # embedding image within email
import os
password = os.environ.get("EMAIL_PASSWORD")

# Gets todays current date, opens csv file and compares current date with all birthdays in csv file
# If there is a match, call send_email function. 
def check_birthday(): 
    current_date = datetime.datetime.now().strftime('%Y-%m-%d') # current date is in (Year-Month-Date) format
    csv_file_path = '/Users/adeilmo226/scripts/Personal_Project/Birthdays.csv'
    with open(csv_file_path, 'r') as file: # open csv file and read it.  
        reader = csv.DictReader(file) 
        for row in reader: #iterates through file
            name, birthday, contact = row['name'], row['birthday'], row['contact']
            if current_date[5:] == birthday[5:]:  # Match MM-DD, excludes year (5 characters with dash (YYYY-) 
                message = "Happy Birthday, " + name + "! Have a great day! "
                send_email(contact, "Happy Birthday!", message) 
                



def send_email(to_address, subject, message):
    from_address = "adeiltherealdeal@gmail.com"  # Your email
    password = "dvvh mhhk mefc fvar"   # Your email password or app password

    # Create a MIMEText message
    html = f"""\
    <html>
      <body>
        <p>{message}</p>
        <img src="https://i.pinimg.com/736x/29/3c/d1/293cd1bc2cbe30d7dcf0d935fd27835f.jpg" alt="Happy Birthday!"> 
      </body>
    </html>
    """
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(html, 'html'))

    # Server configuration (example with Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For TLS

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure
    server.login(from_address, password)
    server.send_message(msg)
    server.quit()
    print("Email was sent")
    



if __name__ == "__main__":
    check_birthday()
    


# cron scheduler is a time based scheduler in Unix-like Operating systems. 

# path for Birthday_Email.py -> /Users/adeilmo226/scripts/Personal_Project/Birthday_Email.py 

# path for python3 -> /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 

# crontab -l -> to use current cron jobs
# crontab -e -> to edit cron jobs
# 00 08 * * * /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/adeilmo226/scripts/Personal_Project/Birthday_Email.py > /Users/adeilmo226/scripts/Personal_Project/cron.log 2>&1
# Press escape then add :wq and enter to save and exit