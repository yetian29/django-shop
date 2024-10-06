from ninja import Router
from django.http import HttpRequest

from src.api.v1.product.schemas import ProductOutSchema
from src.api.v1.schemas import ApiResponse, PaginatedListResponse
from src.apps.product.domain.commans import GetProductListCommand, PaginationQuery, SortOrderEnum, SortQuery
from src.core.containers import get_container
from src.apps.product.domain.entities import ProductSortFieldsList
import punq


router = Router()

def get_sort(
    sort_field: ProductSortFieldsList = ProductSortFieldsList.oid,  # type: ignore
    sort_order: SortOrderEnum = SortOrderEnum.asc
    ) -> SortQuery:
    return SortQuery(
        sort_field=sortfield,
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
    container: punq.Container = get_container(),
) -> ApiResponse[PaginatedListResponse[ProductOutSchema]]:
    pass