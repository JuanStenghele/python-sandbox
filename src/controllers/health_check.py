from fastapi import APIRouter
from constants import Tags


router = APIRouter()


@router.get("/health-check", tags = [Tags.HEALTH_CHECK])
def health_check():
  return {
    "message": "ok"
  }
