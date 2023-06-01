from typing import Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.role import RoleSchemaBase
from ..services.role import get_all
from ..db import get_db
from ..dependencies import auth_checker


roles_router = APIRouter(prefix="/roles", tags=["Roles"])


@roles_router.get(
    "",
    response_model=list[RoleSchemaBase],
    dependencies=[Depends(auth_checker)],
    tags=["Admin"],
)
async def get_all_roles(
    db: Annotated[AsyncSession, Depends(get_db)], limit: int | None = Query(None, gt=0)
):
    return await get_all(db, limit)
