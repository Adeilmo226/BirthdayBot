import csv
import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to check birthdays and send emails if there is a match
def check_birthday():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Current date in YYYY-MM-DD format
    csv_file_path = "birthdays.csv"  # Path to CSV file

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, birthday, contact = row['name'], row['birthday'], row['contact']
                if current_date[5:] == birthday[5:]:  # Match MM-DD, excludes year
                    message = f"Happy Birthday, {name}! Have a great day! 🎉"
                    send_email(contact, "Happy Birthday!", message)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send an email
def send_email(to_address, subject, message):
    from_address = os.environ.get("EMAIL_ADDRESS")  # Email address from environment variables
    password = os.environ.get("EMAIL_PASSWORD")  # Email password from environment variables

    if not from_address or not password:
        print("Error: Email credentials not set in environment variables.")
        return

    # Create an HTML email with a fun image
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

    # Send email using SMTP
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, password)
        server.send_message(msg)
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    check_birthday()
