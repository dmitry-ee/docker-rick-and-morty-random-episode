#!cmake
APP_VERSION = $(shell git describe --abbrev=0 --tags)
IMAGE_NAME = "dmi7ry/rick-and-morty-random-episode:$(APP_VERSION)"
IMAGE_NAME_LATEST = "dmi7ry/rick-and-morty-random-episode:latest"

all: build-latest push-latest

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm $(IMAGE_NAME)

run-latest:
	docker run --rm $(IMAGE_NAME_LATEST)

push:
	docker push $(IMAGE_NAME)

build-latest:
	docker build -t $(IMAGE_NAME_LATEST) .

push-latest:
	docker push $(IMAGE_NAME_LATEST)
