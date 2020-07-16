FROM    python:3.7-alpine

ARG     APP_DIR=/app/
WORKDIR ${APP_DIR}
ENV     PATH=.:$PATH
COPY    ./src requirements.txt ${APP_DIR}
RUN     pip install -r requirements.txt

ENTRYPOINT ["python", "."]
