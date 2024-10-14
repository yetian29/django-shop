import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.schemas import ApiResponse
from src.api.v1.size.schemas import SizeOutSchema
from src.apps.product.domain.use_cases.size import GetSizesUseCase
from src.core.containers import get_container

router = Router()


@router.get("", response=ApiResponse[SizeOutSchema])
def get_sizes_views(request: HttpRequest) -> ApiResponse[SizeOutSchema]:
    container: punq.Container = get_container()
    use_case: GetSizesUseCase = container.resolve(GetSizesUseCase)
    sizes = use_case.execute()
    return ApiResponse(data=[SizeOutSchema.from_entity(size) for size in sizes])
