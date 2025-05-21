# 1. Базовый образ с поддержкой Playwright
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

# 2. Установка зависимостей Python (если нужен poetry — добавь по аналогии)
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 3. Копируем исходники backend (всё кроме .venv)
COPY . .

# 4. Playwright browsers уже установлены в базовом образе, но на всякий случай:
RUN playwright install --with-deps

# 5. Открываем порт (для Render и Railway не обязательно, но не мешает)
EXPOSE 8000

# 6. Стартуем сервер
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
