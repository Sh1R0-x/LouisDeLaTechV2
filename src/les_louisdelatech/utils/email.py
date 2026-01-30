import base64
from email.message import EmailMessage

from googleapiclient.discovery import Resource


def _gmail_raw_message(*, from_addr: str, to_addr: str, subject: str, body: str) -> str:
    msg = EmailMessage()
    msg["To"] = to_addr
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg.set_content(body)

    # Gmail API expects the RFC 2822 message in base64url encoding.
    return base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")


def send_email(
    gmail_sdk: Resource,
    *,
    from_addr: str,
    to_addr: str,
    subject: str,
    body: str,
):
    raw = _gmail_raw_message(
        from_addr=from_addr,
        to_addr=to_addr,
        subject=subject,
        body=body,
    )
    return gmail_sdk.users().messages().send(userId="me", body={"raw": raw}).execute()
