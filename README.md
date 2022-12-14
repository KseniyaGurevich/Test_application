# CLI приложение
### Описание:

Реализовано CLI приложение, которое:

1) Получает на вход N строк.
2) Итерируется по этим строкам и определяет, является ли эта строка ссылкой или нет.
3) Если эта строка не ссылка, выводится уведомление: Строка "X" не является ссылкой.
4) Если является ссылкой, то
	1) Приложение определяет какие методы доступны по этой ссылки
		1) Проверяются все http методы.
		2) Доступным считается метод, обработка которого завершилась не 405 ошибкой.
	3) Передаваемые данные и ошибки от сервера не важны.
	4) Выполнив запрос приложение сохраняет код ответа.
6) Результат работы приложения -  словарь, состоящий из ссылок и информации о доступных методах.

### Используемые технологии: 
- python
- poetry
- pytest
- coverage

### Запуск проекта

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:KseniyaGurevich/Test_application.git
```

- Cоздать и активировать виртуальное окружение.

- Установить зависимости:
```
poetry install
```

### Отчёт о покрытии тестами в можно посмотреть в директории:

Test_application / htmlcov / index.html