"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.core.exceptions import BadRequest
from django.http import HttpRequest, StreamingHttpResponse
from faker import Faker

DEFAULT_LENGTH = 100
DEFAULT_CHUNK_SIZE = 1024
MAX_CHUNK_SIZE = 1024 * 1024 * 10


def generate_fake_text(fake: Faker, length: int):
    chunk_size = min(length, DEFAULT_CHUNK_SIZE)
    while length > 0:
        yield fake.text(max_nb_chars=length)
        length -= chunk_size


def generate_file_with_text_view(request: HttpRequest) -> StreamingHttpResponse:
    fake = Faker()
    fake.text()
    file_length: int = int(request.GET.get("length", DEFAULT_LENGTH))
    if file_length > MAX_CHUNK_SIZE:
        raise BadRequest("File length exceeds max length")
    file_name: str = request.GET.get("file_name", "text.txt")
    return StreamingHttpResponse(
        generate_fake_text(fake, file_length),
        content_type="text/plain",
        headers={
            "Content-Disposition": f'attachment; filename="{file_name}"',
        },
    )
