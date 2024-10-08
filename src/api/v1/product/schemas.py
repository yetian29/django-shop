from uuid import UUID
from ninja import Schema
from src.apps.product.domain.entities import CatalogProduct


class ProductOutSchema(Schema):
    oid: UUID
    name: str
    price: int
    sold: str
    place_sell: str

    @staticmethod
    def from_entity(product: CatalogProduct) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            sold=product.sold,
            place_sell=product.place_sell.name
        )
    
    