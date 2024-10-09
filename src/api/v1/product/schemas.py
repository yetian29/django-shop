from uuid import UUID
from ninja import Schema
from src.apps.product.domain.entities import CatalogProduct, DetailProduct


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
    colores: list[str]
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
            colores=[color.name for color in product.colores],
            sizes=[size.name for size in product.sizes],
            quantity=product.quantity
        )
    