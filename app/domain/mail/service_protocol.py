from typing import Protocol, Union, List, Optional
from datetime import datetime
from decimal import Decimal

class MailService(Protocol):
    def send_email(
        self,
        to_email: Union[str, List[str]],
        subject: str,
        html_content: str,
        from_email: str
    ) -> None:
        ...

    def generate_order_html_content(
        self, 
        quantity: int,
        total_price: Decimal,
        created_at: datetime,
        tracking_token: str,
        status: str,
        full_name: str,
        email: str,
        address_line: str,
        city: str,
        region: str,
        country: str,
        postal_code: Optional[int] = None,
        delivery_notes: Optional[str] = None
    ) -> str:
        ...