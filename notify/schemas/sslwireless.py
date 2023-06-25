from typing import Any, Dict, Mapping, Optional

from pydantic import root_validator

from notify.schemas import BaseSchema


class SSLWirelessResponse(BaseSchema):
    params_status: bool
    login_status: bool
    push_api_status: bool = False
    stakeholder_status: bool = False
    permitted: bool = False
    msisdn: Optional[str] = None
    sms_body: Optional[str] = None
    csms_id: Optional[str] = None
    reference_id: Optional[str] = None

    @root_validator(pre=True)
    @classmethod
    def _validate_args(cls, values: Dict[str, Any]) -> Mapping[str, Any]:
        boolean_fields = [
            "params_status",
            "login_status",
            "push_api_status",
            "stakeholder_status",
            "permitted",
        ]

        for field in boolean_fields:
            if field in values:
                values[field] = values[field] in {
                    "OK",
                    "SUCCESSFULL",
                    "ACTIVE",
                }

        return values
