from fastapi import APIRouter, Depends
from constants import Tags
from objects.health_check import HealthCheckResponse
from dal.health_check_dal import HealthCheckDAL
from dependency_injector.wiring import inject, Provide
from inject import Container
from sqlmodel import Session
from controllers.dependencies import get_session


router = APIRouter()


@router.get("/health-check", response_model = HealthCheckResponse, tags = [Tags.HEALTH_CHECK])
@inject
def health_check(
  session: Session = Depends(get_session),
  health_check_dal: HealthCheckDAL = Depends(Provide[Container.health_check_dal])
):
  return HealthCheckResponse(
    api = "ok",
    postgres_database = health_check_dal.health_check(session)
  )
