from fastapi import FastAPI

from notify.routes import router
from notify.util import metadata

API_VERSION_V1 = "/api/v1"

description = """
PLIL Notify API helps send notifications to customers with SMS/Email. 🚀

## 📱 SMS
- You can **send sms** to customer phone number.
- Get Recent **sent sms** list (last 100 sms).
- Send bulk sms.

## 📤 Email

You can **send email** to customer phone number.

"""

app = FastAPI(
    version="0.1.0",
    title="PLIL Notify Service",
    openapi_tags=metadata.metadata_tags,
    openapi_url=f"{API_VERSION_V1}/openapi.json",
    docs_url=f"{API_VERSION_V1}/docs",
    redoc_url=f"{API_VERSION_V1}/redoc",
    description=description,
    contact={
        "name": "Jiaul Islam Jibon",
        "url": "https://jiaulislam.github.io",
        "email": "jiaulislam.ict.bd@gmail.com",
    },
)

app.include_router(router.app_router, prefix=API_VERSION_V1)
