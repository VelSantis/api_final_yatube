API project
---
Разработка приложения API к проекту блога с постами, сообществами, комментариями и системами подписок.

Как запустить проект:
---

1.Клонировать репозиторий:

    git@github.com:VelSantis/api_final_yatube.git

2.Cоздать и активировать виртуальное окружение:

    python -m venv env
    source venv/Scripts/activate

3.Установить зависимости из файла requirements.txt:

    pip install -r requirements.txt

4.Из директории yatube_api запустить сервер:

    python manage.py runserver

Запуск тестов
---
Находясь в главной папке проекта, где есть папка tests, при активированном виртуальном окружении выполнить

    pytest

Технологии:
---
    Python 3.9.10
    
    Django

    Django REST Framework

    JWT аутенфикация (Djoser)

    Динамическая документация Swagger

    Тестирование API в Postman

Примеры запросов к API
---
Подробная документация по работе API:

    http://127.0.0.1:8000/redoc/
Получить список всех постов (GET):

    http://127.0.0.1:8000/api/v1/posts/
Создать новый пост (POST):

    http://127.0.0.1:8000/api/v1/posts/

Автор
---
Кирилюк Андрей

    https://github.com/VelSantis