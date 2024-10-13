# Category
import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.category.schemas import CategoryOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.product.domain.use_cases.category import GetCategoriesUseCase
from src.core.containers import get_container

router = Router()


@router.get("", response=ApiResponse[CategoryOutSchema])
def get_categories_views(request: HttpRequest) -> ApiResponse[CategoryOutSchema]:
    container: punq.Container = get_container()
    use_case: GetCategoriesUseCase = container.resolve(GetCategoriesUseCase)
    categories = use_case.execute()
    return ApiResponse(
        data=[CategoryOutSchema.from_entity(category) for category in categories]
    )
