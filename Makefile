#!cmake
APP_VERSION = 0.1.0

all: build run

build:
	docker build -t "dmi7ry/rick-and-morty-random-episode:${APP_VERSION}" .

run:
	docker run --rm "dmi7ry/rick-and-morty-random-episode:${APP_VERSION}"
