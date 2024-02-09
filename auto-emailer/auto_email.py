import email
import email.mime.multipart
import email.mime.text
import getpass
import logging
import os
import re
import smtplib
from collections import namedtuple

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_fmt = logging.Formatter("%(asctime)s %(levelname).4s %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setFormatter(log_fmt)
logger.addHandler(console)

FROM_EMAIL = "tutorials@scipy.org"
CC_EMAIL = "logan.thomas005@gmail.com,tkoyama010@gmail.com,benoit.hamelin@gmail.com,inessa@albuscode.org"  # str no space
HERE = os.path.dirname(__file__)
RECIPIENTS_FILE = "recipients.txt"
Recipient = namedtuple("Recipient", ["first_name", "full_name", "email"])
HTML_FILE = "test.html"


class AutoEmailer:
    def __init__(
        self,
        from_email=FROM_EMAIL,
        cc_email=CC_EMAIL,
        recipients_file=RECIPIENTS_FILE,
        html_file=HTML_FILE,
    ):
        self.from_email = from_email
        self.password = getpass.getpass(prompt="Email password: ")
        self.cc_email = cc_email
        self.recipients_file = recipients_file
        self.html_file = html_file

    @property
    def recipients(self):
        recipients_path = os.path.join(HERE, self.recipients_file)
        if not os.path.isfile(recipients_path):
            logger.error(f"Could not find '{recipients_path}'.")
            return
        logger.info(f"Recipients file is '{recipients_path}'.")

        BAD_CHARS = list("<>,")
        info = []
        with open(recipients_path, "r", encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                line = "".join([c for c in line if c not in BAD_CHARS])
                chunks = line.split()
                first_name = chunks[0]
                email = chunks[-1]
                full_name = " ".join(chunks[:-1])
                info.append(Recipient(first_name, full_name, email))
        return sorted(info)

    def send_html_message(self, email_to, email_subject, html_body):
        msg = email.mime.multipart.MIMEMultipart("alternative")
        msg["From"] = self.from_email
        msg["CC"] = self.cc_email
        msg["To"] = email_to
        msg["Subject"] = email_subject

        part1 = email.mime.text.MIMEText(email_subject, "plain")
        part2 = email.mime.text.MIMEText(html_body, "html")

        msg.attach(part1)
        msg.attach(part2)

        # To and CC must be a list
        rcpts = self.cc_email.split(',') + [email_to]
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.ehlo()
            s.starttls()
            s.login(self.from_email, self.password)
            s.sendmail(self.from_email, rcpts, msg.as_string())

    def send_emails(self):
        template_path = os.path.join(HERE, self.html_file)
        if not os.path.isfile(template_path):
            logger.error(f"Could not find '{template_path}'.")
            return
        logger.info(f"Draft email file is '{template_path}'.")

        with open(template_path, "r", encoding="utf-8") as fp:
            subject_line = fp.readline()
            template_html = fp.read()

        subject = re.match(r".*subject:\s+(.*?)<", subject_line)[1]
        logger.info(f"subject='{subject}'")

        for recipient in self.recipients:
            email_html = template_html.replace("{{Name}}", recipient.first_name)
            self.send_html_message(email_to=recipient.email, email_subject=subject, html_body=email_html)
            logger.info(f"Email sent to '{recipient.full_name}' (<{recipient.email}>)")


if __name__ == "__main__":
    ae = AutoEmailer()
    ae.send_emails()
