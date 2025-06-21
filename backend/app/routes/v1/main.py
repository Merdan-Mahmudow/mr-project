from fastapi import APIRouter
from app.routes.v1.hidden import router as hidden
from app.routes.v1.auth import router as auth

router = APIRouter(prefix="/v1")

router.include_router(router=hidden)
router.include_router(router=auth)