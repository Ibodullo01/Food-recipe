FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install celery redis

COPY . .

ENV DJANGO_SETTINGS_MODULE=food_recipe.settings

CMD ["celery", "-A", "food_recipe.celery", "worker", "-l", "INFO"]
