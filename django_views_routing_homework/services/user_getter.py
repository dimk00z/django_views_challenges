from dataclasses import dataclass

from django.http import HttpRequest


@dataclass
class UserNameGetter:
    request: HttpRequest

    def __call__(self) -> str:
        user_name = (
            self.request.user.username
            if self.request.user.is_authenticated
            else "Anonymous"
        )
        return user_name
