"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""

import json
from enum import StrEnum
from http import HTTPStatus

from django import forms
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST


class RegisteredFrom(StrEnum):
    WEBSITE = "website"
    MOBILE_APP = "mobile_app"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class UserForm(forms.Form):
    full_name = forms.CharField(min_length=5, max_length=256)
    email = forms.EmailField()
    registered_from = forms.ChoiceField(choices=RegisteredFrom.choices)
    age = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=150,
    )


@require_POST
def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    form = UserForm(data)
    if not form.is_valid():
        return JsonResponse(
            data={"is_valid": False, "errors": form.errors},
            status=HTTPStatus.BAD_REQUEST,
        )
    return JsonResponse(
        data={"is_valid": True},
        status=HTTPStatus.BAD_REQUEST,
    )
