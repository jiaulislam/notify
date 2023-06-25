from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from notify.routes import router
from notify.util import metadata

API_VERSION_V1 = "/api/v1"

description = """
![Notify API](https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png)

    PLIL Notify API helps send notifications to customers with SMS/Email. 🚀

## 📱 SMS
- You can **send sms** to customer phone number.
- Get Recent **sent sms** list (last 100 sms).
- Send bulk sms.

## 📤 Email

You can **send email** to customer email address.

"""

app = FastAPI(
    version="0.1.0",
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


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PLIL Notify",
        version="0.1.0",
        description=description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png"
    }
    openapi_schema["info"]["x-logo"]["altText"] = "Pragati Life Banner"
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
