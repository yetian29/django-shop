from ninja import NinjaAPI
from src.api.v1.product.views import router as product_router


api_v1 = NinjaAPI(
    docs_url="/api/v1/docs"
)


api_v1.add_router("/product", product_router, tags=["product"])


