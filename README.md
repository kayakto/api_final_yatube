# Yatube API

## Описание

Yatube API — проект социальной сети, где реализованы функции для публикации записей, комментирования и подписки на авторов.

## Стек технологий

- Python 3.12
- Django 3.2.16
- Django REST Framework (DRF)
- JWT + Djoser

## Запуск проекта в режиме разработки

1. Клонируйте репозиторий и перейдите в него в командной строке.
    ```bash
   git clone https://github.com/kayakto/api_final_yatube.git
   ```

2. Перейдите в директорию проекта
    ```bash
   cd api_final_yatube
   ```

2. Установите и активируйте виртуальное окружение (не ниже Python 3.9):

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Для Windows
   source venv/bin/activate      # Для macOS/Linux
   ```

3. Обновите pip и установите зависимости:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Выполните миграции и создайте суперпользователя:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

## Примеры работы с API для всех пользователей

Для неавторизованных пользователей API доступно только в режиме чтения. Создавать и изменять данные нельзя.

- Получение списка всех публикаций с пагинацией:

  ```http
  GET /api/v1/posts/?limit=5&offset=0
  ```

- Получение публикации по ID:

  ```http
  GET /api/v1/posts/{id}/
  ```

- Получение списка доступных сообществ:

  ```http
  GET /api/v1/groups/
  ```

- Получение информации о сообществе по ID:

  ```http
  GET /api/v1/groups/{id}/
  ```

- Получение всех комментариев к публикации:

  ```http
  GET /api/v1/{post_id}/comments/
  ```

- Получение комментария к публикации по ID:

  ```http
  GET /api/v1/{post_id}/comments/{id}/
  ```

## Примеры работы с API для авторизованных пользователей

Авторизованные пользователи могут создавать публикации, комментировать их и подписываться на других пользователей. Изменять и удалять можно только свои данные.

- Создание публикации:

  ```http
  POST /api/v1/posts/
  ```

  Body:

  ```json
  {
    "text": "string",
    "image": "string",
    "group": 0
  }
  ```

- Обновление публикации:

  ```http
  PUT /api/v1/posts/{id}/
  ```

  Body:

  ```json
  {
    "text": "string",
    "image": "string",
    "group": 0
  }
  ```

- Частичное обновление публикации:

  ```http
  PATCH /api/v1/posts/{id}/
  ```

  Body:

  ```json
  {
    "text": "string"
  }
  ```

- Удаление публикации:

  ```http
  DELETE /api/v1/posts/{id}/
  ```

- Подписки (только для авторизованных пользователей):

  ```http
  GET /api/v1/follow/
  ```

## Авторизация

Доступ к защищённым эндпоинтам осуществляется по JWT-токену (поддерживается Djoser).

- Получение токена:

  ```http
  POST /api/v1/jwt/create/
  ```

  Body:

  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

- Обновление токена:

  ```http
  POST /api/v1/jwt/refresh/
  ```

- Проверка токена:

  ```http
  POST /api/v1/jwt/verify/
  ```

После получения JWT-токена добавьте его в headers (например, в Postman):

```http
Authorization: Bearer {your_token}
```

## Админ-панель

### Добавление группы через админ панель

Для добавления группы в проект используйте встроенную админ-панель Django:

1. **Авторизация в админке:**
   - Перейдите по адресу `/admin/` в браузере.
   - Введите логин и пароль суперпользователя, созданного на этапе настройки проекта.

2. **Создание группы:**
   - В разделе **Groups** нажмите кнопку “Add” (Добавить).
   - Заполните необходимые поля, такие как **Название группы** (Name).
   - Сохраните изменения, нажав кнопку “Save”.

Теперь созданная группа будет доступна через API и может быть связана с публикациями.

### Управление пользователями

В админке также доступны возможности управления пользователями:

- **Просмотр списка пользователей**: Перейдите в раздел **Users**.
- **Редактирование профиля пользователя**: Нажмите на имя пользователя в списке, внесите изменения и сохраните их.
- **Создание нового пользователя**: Нажмите кнопку “Add User”, заполните форму и сохраните.

### Управление записями и комментариями

- Записи (Posts) и комментарии (Comments) также доступны для просмотра и редактирования через админку.
- Для этого найдите соответствующий раздел, выберите нужный объект, внесите изменения и сохраните их.






