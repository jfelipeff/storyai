from datetime import datetime
from pydantic import BaseModel, Field


class QueryBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class QueryPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class QueryCreate(QueryBase):
    pass


class QueryRead(QueryBase):
    id: int
