# pyright: reportOptionalMemberAccess=false

import xml.etree.ElementTree as ET

from notify.schemas.sslwireless import SSLWirelessResponse


def parse_xml_response(xml_content: str) -> SSLWirelessResponse:
    root = ET.fromstring(xml_content)
    params_status = root.find("PARAMETER").text
    login_status = root.find("LOGIN").text
    push_api_status = root.find("PUSHAPI").text
    stakeholder_status = root.find("STAKEHOLDERID").text
    permitted = root.find("PERMITTED").text
    sms_info = root.find("SMSINFO")
    msisdn = sms_info.find("MSISDN").text
    sms_body = sms_info.find("SMSTEXT").text
    csms_id = sms_info.find("CSMSID").text
    reference_id = sms_info.find("REFERENCEID").text

    if not params_status or not login_status:
        return SSLWirelessResponse(params_status=False, login_status=False)

    return SSLWirelessResponse(
        **{
            "params_status": params_status,
            "login_status": login_status,
            "push_api_status": push_api_status,
            "stakeholder_status": stakeholder_status,
            "permitted": permitted,
            "msisdn": msisdn,
            "sms_body": sms_body,
            "csms_id": csms_id,
            "reference_id": reference_id,
        }  # type: ignore
    )
