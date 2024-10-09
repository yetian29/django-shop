from uuid import UUID
from ninja import Schema
from src.apps.product.domain.entities import CatalogProduct, DetailProduct


class CatalogProductOutSchema(Schema):
    oid: UUID
    name: str
    price: int
    sold: str
    place_sell: str

    @staticmethod
    def from_entity(product: CatalogProduct) -> "CatalogProductOutSchema":
        return CatalogProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            sold=product.sold,
            place_sell=product.place_sell.name
        )
    
class DetailProductOutSchema(Schema):
    oid: UUID
    name: str
    price: int
    brand: str
    color: list[str]
    size: list[str]
    quantity: int


    @staticmethod
    def from_entity(product: DetailProduct) -> "DetailProductOutSchema":
        return DetailProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            brand=product.brand.name,
            color=product.color.name,
            size=product.size.name,
            quantity=product.quantity
        )
    