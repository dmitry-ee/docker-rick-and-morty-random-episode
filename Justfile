app_version := `git describe --abbrev=0 --tags`
app_name := "rick-and-morty-random-episode"
docker_user_id := "dmi7ry"
docker_image_name := docker_user_id + "/" + app_name + ":" + app_version
docker_image_latest := docker_user_id + "/" + app_name + ":latest"

build:
	docker build -t {{docker_image_name}} .

run:
	docker run --rm {{docker_image_name}}

run-latest:
	docker run --rm {{docker_image_latest}}

push:
	docker push {{docker_image_name}}

build-latest:
	docker build -t {{docker_image_latest}} .

push-latest:
	docker push {{docker_image_latest}}

dive:
	dive {{docker_image_name}}