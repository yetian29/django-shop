from uuid import UUID

import punq  # type: ignore
from django.http import HttpRequest
from ninja import Query, Router

from src.api.v1.product.schemas import (
    BrandOutSchema,
    CatalogProductOutSchema,
    CatalogProductQueryParams,
    CategoryOutSchema,
    DetailProductOutSchema,
)
from src.api.v1.schemas import ApiResponse, PaginatedListResponse, PaginationOutSchema
from src.apps.product.domain.commands.product import GetProductCommand
from src.apps.product.domain.use_cases.brand import GetBrandsUseCase
from src.apps.product.domain.use_cases.category import GetCategoriesUseCase
from src.apps.product.domain.use_cases.product import (
    GetProductListUseCase,
    GetProductUseCase,
)
from src.core.containers import get_container

router = Router()


# Product
@router.get("", response=ApiResponse[PaginatedListResponse[CatalogProductOutSchema]])
def find_many_products_views(
    request: HttpRequest, params: CatalogProductQueryParams = Query(...)
) -> ApiResponse[PaginatedListResponse[CatalogProductOutSchema]]:
    command = params.to_command()
    container: punq.Container = get_container()
    use_case: GetProductListUseCase = container.resolve(GetProductListUseCase)
    products, count = use_case.execute(command=command)
    return ApiResponse(
        data=PaginatedListResponse(
            items=[
                CatalogProductOutSchema.from_entity(product) for product in products
            ],
            pagination=PaginationOutSchema(
                page=command.pagination.page,
                limit=command.pagination.limit,
                total=count,
            ),
        )
    )


@router.get("/{oid}", response=ApiResponse[DetailProductOutSchema])
def get_product(
    request: HttpRequest,
    oid: UUID,
) -> ApiResponse[DetailProductOutSchema]:
    container: punq.Container = get_container()
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    command = GetProductCommand(oid=oid)
    product = use_case.execute(command=command)
    return ApiResponse(data=DetailProductOutSchema.from_entity(product))


# Category
@router.get("/categories", response=ApiResponse[CategoryOutSchema])
def get_categories_views(request: HttpRequest) -> ApiResponse[CategoryOutSchema]:
    container: punq.Container = get_container()
    use_case: GetCategoriesUseCase = container.resolve(GetCategoriesUseCase)
    categories = use_case.execute()
    return ApiResponse(
        data=[CategoryOutSchema.from_entity(category) for category in categories]
    )


# Brand
@router.get("/brands", response=ApiResponse[BrandOutSchema])
def get_brands_views(request: HttpRequest) -> ApiResponse[CategoryOutSchema]:
    container: punq.Container = get_container()
    use_case: GetBrandsUseCase = container.resolve(GetBrandsUseCase)
    brands = use_case.execute()
    return ApiResponse(data=[BrandOutSchema.from_entity(brand) for brand in brands])
