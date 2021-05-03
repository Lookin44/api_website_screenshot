# Описание сервиса
Веб-приложение для сбора скринов сайта по уровням вложенности

# Алгоритм установки на локальный компьютер:
1. Скопируй репозиторий на свой компьютер: ```https://github.com/Lookin44/api_website_screenshot.git```;
2. Установите виртуальное окружение в скачанной директории: ```python3 -m venv venv```;
3. Активируйте виртуальное окружение в скачанной директории: ```source venv/bin/activate```;
4. После активации установите список зависимостей: ```pip install -r requirements.txt```;
5. Готово, можно приступить)

# Алгоритм запуска микросервиса на локальном компьютере:
#ВАЖНО: для работы микросервиса необходимо что бы на компьютере был установлен Google Chrome (Версия 90.0.4430.93 (Официальная сборка), (64 бит))
1. Для начала необходимо создать миграций на локальном компьютере: ```python3 manage.py makemigrations```;
2. Выполните миграцию: ```python3 manage.py migrate```;
3. Запустите сервер на локальном компьютере: ```python3 manage.py migrate```;

# Работа с микросервисом:
1. Для создания скриншотов с сайта отправьте POST-запрос на http://localhost:8000/screenshot/ c параметрами: 
 {'link': '<сайт в формате https://www.<запращиваемый сайт>/>', 'level': '<уровень вложенности сайта числом>'} 
 пример: {'link': 'https://www.google.ru/', 'level': '2'}
 2. Скриншоты сайта найдете в директории проекта в папке photo.
