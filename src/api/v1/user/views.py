import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.schemas import ApiResponse
from src.api.v1.user.schemas import (
    AuthorizeInSchema,
    AuthorizeOutSchema,
    LoginInSchema,
    LoginOutSchema,
)
from src.apps.user.domain.commands import AuthorizeUserCommand, LoginUserCommand
from src.apps.user.domain.use_cases import AuthorizeUserUseCase, LoginUserUseCase
from src.core.containers import get_container

router = Router()


@router.post("/authorize", response=ApiResponse[AuthorizeOutSchema])
def authorize_user_views(
    request: HttpRequest, user_in: AuthorizeInSchema
) -> ApiResponse[AuthorizeOutSchema]:
    container: punq.Container = get_container()
    use_case: AuthorizeUserUseCase = container.resolve(AuthorizeUserUseCase)
    command = AuthorizeUserCommand(user=user_in.to_entity())
    code = use_case.execute(command=command)
    if command.user.phone_number:
        message = f"The code <{code}> has been sent to phone number <{command.user.phone_number}>"
    else:
        if command.user.email:
            message = f"The code <{code}> has been sent to email <{command.user.email}>"

    return ApiResponse(data=AuthorizeOutSchema(message=message))


@router.post("/login", response=ApiResponse[LoginOutSchema])
def login_user_views(
    request: HttpRequest, login_in: LoginInSchema
) -> ApiResponse[LoginOutSchema]:
    container: punq.Container = get_container()
    use_case: LoginUserUseCase = container.resolve(LoginUserUseCase)
    command = LoginUserCommand(
        phone_number=login_in.phone_number, email=login_in.email, code=login_in.code
    )
    token = use_case.execute(command=command)
    return ApiResponse(data=LoginOutSchema(token=token))
