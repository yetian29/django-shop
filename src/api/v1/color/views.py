import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.color.schemas import ColorOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.product.domain.use_cases.color import GetColorsUseCase
from src.core.containers import get_container

router = Router()


@router.get("", response=ApiResponse[ColorOutSchema])
def get_colors_views(request: HttpRequest) -> ApiResponse[ColorOutSchema]:
    container: punq.Container = get_container()
    use_case: GetColorsUseCase = container.resolve(GetColorsUseCase)
    colors = use_case.execute()
    return ApiResponse(data=[ColorOutSchema.from_entity(color) for color in colors])
