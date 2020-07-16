FROM    python:3.7-alpine

ARG     APP_DIR=/app/
WORKDIR ${APP_DIR}
ENV     PATH=.:$PATH
COPY    ./src ${APP_DIR}

ENTRYPOINT ["python", "."]
