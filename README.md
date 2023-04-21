# homework_71_zulufov_ruslan
Данные админки:  
 Логин - root 
 Пароль - root  
  
# Инстукция к API  
### Аутентификация  
1. Отправить POST запрос по адресу http://127.0.0.1:8000/api/login/  
В body передать (изменяем тип передаваемых данных на JSON):  
{  
    "username": "root",  
    "password": "root"  
}  
Далее, копируем токен, заходим в Headers, в поле Key прописываем Authorization и в value вставляем Token <полученный токен> (без стрелок)  
  
### Для постов  
1. Просмотр постов  
GET http://127.0.0.1:8000/api/posts  
2. Детальный просмотр  
GET http://127.0.0.1:8000/api/posts/1  
3. Добавление поста  
POST http://127.0.0.1:8000/api/posts/  
В body передаём (изменяем тип передаваемых данных на JSON):  
{  
    "author": 1,  
    "description": "New Post"  
}  
4. Редактирование  
PUT http://127.0.0.1:8000/api/posts/1/  
В body передаём (изменяем тип передаваемых данных на JSON):  
  
{  
    "author": 1,  
    "description": "Change post"  
}  
  
5. Удаление  
DELETE http://127.0.0.1:8000/api/posts/1/  
  
### Для лайков  
1. Добавление лайка  
POST http://127.0.0.1:8000/api/likes/  
В body передаём (изменяем тип передаваемых данных на JSON):  
  
{  
    "user": 1,  
    "post": 3  
}  
  
2. Удаление лайка  
DELETE http://127.0.0.1:8000/api/likes/31/  
