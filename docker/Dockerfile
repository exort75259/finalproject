# Используем базовый образ Python
FROM python:3.9-slim

# Переходим в рабочую директорию контейнера
WORKDIR /app

# Копируем файлы из контекста сборки в контейнер
COPY ./src/server.py /app/

# Указываем команду запуска
CMD ["python", "server.py"]

