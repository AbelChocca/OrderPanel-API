from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Union, List, Any
from app.core.settings.pydantic_setitngs import settings

from app.domain.mail.service_protocol import MailService

class SendGridService(MailService):
    def __init__(self):
        self.client: SendGridAPIClient = SendGridAPIClient(
            api_key=settings.SENDGRID_API_KEY
        )
    def send_email(
        self,
        to_email: Union[str, List[str]],
        subject: str,
        html_content: str,
        from_email: str = settings.FROM_EMAIL
    ) -> Any:
        message: Mail = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        res = self.client.send(message)
        return res.status_code