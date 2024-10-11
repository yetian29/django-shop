from functools import lru_cache
import punq
from src.apps.category.domain.services import ICategoryService
from src.apps.category.domain.use_cases import GetCategoriesUseCase
from src.apps.category.infrastructure.repositories import ICategoryRepository, PostgresCategoryRepository
from src.apps.category.services.category import CategoryService
from src.apps.product.domain.services import IProductService
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.apps.product.infrastructure.repositories import IProductRepository, PostgresProductRepository
from src.apps.product.services.products import ProductService

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