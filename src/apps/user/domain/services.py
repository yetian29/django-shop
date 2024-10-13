
from abc import ABC, abstractmethod
import random

from src.apps.user.domain.entities import User # type: ignore



class ICodeService(ABC):
    @abstractmethod
    def generate_code(self, user: User) -> str:  
        pass    
    
    @abstractmethod
    def validate_code(self, code: str) -> None:
        pass
       
class ISendService(ABC):
    @abstractmethod
    def send_code(self, user: User, code: str) -> None:
        pass
        if user.phone_number:
            print(f"The Code <{code}> has sent to phone number: <{user.phone_number}>")
        if user.email:
            print(f"The code <{code}> has sent to email: <{user.email}>")
        
        