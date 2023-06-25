from fastapi import APIRouter, BackgroundTasks

from notify.logging import get_logger
from notify.schemas.notification import EmailPayload
from notify.services import email

logging = get_logger(__name__)


router = APIRouter(prefix="/mailservice", tags=["EmailService"])


@router.post(
    "/send",
    summary="Send an email respective with Event Type",
    description="This route is used to send an email to a single customer",
)
def send_mail(payload: EmailPayload, background_task: BackgroundTasks):
    logging.debug(f"raw payload: {payload.json()}")
    background_task.add_task(email.send_mail, payload)
    return {"status": "ok"}
