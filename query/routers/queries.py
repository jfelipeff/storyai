from fastapi import APIRouter, Depends, Query
from ..schemas import user
from ..db_config.config import create_all_tables, get_async_session
from ..repository.query import QueryRepository


router = APIRouter()

async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

@router.post("/attendance/add")
async def add_attendance(req:QueryRepository ):
    async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = QueryRepository(sess)
            attendance = Attendance_Member(id=req.id, member_id=req.member_id, timein=req.timein, timeout=req.timeout, date_log=req.date_log)
            return await repo.insert_query(attendance)

@router.get("/queries", response_model=list[user.PostRead])
async def list_queries(
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Post]:
    skip, limit = pagination
    select_query = select(Post).offset(skip).limit(limit)
    result = await session.execute(select_query)

    return result.scalars().all()
