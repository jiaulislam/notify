from fastapi import APIRouter, BackgroundTasks

from notify.logging import get_logger
from notify.schemas.notification import SMSPayload
from notify.services import sms

logging = get_logger(__name__)


router = APIRouter(prefix="/smsservice", tags=["SMSService"])


@router.post(
    "/send",
    summary="Send an SMS respective with Event Type",
    description="This route is used to send a SMS to a single customer",
)
def send_sms(payload: SMSPayload, background_task: BackgroundTasks):
    logging.debug(f"raw payload: {payload.json()}")
    background_task.add_task(sms.send_sms, payload)
    return {"status": "ok"}
