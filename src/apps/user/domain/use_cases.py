from dataclasses import dataclass
from uuid import UUID

from src.apps.user.domain.commands import AuthorizeUserCommand, LoginUserCommand
from src.apps.user.domain.services import (
    ICodeService,
    ILoginService,
    ISendService,
    IUserService,
)


@dataclass
class AuthorizeUserUseCase:
    code_service: ICodeService
    send_service: ISendService
    user_service: IUserService

    def execute(self, command: AuthorizeUserCommand) -> str:
        self.user_service.get_or_create(user=command.user)
        code = self.code_service.generate_code(user=command.user)
        self.send_service.send_code(user=command.user, code=code)
        return code


@dataclass
class LoginUserUseCase:
    code_service: ICodeService
    login_service: ILoginService
    user_service: IUserService

    def execute(self, command: LoginUserCommand) -> UUID:
        user = self.user_service.get_by_phone_number_or_email(
            phone_number=command.phone_number, email=command.email
        )
        self.code_service.validate_code(user=user, code=command.code)
        token = self.login_service.active_and_genarate_token(user=user)
        self.user_service.update(user=user)
        return token
