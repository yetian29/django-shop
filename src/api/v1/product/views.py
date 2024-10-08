from ninja import Router
from django.http import HttpRequest

from src.api.v1.product.schemas import ProductOutSchema
from src.api.v1.schemas import ApiResponse, PaginatedListResponse, PaginationOutSchema
from src.apps.product.domain.commans import GetProductListCommand, PaginationQuery, SortOrderEnum, SortQuery
from src.apps.product.domain.use_cases import GetProductListUseCase
from src.core.containers import get_container
from src.apps.product.domain.entities import CatalogProductSortFieldsEnum
import punq # type: ignore


router = Router()

def get_sort(
    sort_field: CatalogProductSortFieldsEnum = CatalogProductSortFieldsEnum.oid,   # type: ignore
    sort_order: SortOrderEnum = SortOrderEnum.asc
    ) -> SortQuery:
    return SortQuery(
        sort_field=sort_field.value,
        sort_order=sort_order
    )
 
def get_pagination(
    page: int = 0,
    limit: int = 20
) -> PaginationQuery:
    return PaginationQuery(
        page=page,
        limit=limit
    ) 
      
def get_post_list_command_factory(
    search: str | None = None,
    sort: SortQuery = get_sort(),
    pagination: PaginationQuery = get_pagination()
    
    ) -> GetProductListCommand:
    return GetProductListCommand(
        search=search,
        sort=sort,
        pagination=pagination
    )
@router.get("")
def find_many_products_views(
    request: HttpRequest,
    command: GetProductListCommand = get_post_list_command_factory(),
) -> ApiResponse[PaginatedListResponse[ProductOutSchema]]:
    container: punq.Container = get_container()
    use_case: GetProductListUseCase = container.resolve(GetProductListUseCase)
    products, count = use_case.execute(command=command)
    return ApiResponse(
        data=PaginatedListResponse(
            items=[ProductOutSchema.from_entity(product) for product in products],
            pagination=PaginationOutSchema(
                page=command.pagination.page,
                limit=command.pagination.limit,
                total=count
            )
        )
    )