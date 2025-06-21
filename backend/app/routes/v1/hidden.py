from fastapi import APIRouter
from scalar_fastapi import get_scalar_api_reference
import app.app as APP

router = APIRouter()

@router.get("/docs", include_in_schema=False)
async def scalar_html() -> None:
    """Документация Scalar /api/v1/docs"""
    return get_scalar_api_reference(
        openapi_url=APP.root.openapi_url,
        title=APP.root.title,
    )