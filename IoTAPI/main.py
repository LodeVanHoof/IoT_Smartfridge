from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import get_endpoints, post_endpoints
app = FastAPI(docs_url=config.documentation_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins = config.origins.split(","),
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(get_endpoints.router)
app.include_router(post_endpoints.router)
