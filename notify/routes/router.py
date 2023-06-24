from fastapi import APIRouter

from notify.routes.api_v1 import healthcheck

app_router = APIRouter(prefix="", tags=["Base"])

app_router.include_router(healthcheck.router)
