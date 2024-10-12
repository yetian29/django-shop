from src.apps.base.domain.entities import BaseDataField
from src.apps.base.infrastructure.models import BaseDataFieldORM


class SizeORM(BaseDataFieldORM):
    def __str__(self):
        return self.name
    
    def to_entity(self) -> BaseDataField:
        return BaseDataField(
            oid=self.oid,
            name=self.name
            
        )