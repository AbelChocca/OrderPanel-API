
from app.domain.mail.service_protocol import MailService
from app.application.mail.inputs.reactor_inputs import SendMailOfOrderCommand

class SendMailOfOrderCreated:
    def __init__(
            self,
            mail_service: MailService
            ):
        self.mail_service = mail_service

    async def execute(self, command: SendMailOfOrderCommand) -> None:
        pass