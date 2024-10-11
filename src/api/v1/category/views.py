from ninja import Router
from src.api.v1.category.schemas import CategoryOutSchema
from src.api.v1.schemas import ApiResponse
from django.http import HttpRequest

from src.apps.category.domain.use_cases import GetCategoriesUseCase
import punq
from src.core.containers import get_container


router = Router()

@router.get("")
def get_categories_views(request: HttpRequest) -> ApiResponse[CategoryOutSchema]:
    container: punq.Container = get_container()
    use_case: GetCategoriesUseCase = container.resolve(GetCategoriesUseCase)
    categories = use_case.execute()
    return ApiResponse(
        data=[CategoryOutSchema.from_entity(cat) for cat in categories]
    )

    

