import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.schemas import ApiResponse
from src.api.v1.user.schemas import AuthorizeInSchema, AuthorizeOutSchema
from src.apps.user.domain.commands import AuthorizeUserCommand
from src.apps.user.domain.use_cases import AuthorizeUserUseCase
from src.core.containers import get_container

router = Router()


@router.post("", response=ApiResponse[AuthorizeOutSchema])
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
