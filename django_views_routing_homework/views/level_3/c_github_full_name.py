"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from dataclasses import dataclass
from http import HTTPStatus

import httpx
from django.http import HttpRequest, HttpResponse, JsonResponse


@dataclass
class GitHubUserFetcher:
    username: str

    def __call__(
        self,
    ) -> str | None:
        response: httpx.Response = httpx.get(
            f"https://api.github.com/users/{self.username}"
        )
        response.raise_for_status()
        response_data = response.json()
        if "name" not in response_data:
            return None
        return response_data["name"] or "None"


def fetch_name_from_github_view(
    request: HttpRequest,
    github_username: str,
) -> HttpResponse:
    name: str | None = GitHubUserFetcher(github_username)()
    if not name:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)

    return JsonResponse({"name": name})
