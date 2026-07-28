"""Health check routes for service readiness and liveness."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ai_solutions_platform.persistence.database import get_db_session

router = APIRouter(tags=["health"])


@router.get("/healthz/ready", status_code=status.HTTP_200_OK)
async def readiness_probe(session: AsyncSession = Depends(get_db_session)):
    """Return 200 OK if PostgreSQL connection is healthy, else 503."""
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database unready: {str(exc)}",
        )

