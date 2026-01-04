from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Union, List, Any, Optional
from decimal import Decimal
from datetime import datetime
from app.core.settings.pydantic_setitngs import settings

from app.domain.mail.service_protocol import MailService

class SendGridClient(MailService):
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
    ):
        created_at_str = created_at.strftime("%Y-%m-%d %H:%M")

        postal_code_html = f"{postal_code}" if postal_code else ""
        delivery_notes_html = (
            f"""
            <tr>
            <td style="font-size:13px; padding-top:10px; color:#9ca3af;">
                <em>Delivery notes: {delivery_notes}</em>
            </td>
            </tr>
            """
            if delivery_notes
            else ""
        )

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8" />
        <meta name="color-scheme" content="light dark">
        <meta name="supported-color-schemes" content="light dark">
        <title>Order Confirmation</title>
        </head>

        <body style="
        margin:0;
        padding:0;
        background-color:#f4f6f8;
        font-family:Arial, Helvetica, sans-serif;
        color:#111827;
        ">

        <table width="100%" cellpadding="0" cellspacing="0" style="padding:40px 0;">
            <tr>
            <td align="center">

                <!-- Card -->
                <table width="600" cellpadding="0" cellspacing="0" style="
                background:#ffffff;
                border-radius:12px;
                overflow:hidden;
                box-shadow:0 8px 24px rgba(0,0,0,0.08);
                ">

                <!-- Header -->
                <tr>
                    <td style="
                    padding:24px 32px;
                    background:#0f172a;
                    color:#ffffff;
                    ">
                    <h1 style="margin:0; font-size:22px;">
                        Order Confirmation
                    </h1>
                    <p style="margin:6px 0 0; font-size:14px; opacity:0.85;">
                        Thank you for your purchase, {full_name}
                    </p>
                    </td>
                </tr>

                <!-- Body -->
                <tr>
                    <td style="padding:32px;">

                    <!-- Tracking -->
                    <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:32px;">
                        <tr>
                        <td align="center">
                            <p style="margin:0; font-size:13px; color:#6b7280;">
                            Tracking Code
                            </p>
                            <p style="
                            margin:8px 0 0;
                            font-size:20px;
                            font-weight:bold;
                            letter-spacing:1.5px;
                            color:#0f172a;
                            ">
                            {tracking_token}
                            </p>
                        </td>
                        </tr>
                    </table>

                    <!-- Order Info -->
                    <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Status:</strong> {status}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Quantity:</strong> {quantity}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Total Price:</strong> ${total_price}</td></tr>
                        <tr><td style="font-size:14px;"><strong>Created At:</strong> {created_at_str}</td></tr>
                    </table>

                    <hr style="border:none; border-top:1px solid #e5e7eb; margin:24px 0;" />

                    <!-- Shipping -->
                    <h3 style="margin:0 0 12px; font-size:16px; color:#0f172a;">
                        Shipping Information
                    </h3>

                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr><td style="font-size:14px; padding-bottom:6px;">{address_line}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:6px;">{city}, {region}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:6px;">{country} {postal_code_html}</td></tr>
                        {delivery_notes_html}
                    </table>

                    </td>
                </tr>

                <!-- Footer -->
                <tr>
                    <td style="
                    padding:20px 32px;
                    background:#f8fafc;
                    text-align:center;
                    font-size:12px;
                    color:#6b7280;
                    ">
                    This email was sent to {email}
                    </td>
                </tr>

                </table>
            </td>
            </tr>
        </table>

        </body>
        </html>
        """