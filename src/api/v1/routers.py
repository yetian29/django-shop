from ninja import NinjaAPI  # type: ignore

from src.api.v1.brand.views import router as brand_router
from src.api.v1.category.views import router as category_router
from src.api.v1.product.views import router as product_router

api_v1 = NinjaAPI(docs_url="/api/v1/docs")


api_v1.add_router("/product", product_router, tags=["product"])
api_v1.add_router("/category", category_router, tags=["category"])
api_v1.add_router("/brand", brand_router, tags=["brand"])
