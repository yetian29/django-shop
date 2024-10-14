from datetime import datetime
from uuid import UUID, uuid4

from ninja import Schema, Field

from src.apps.user.domain.entities import User

from pydantic import field_validator, model_validator

import re

class AuthorizeInSchema(Schema):
    phone_number: str | None = Field(default=None)
    email: str | None = Field(default=None)


    @field_validator("phone_number")
    def validate_phone_number(cls, value):       
        if value == "":
            value = None
            return value

        # Loại bỏ khoảng trắng và ký tự đặc biệt
        cleaned_number = re.sub(r'[\s\-\(\)]', '', value)
        if not cleaned_number.isdigit():
            raise ValueError("Số điện thoại chỉ được chứa chữ số")
        if len(cleaned_number) < 10 or len(cleaned_number) > 10:
            raise ValueError("Độ dài số điện thoại không hợp lệ")
        return cleaned_number 

    @field_validator("email")
    def validate_email(cls, value):
        if value == "":
            value = None
            return value
        
        # Một regex đơn giản để kiểm tra email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Email không hợp lệ")
        return value
    
    @model_validator(mode="after")
    def check_phone_or_email(cls, values):
        phone_number = values.phone_number
        email = values.email
        if not phone_number and not email:
            raise ValueError("Cần cung cấp số điện thoại hoặc email để đăng nhập")
        if phone_number and email:
            raise ValueError("Không được phép đăng nhập đồng thời số điện thoại và email")
        return values
    
        
    def to_entity(
        self,
        oid: UUID = uuid4,
        token: UUID = None,
        is_active: bool = False,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> User:
        return User(
            oid=oid,
            phone_number=self.phone_number,
            email=self.email,
            token=token,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
        )


class AuthorizeOutSchema(Schema):
    message: str



class LoginInSchema(Schema):
    phone_number: str | None = Field(default=None)
    email: str | None = Field(default=None)
    code: str 
    
    @field_validator("phone_number")
    def validate_phone_number(cls, value):       
        if value == "":
            value = None
            return value

        # Loại bỏ khoảng trắng và ký tự đặc biệt
        cleaned_number = re.sub(r'[\s\-\(\)]', '', value)
        if not cleaned_number.isdigit():
            raise ValueError("Số điện thoại chỉ được chứa chữ số")
        if len(cleaned_number) < 10 or len(cleaned_number) > 10:
            raise ValueError("Độ dài số điện thoại không hợp lệ")
        return cleaned_number 

    @field_validator("email")
    def validate_email(cls, value):
        if value == "":
            value = None
            return value
        
        # Một regex đơn giản để kiểm tra email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Email không hợp lệ")
        return value
    
    @model_validator(mode="after")
    def check_phone_or_email(cls, values):
        phone_number = values.phone_number
        email = values.email
        if not phone_number and not email:
            raise ValueError("Cần cung cấp số điện thoại hoặc email để đăng nhập")
        if phone_number and email:
            raise ValueError("Không được phép đăng nhập đồng thời số điện thoại và email")
        return values
    
class LoginOutSchema(Schema):
    token: UUID 
