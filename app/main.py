from fastapi import FastAPI

from app.routers import done, healthcheck, task

app = FastAPI()
app.include_router(task.router, tags=["task"])
app.include_router(done.router, tags=["done"])
app.include_router(healthcheck.router, tags=["healthcheck"])
