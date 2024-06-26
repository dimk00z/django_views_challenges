import json
from http import HTTPStatus

from django.core.exceptions import BadRequest
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

"""
В этой задаче у нас сразу две вьюхи.
authorization_view - просто отрисовывает страниц авторизации по ссылке http://127.0.0.1:8000/authorization/ . В ней мы ничего не меняем
process_authorization_view - обрабатывает заполненные данные на странице авторизации
и возвращает статус об успехе или неуспехе. С ней мы и будем работать

Задания:
    1. Откройте страницу по ссылке http://127.0.0.1:8000/authorization/
    2. Введите какие-нибудь данные, нажмите на кнопку и посмотрите на результат.
    3. Страница отправила во вьюху process_authorization_view данные, которые мы положили в переменную data.
       Распечатйте переменную data, чтобы посмотреть в каком формате хранятся входящие данные
    4. Допишите логику в process_authorization_view таким образом, что если юзернэйм есть
       в USERNAME_TO_PASSWORD_MAPPER и введенный пароль совпадает, то возвращайте JsonResponse со статусом 200.
       Если введенного юзернэйма нет, то возвращайте JsonResponse со статусом 403.
       Например JsonResponse(data={}, status=200) или JsonResponse(data={}, status=403)
    5. На странице вы увидете сообщение об успехе или неудаче.
"""
USERNAME_TO_PASSWORD_MAPPER = {
    "john_doe": "password123",
    "sarah_connor": "terminator2",
    "admin": "admin_pass",
    "coder2021": "qwerty",
    "happy_user": "12345",
    "l33t_h4ck3r": "leetpassword",
    "music_lover": "beethoven",
    "sports_fan": "goal2023",
    "travel_guru": "wanderlust",
}


def check_auth(username: str, password: str) -> bool:
    if username not in USERNAME_TO_PASSWORD_MAPPER:
        return False
    return USERNAME_TO_PASSWORD_MAPPER[username] == password


@require_POST
@csrf_exempt
def process_authorization_view(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if not any((username, password)):
        raise BadRequest("username and password are required")
    if not check_auth(username, password):
        return JsonResponse(data={}, status=HTTPStatus.FORBIDDEN)
    return JsonResponse(data={}, status=HTTPStatus.OK)


# не обращайте внимания на эту вьюху, она нужна лишь для отрисовки страницы авторизации
def authorization_view(request: HttpRequest) -> HttpResponse:
    return render(request, "authorization.html")
