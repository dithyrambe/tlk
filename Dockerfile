FROM python:3.12-slim AS builder

RUN apt -y update && apt -y install curl
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.2
ENV PATH /root/.local/bin:$PATH

WORKDIR /app
COPY . .

RUN poetry build --format wheel --output ./dist
RUN poetry run pip install ./dist/*

FROM python:3.12-slim AS prod

RUN apt-get update && \
    apt-get install -y build-essential git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
ENV PATH /app/.venv/bin:$PATH
WORKDIR /app

ENTRYPOINT [ "tlk" ]
