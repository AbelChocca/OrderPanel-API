

from app.infra.messaging.payloads.order import OrderCreatedInfo

def render_order_confirmation_html(
        info: OrderCreatedInfo
    ):
        created_at_str = info['created_at'].strftime("%Y-%m-%d %H:%M")

        postal_code_html = f"{info['postal_code']}" if info["postal_code"] else ""
        delivery_notes_html = (
            f"""
            <tr>
            <td style="font-size:13px; padding-top:10px; color:#9ca3af;">
                <em>Delivery notes: {info['delivery_notes']}</em>
            </td>
            </tr>
            """
            if info['delivery_notes']
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
                        Thank you for your purchase, {info['full_name']}
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
                            {info['tracking_token']}
                            </p>
                        </td>
                        </tr>
                    </table>

                    <!-- Order Info -->
                    <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Status:</strong> {info['status']}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Quantity:</strong> {info['quantity']}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:8px;"><strong>Total Price:</strong> ${info['total_price']}</td></tr>
                        <tr><td style="font-size:14px;"><strong>Created At:</strong> {created_at_str}</td></tr>
                    </table>

                    <hr style="border:none; border-top:1px solid #e5e7eb; margin:24px 0;" />

                    <!-- Shipping -->
                    <h3 style="margin:0 0 12px; font-size:16px; color:#0f172a;">
                        Shipping Information
                    </h3>

                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr><td style="font-size:14px; padding-bottom:6px;">{info['address_line']}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:6px;">{info['city']}, {info['region']}</td></tr>
                        <tr><td style="font-size:14px; padding-bottom:6px;">{info['country']} {postal_code_html}</td></tr>
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
                    This email was sent to {info['email']}
                    </td>
                </tr>

                </table>
            </td>
            </tr>
        </table>

        </body>
        </html>
        """