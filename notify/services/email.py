import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from notify.config import configs
from notify.enums import MsgTypeEnum
from notify.logging import get_logger
from notify.schemas.notification import EmailNotifier, EmailPayload

logging = get_logger(__name__)


message = MIMEMultipart("alternative")


def lapsed_policy_email(payload: EmailNotifier) -> str:
    return f"""\
            <html>
                <body style="font-family: Arial, Helvetica, Courier New">
                    <p>Dear Policy Holder,<br>
                    Greetings from Pragati Life Insurance Ltd<br>
                    </p>
                    <p>Your premium fee request for Policy No: {payload.policy_no} could no longer processed the use of bKash/Nagad due to lapsed over 3 months.</p><br>
                    <p>For any query reach us at : <span>880-2-9124024</span></p>
                    <p>With Regards,<br>
                        Pragati Life Insurance Ltd.
                    </p>
                    <br>
                    <p style="color: #999999; font-family: Arial;">**This is a system-generated email. Please do not reply to this message.</p>
                    <div>
                        <img src="https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png" alt="Pragati Life Logo" style="width: 200px;">
                    </div>
                    <p style="font-size: 12px;">
                        Pragati Insurance Bhaban (6th Floor),<br>
                        20-21 Kawran Bazar, Dhaka. Bangladesh.<br>
                        Phone: 02-8189184-8, Fax: +880-2222241574 <br>
                        Web: <a href="https://pragatilife.com">https://pragatilife.com</a>
                    </p>
                    <br>
                </body>
            </html>
            """


def next_bill_date(payload: EmailNotifier) -> str:
    if payload.bill_activation_date:
        next_bill_date = payload.bill_activation_date.strftime("%d-%b-%Y")
        return f"""\
                <html>
                <body>
                    <p>Dear Policy Holder,<br>
                    Greetings from Pragati Life Insurance Ltd.<br>
                    </p>
                    <p>Your premium fee request for Policy No: {payload.policy_no} could no longer processed the use of bKash/Nagad due to no pending bill. You subsequent bill generatation will be <b>{next_bill_date}</b> or please use other channel to pay premium.</p>
                    <br>
                    <p style="color: #999999; font-family: Arial;">**This is a system-generated email. Please do not reply to this message.</p>
                    <div>
                        <img src="https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png" alt="Pragati Life Logo" style="width: 200px;">
                    </div>
                    <p style="font-size: 12px;">
                        Pragati Insurance Bhaban (6th Floor),<br>
                        20-21 Kawran Bazar, Dhaka. Bangladesh.<br>
                        Phone: 02-8189184-8, Fax: +880-2222241574 <br>
                        Web: <a href="https://pragatilife.com">https://pragatilife.com</a>
                    </p>
                    <br>
                </body>
                </html>
                """
    else:
        raise ValueError("bill_activation_date is None")


def premium_paid(payload: EmailNotifier) -> str:
    return f"""\
            <html>
                <body>
                    <p>Dear Policy Holder,<br>
                    Greetings from Pragati Life Insurance Ltd.<br>
                    </p>
                    <p>Your premium amount: {payload.premium_amount} for Policy: {payload.policy_no} has been successfully received.</p>
                    <br>
                    <p style="color: #999999; font-family: Arial;">**This is a system-generated email. Please do not reply to this message.</p>
                    <div>
                        <img src="https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png" alt="Pragati Life Logo" style="width: 200px;">
                    </div>
                    <p style="font-size: 12px;">
                        Pragati Insurance Bhaban (6th Floor),<br>
                        20-21 Kawran Bazar, Dhaka. Bangladesh.<br>
                        Phone: 02-8189184-8, Fax: +880-2222241574 <br>
                        Web: <a href="https://pragatilife.com">https://pragatilife.com</a>
                    </p>
                    <br>
                </body>
            </html>
            """


def send_mail(payload: EmailPayload):
    try:
        with smtplib.SMTP(
            str(configs.smtp_server), configs.smtp_outgoing_port
        ) as server:
            server.set_debuglevel(1)
            body = payload.body
            message["From"] = configs.smtp_email
            message["to"] = body.email
            match payload.event_type:
                case MsgTypeEnum.LAPSED:
                    message[
                        "Subject"
                    ] = f"Policy: {body.policy_no} lapsed - Pragati Life Insurance Ltd."
                    partial = MIMEText(lapsed_policy_email(body), "html")
                case MsgTypeEnum.PREMIUM_PAID:
                    message[
                        "Subject"
                    ] = f"Policy: {body.policy_no} Premium Received - Pragati Life Insurance Ltd."
                    partial = MIMEText(premium_paid(body), "html")
                case _:
                    message[
                        "Subject"
                    ] = f"No due bill for Policy: {body.policy_no} - Pragati Life Insurance Ltd."
                    partial = MIMEText(next_bill_date(body), "html")
            message.attach(partial)
            server.sendmail(configs.smtp_email, body.email, message.as_string())
    except Exception as e:
        logging.exception(e)
