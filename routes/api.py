from fastapi import APIRouter
from src.controllers import kalori

router = APIRouter()
router.include_router(kalori.router)