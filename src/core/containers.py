from functools import lru_cache

import punq

from src.apps.product.domain.services.brand import IBrandService
from src.apps.product.domain.services.category import ICategoryService
from src.apps.product.domain.services.color import IColorService
from src.apps.product.domain.services.product import IProductService
from src.apps.product.domain.services.size import ISizeService
from src.apps.product.domain.use_cases.brand import GetBrandsUseCase
from src.apps.product.domain.use_cases.category import GetCategoriesUseCase
from src.apps.product.domain.use_cases.color import GetColorsUseCase
from src.apps.product.domain.use_cases.product import (
    GetProductListUseCase,
    GetProductUseCase,
)
from src.apps.product.domain.use_cases.size import GetSizesUseCase
from src.apps.product.infrastructure.repositories.brand import (
    IBrandRepository,
    PostgresBrandRepository,
)  # type: ignore
from src.apps.product.infrastructure.repositories.category import (
    ICategoryRepository,
    PostgresCategoryRepository,
)
from src.apps.product.infrastructure.repositories.color import IColorRepository, PostgresColorRepository
from src.apps.product.infrastructure.repositories.product import (
    IProductRepository,
    PostgresProductRepository,
)
from src.apps.product.infrastructure.repositories.size import ISizeRepository, PostgresSizeRepository
from src.apps.product.services.brand import BrandService
from src.apps.product.services.category import CategoryService
from src.apps.product.services.color import ColorService
from src.apps.product.services.product import ProductService
from src.apps.product.services.size import SizeService


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

    container.register(IBrandRepository, PostgresBrandRepository)
    container.register(IBrandService, BrandService)
    container.register(GetBrandsUseCase)
    
    
    container.register(ISizeRepository, PostgresSizeRepository)
    container.register(ISizeService, SizeService)
    container.register(GetSizesUseCase)

    container.register(IColorRepository, PostgresColorRepository)
    container.register(IColorService, ColorService)
    container.register(GetColorsUseCase)
    return container
