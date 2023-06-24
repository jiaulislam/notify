from typing import Mapping

from fastapi import APIRouter, status

from notify.enums import APIStatusEnum
from notify.schemas.healthcheck import (
    HealtCheckDown,
    HealtCheckUp,
    HealtCheckUpgradation,
)

router = APIRouter()


@router.get(
    "/",
    response_model=HealtCheckUp,
    response_description="<b>API is alive</b>",
    responses={
        status.HTTP_200_OK: {"model": HealtCheckUp},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": HealtCheckDown,
            "description": "<b>API is down</b>",
        },
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "model": HealtCheckUpgradation,
            "description": "<b>API Upgradation On-Going</b>",
        },
    },
    summary="API server health check route",
    description="This route is used to perform a health check on the API server.",
)
def healthcheck() -> Mapping[str, APIStatusEnum | str]:
    """
    Perform a health check on the API server.

    Returns:
        A response containing the API status and a message indicating whether the API is working correctly.
    """
    return {"api_status": APIStatusEnum.ALIVE, "message": "api is working ok"}
