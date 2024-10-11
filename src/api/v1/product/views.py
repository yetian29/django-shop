from uuid import UUID
from ninja import Router, Query

from django.http import HttpRequest

from src.api.v1.product.schemas import CatalogProductOutSchema, CatalogProductQueryParams, DetailProductOutSchema
from src.api.v1.schemas import ApiResponse, PaginatedListResponse, PaginationOutSchema
from src.apps.product.domain.commands import GetProductCommand
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.core.containers import get_container
import punq # type: ignore


router = Router()

    
@router.get("")
def find_many_products_views(
    request: HttpRequest,
    params: CatalogProductQueryParams = Query(...)
) -> ApiResponse[PaginatedListResponse[CatalogProductOutSchema]]:
    command = params.to_command()
    container: punq.Container = get_container()
    use_case: GetProductListUseCase = container.resolve(GetProductListUseCase)
    products, count = use_case.execute(command=command)
    return ApiResponse(
        data=PaginatedListResponse(
            items=[CatalogProductOutSchema.from_entity(product) for product in products],
            pagination=PaginationOutSchema(
                page=command.pagination.page,
                limit=command.pagination.limit,
                total=count
            )
        )
    )

@router.get("/{oid}")
def get_product(
    request: HttpRequest,
    oid: UUID,
    ) -> ApiResponse[DetailProductOutSchema]:
    container: punq.Container = get_container()
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    command = GetProductCommand(oid=oid) 
    product = use_case.execute(command=command)
    return ApiResponse(
        data=DetailProductOutSchema.from_entity(product)
    )
    