
from abc import ABC, abstractmethod
import random

from src.apps.user.domain.entities import User # type: ignore



class ICodeService(ABC):
    @abstractmethod
    def generate_code(self, user: User) -> str:  
        pass    
       
    
        
        