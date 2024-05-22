from django.http import HttpRequest, HttpResponse

from django_views_routing_homework.services.user_getter import UserNameGetter

"""
У нас есть вьюха welcome_user_view, в которой должно формироваться приветствие, а формируется прощание.

Задания:
    1. Исправьте вьюху welcome_user_view таким образом, чтобы юзер видел приветствие, а не прощание.
    2. Проверьте результат по ссылке тут http://127.0.0.1:8000/welcome/
"""


def welcome_user_view(request: HttpRequest) -> HttpResponse:
    "Welcome view."
    user_name = UserNameGetter(request)()
    welcome_message = f"Welcome, {user_name}"
    return HttpResponse(welcome_message)
