from uuid import UUID

from ninja import Field, Schema 

from src.apps.product.domain.commands.product import (
    FilterQuery,
    GetProductListCommand,
    PaginationQuery,
    SortOrderEnum,
    SortQuery,
)
from src.apps.product.domain.entities.product import (
    CatalogProduct,
    CatalogProductSortFieldsEnum,
    DetailProduct,
)
from src.apps.product.domain.values_object.gender import GenderEnum


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
    sort_field: CatalogProductSortFieldsEnum = CatalogProductSortFieldsEnum.oid  
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
                gender=self.gender,
            ),
            sort=SortQuery(
                sort_field=self.sort_field.value, sort_order=self.sort_order
            ),
            pagination=PaginationQuery(page=self.page, limit=self.limit),
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
            place_sell=[place_sell.name for place_sell in product.places_sell],
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
    def from_entity(entity: DetailProduct) -> "DetailProductOutSchema":
        return DetailProductOutSchema(
            oid=entity.oid,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            brand=entity.brand.name,
            colors=[color.name for color in entity.colors],
            sizes=[size.name for size in entity.sizes],
            quantity=entity.quantity,
        )
