import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.brand.schemas import BrandOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.product.domain.use_cases.brand import GetBrandsUseCase
from src.core.containers import get_container

router = Router()


@router.get("", response=ApiResponse[BrandOutSchema])
def get_brands_views(request: HttpRequest) -> ApiResponse[BrandOutSchema]:
    container: punq.Container = get_container()
    use_case: GetBrandsUseCase = container.resolve(GetBrandsUseCase)
    brands = use_case.execute()
    return ApiResponse(data=[BrandOutSchema.from_entity(brand) for brand in brands])
