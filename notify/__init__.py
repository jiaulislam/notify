import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from notify.routes import router
from notify.util.metadata import description, metadata_tags

API_VERSION_V1 = "/api/v1"


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Notify",
        version="0.1.0",
        description=description,
        routes=app.routes,
        tags=metadata_tags,
        contact={
            "name": "Jiaul Islam Jibon",
            "url": "https://jiaulislam.github.io",
            "email": "jiaulislam.ict.bd@gmail.com",
        },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://pragatilife.com/images/banners/pragati-Life-Ins-Logo-Eng.png"
    }
    openapi_schema["info"]["x-logo"]["altText"] = "Pragati Life Banner"
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(
    openapi_url=f"{API_VERSION_V1}/openapi.json",
    docs_url=f"{API_VERSION_V1}/docs",
    redoc_url=f"{API_VERSION_V1}/redoc",
)

app.include_router(router.app_router, prefix=API_VERSION_V1)


app.openapi = custom_openapi


if __name__ == "__main__":
    uvicorn.run("notify:app", host="127.0.0.1", port=8000)
