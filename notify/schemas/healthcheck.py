from datetime import datetime

import pendulum
from pydantic import Field

from notify.enums import APIStatusEnum
from notify.schemas import BaseSchema


class BaseHealthCheck(BaseSchema):
    api_status: str = Field(..., example=APIStatusEnum.ALIVE)
    message: str = Field(..., example="api is working ok")
    timestamp: datetime = Field(default=pendulum.now(tz="Asia/Dhaka"))


class HealtCheckUp(BaseHealthCheck):
    pass


class HealtCheckDown(BaseHealthCheck):
    api_status: str = Field(..., example=APIStatusEnum.DEAD)
    message: str = Field(..., example="api server down")


class HealtCheckUpgradation(BaseHealthCheck):
    api_status: str = Field(..., example=APIStatusEnum.UPGRDATION_ONGOING)
    message: str = Field(
        ..., example="api is currently unavailable due to server upgradation going on."
    )
