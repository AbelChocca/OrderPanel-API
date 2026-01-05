from app.infra.mail.sendgrid.base import SendGridService
from functools import lru_cache

@lru_cache
def get_mail_service() -> SendGridService:
    return SendGridService()