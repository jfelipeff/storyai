import contextlib
from fastapi import Depends, FastAPI, HTTPException, Query, status

from chapter06.sqlalchemy.database import create_all_tables, get_async_session
from .routers import users

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
