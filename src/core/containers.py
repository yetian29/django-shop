from functools import lru_cache
import punq
from src.apps.product.domain.services.category import ICategoryService
from src.apps.product.domain.services.product import IProductService
from src.apps.product.domain.use_cases.category import GetCategoriesUseCase
from src.apps.product.domain.use_cases.product import GetProductListUseCase, GetProductUseCase
from src.apps.product.infrastructure.repositories.category import ICategoryRepository, PostgresCategoryRepository
from src.apps.product.infrastructure.repositories.product import IProductRepository, PostgresProductRepository
from src.apps.product.services.category import CategoryService
from src.apps.product.services.product import ProductService


@lru_cache(1)
def get_container() -> punq.Container:
    return init_container()

def init_container() -> punq.Container:
    container = punq.Container()

    container.register(IProductRepository, PostgresProductRepository)
    container.register(IProductService, ProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    container.register(ICategoryRepository, PostgresCategoryRepository)
    container.register(ICategoryService, CategoryService)
    container.register(GetCategoriesUseCase)
    return container