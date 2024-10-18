from datetime import datetime, timedelta
import random

from src.apps.product.domain.commands.product import FilterQuery
from src.apps.product.domain.entities.product import CatalogProduct, DetailProduct
from src.apps.product.domain.services.product import IProductService
from src.apps.user.domain.entities import User
from src.apps.user.domain.services import ICodeService, IUserService
from src.apps.user.service.errors import CachedDataNotExistException, CodeNotFoundException, EqualCodesException, ExpiredCodeException
from test.mocks.product.factories import CatalogProductFactory, DetailProductFactory


class DummyProductService(IProductService):
    def get_by_id(self, oid: str) -> DetailProduct:
        return DetailProductFactory.build(oid=oid)

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        filter: FilterQuery,
        search: str | None = None,
    ) -> list[CatalogProduct]:
        return [CatalogProductFactory.build() for _ in range(random.randint(0, limit))]

    def count_many(self, filter: FilterQuery, search: str | None = None) -> int:
        return random.randint(0, 1000)


class DummyCodeService(ICodeService):
    cache = {}
    def generate_code(self, user: User) -> str:
        code = str(random.randint(100000, 999999))
        time_out = timedelta(milliseconds=1000)
        cached_data = {
            "code": code,
            "ttl": datetime.now() + time_out
        }
        if user.phone_number:
            self.cache[user.phone_number] = cached_data
        else:
            if user.email:
                self.cache[user.email] = cached_data
        return code
    
    def validate_code(self, user: User, code: str) -> None:
        if user.phone_number:
            try:
               cached_data = self.cache.get(user.phone_number)
            except:
               raise CachedDataNotExistException
            else:
                if not cached_data.get("code"):
                    del self.cache[user.phone_number]
                    raise CodeNotFoundException
               
                if datetime.now() > cached_data.get("ttl"):
                    del self.cache[user.phone_number]
                    raise ExpiredCodeException
                    
                if code != cached_data.get("code"):
                    del self.cache[user.phone_number]
                    raise EqualCodesException

                del self.cahe[user.phone_number]
        else:
            if user.emal:
                try:
                    cached_data = self.cache.get(user.email)
                except:
                    raise CachedDataNotExistException
                else:
                    if not cached_data.get("code"):
                        del self.cache[user.email]
                        raise CodeNotFoundException
                
                    if datetime.now() > cached_data.get("ttl"):
                        del self.cache[user.email]
                        raise ExpiredCodeException
                        
                    if code != cached_data.get("code"):
                        del self.cache[user.email]
                        raise EqualCodesException

                    del self.cache[user.email]
                
                
                
            


        
class DummyUserService(IUserService):
        