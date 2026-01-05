from typing import Protocol, Union, List

class MailService(Protocol):
    def send_email(
        self,
        to_email: Union[str, List[str]],
        subject: str,
        html_content: str,
        from_email: str
    ) -> None:
        ...