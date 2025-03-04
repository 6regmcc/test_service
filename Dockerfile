# The builder image, used to build the virtual environment
FROM python:3.13.0-alpine3.20 as builder

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.13.0-alpine3.20 as runtime


RUN apk add --update curl && \
    rm -rf /var/cache/apk/* \ && \
    apk add bind-tools
 #   apt -y install libglib2.0-0 libsm6 libxext6 libxrender-dev && \
 #   apt install -yq dnsutils

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
ENV DATABASE_URL="sqlite:///database.db"
ENV ENVIRONMENT="dev"
ENV ROOT_PATH="/"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY src ./src

EXPOSE 8080
CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0",  "--port", "8080"]
