# Бэк для фронта

## **В проекте:**

- База данных с треками, разделенных по категориям.
- Логика на Django.
- Cборка проекта с помощью Docker-compose.
- Авторизация пользователей по JWT.
- Аудиофайлы хранятся в django_media.

----

### Примеры запросов:

1. Пользователи

| Описание запроса       | Пример                | 
| ------------- |:------------------:| 
| _Зарегистрироваться_    |  POST - http://127.0.0.1:8000/user/signup/    | 
| _Войти_   | POST - http://127.0.0.1:8000/user/login/ | 
| _Получить ключ_  | POST - http://127.0.0.1:8000/user/token/     | 
| _Обновить ключ_ | POST - http://127.0.0.1:8000/user/token/refresh/    | 


body.json:

{
    "username":"stasy",
    "email":"an@mail.ru",
    "password":"Gfhjkm3434"
}

----
2. Треки


| Описание запроса       | Пример                | 
| ------------- |:------------------:| 
| _Получить все треки_    |  GET - http://127.0.0.1:8000/catalog/track/all/   | 
| _Получить трек по id_   | GET - http://127.0.0.1:8000/catalog/track/<id>/ | 
| _Получить трек по названию_  | GET - http://127.0.0.1:8000/catalog/track/<name>/     | 
| _Добавить трек в избранное по id_  | POST - http://127.0.0.1:8000/catalog/track/<int:pk>/favorite/    | 
| _Удалить трек из избранного по id_  | DELETE - http://127.0.0.1:8000/catalog/track/<int:pk>/favorite/    | 
| _Добавить треки в избранное по id_  | POST - http://127.0.0.1:8000/catalog/track/favorite?id = <int:pk>,<int:pk>/   | 
| _Удалить треки из избранного по id_  | DELETE - http://127.0.0.1:8000/catalog/track/<int:pk>/favorite/    | 
| _Добавить треки из избранного по id_  | POST - http://127.0.0.1:8000/catalog/track/favorite?id = <int:pk>,<int:pk>/   |
| _Просмотреть подборки_  | GET - http://127.0.0.1:8000/catalog/selection/     | 
| _Просмотреть подборку по id_  | GET - http://127.0.0.1:8000/catalog/selection/<int:pk>/     | 
| _Удалить трек из подборки по id_  | DELETE - http://127.0.0.1:8000/catalog/track/<int:pk>/delete/    | 
| _Добавить трек в подборку по id_  | POST - http://127.0.0.1:8000/catalog/<int:pk>/update/ | 
---






