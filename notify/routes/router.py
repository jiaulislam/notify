from fastapi import APIRouter

from notify.routes.api_v1 import email, healthcheck

app_router = APIRouter()

app_router.include_router(healthcheck.router)
app_router.include_router(email.router)
