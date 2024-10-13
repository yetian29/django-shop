

from polyfactory.factories import DataclassFactory
from src.apps.product.domain.commands.product import GetProductCommand, GetProductListCommand
from src.apps.product.domain.entities.product import CatalogProduct, DetailProduct


class CatalogProductFactory(DataclassFactory[CatalogProduct]):
    __model__ = CatalogProduct


class DetailProductFactory(DataclassFactory[DetailProduct]):
    __model__ = DetailProduct
    

class GetPoruductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand

class GetPoruductListCommandFactory(DataclassFactory[GetProductListCommand]):
    __model__ = GetProductListCommand