from datetime import date

from pydantic import EmailStr

from notify.enums import MsgTypeEnum
from notify.schemas import BaseSchema


class Notifier(BaseSchema):
    user_name: str
    bill_activation_date: date | None = None


class EmailNotifier(Notifier):
    email: EmailStr


class PhoneNotifier(Notifier):
    phone: str


class RequestPayload(BaseSchema):
    event_type: MsgTypeEnum


class EmailPayload(RequestPayload):
    body: EmailNotifier


class PhonePayload(RequestPayload):
    body: PhoneNotifier
