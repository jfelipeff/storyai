from fastapi import APIRouter, Depends
from ..schemas import user
from ..db_config.config import create_all_tables, get_async_session


router = APIRouter()

async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

@router.get("/queries", response_model=list[user.PostRead])
async def list_queries(
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Post]:
    skip, limit = pagination
    select_query = select(Post).offset(skip).limit(limit)
    result = await session.execute(select_query)

    return result.scalars().all()
