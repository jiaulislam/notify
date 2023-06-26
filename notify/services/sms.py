import uuid
from typing import Any, Mapping

from httpx import AsyncClient

from notify.config import configs
from notify.enums import MsgTypeEnum
from notify.logging import get_logger
from notify.schemas.notification import SMSPayload
from notify.schemas.sslwireless import SSLWirelessResponse
from notify.services.parser import parse_xml_response

logging = get_logger(__name__)

QueryParamTypes = Mapping[str, Any]

HEADERS = {
    "User-Agent": "PostmanRuntime/7.32.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}


async def send_sms(payload: SMSPayload) -> SSLWirelessResponse:
    unique = uuid.uuid4()

    match payload.event_type:
        case MsgTypeEnum.LAPSED:
            sms_text = f"Dear Customer, Due to the 90-day premium grace period having expired, your policy No# {payload.body.policy_no}, has lapsed. Inquire with PLIL."
        case _:
            if not payload.body.bill_activation_date:
                raise ValueError("Invalid bill_activation_date or None !")
            activate_date = payload.body.bill_activation_date.strftime("%d-%b-%Y")
            sms_text = f"Dear Customer, there are no payments due at this time for policy No# {payload.body.policy_no}. The date of the next paybill (bkash/nagad) is {activate_date}."

    params: QueryParamTypes = {
        "user": configs.sslwireless_user,
        "pass": configs.sslwireless_pass,
        "sid": "PLILISMS",
        "sms": sms_text,
        "msisdn": payload.body.phone,
        "csmsid": unique,
    }

    async with AsyncClient(headers=HEADERS) as client:
        response = await client.get(configs.sslwireless_base_url, params=params)
        try:
            response = parse_xml_response(response.content.decode("utf-8"))
        except AttributeError as err:
            logging.exception(err)
            raise err
        else:
            logging.info(f"SUCCESS: SMS Response RAW : {response.json()}")
            return response
