from django.http import HttpRequest, HttpResponse

from django_views_routing_homework.services.user_getter import UserNameGetter

"""
В этой вьюхе мы хотим проверять забанен ли юзернэйм или нет.

Задания:
    1. Если юзернэйм в списке забаненных BANNED_USERNAMES, то возрващайте сообщение: User banned,
       иначе возвращайте сообщение: User not banned
    2. Результат проверяйте по ссылке http://127.0.0.1:8000/banned/тут интересующий юзернэйм/, 
       например http://127.0.0.1:8000/banned/any_username/
"""
BANNED_USERNAMES = ["red_dev", "green_bear", "monster"]


def is_username_banned_view(
    request: HttpRequest,
    username: str,
) -> HttpResponse:
    # код писать тут

    return (
        HttpResponse("User not banned")
        if username not in BANNED_USERNAMES
        else HttpResponse("User banned")
    )
