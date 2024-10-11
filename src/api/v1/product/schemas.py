from uuid import UUID
from ninja import Schema, Field
from src.apps.product.domain.entities import CatalogProduct, DetailProduct
from src.apps.product.domain.values_object import GenderEnum
from src.apps.product.domain.entities import CatalogProductSortFieldsEnum
from src.apps.product.domain.command import GetProductListCommand, PaginationQuery, SortOrderEnum, SortQuery, FilterQuery 


class CatalogProductQueryParams(Schema):
    # search
    search: str | None = None
    # filter
    category: list[UUID] = Field(default_factory=list)
    brands: list[UUID] = Field(default_factory=list)
    colors: list[UUID] = Field(default_factory=list)
    sizes: list[UUID] = Field(default_factory=list)
    gender: GenderEnum | None = None
    # sort
    sort_field: CatalogProductSortFieldsEnum = CatalogProductSortFieldsEnum.oid # type: ignore
    sort_order: SortOrderEnum = SortOrderEnum.asc
    # pagination
    page: int = 0
    limit: int = 20
    
    def to_command(self) -> GetProductListCommand:
        return GetProductListCommand(
            filter=FilterQuery(
                category=self.category,
                brands=self.brands,
                colors=self.colors,
                sizes=self.sizes,
                gender=self.gender
            ),
            sort=SortQuery(
                sort_field=self.sort_field.value,
                sort_order=self.sort_order
            ),
            pagination=PaginationQuery(
                page=self.page,
                limit=self.limit
            )
        )

class CatalogProductOutSchema(Schema):
    oid: UUID
    name: str
    price: int
    sold: int
    place_sell: list[str]

    @staticmethod
    def from_entity(product: CatalogProduct) -> "CatalogProductOutSchema":
        return CatalogProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            sold=product.sold,
            place_sell=[place_sell.name for place_sell in product.places_sell]
        )
    
class DetailProductOutSchema(Schema):
    oid: UUID
    name: str
    description: str
    price: int
    brand: str
    colors: list[str]
    sizes: list[str]
    quantity: int


    @staticmethod
    def from_entity(product: DetailProduct) -> "DetailProductOutSchema":
        return DetailProductOutSchema(
            oid=product.oid,
            name=product.name,
            description=product.description,
            price=product.price,
            brand=product.brand.name,
            colors=[color.name for color in product.colores],
            sizes=[size.name for size in product.sizes],
            quantity=product.quantity
        )