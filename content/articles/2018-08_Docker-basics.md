Title: Docker basics
Summary: For those who are using Docker only during holidays like me and keep forgetting the basic commands over and over again.
Category: Articles
Date: 2018-08-23
Updated: 2020-03-23
Author: Tomas Peterka

Docker is a technology to run software already bundled with all their dependencies together by one command.
The software is distributed in images and once you run it a container is created.

## Docker Image

Contains file-system layers with libraries and applications. Images are hosted on hub.docker.com or any other instance of Docker Hub.
You can get one (e.g. nginx image) by calling `docker get nginx`. Maybe you will need to `docker login` first.

Once downloaded, you can do with images ...

* list available images `docker images`
* remove an image `docker rmi nginx` once its containers stopped and removed
* run it as a container `docker run nginx` BEWARE: this creates a new container every time
* build a new image upon this one by adding file-system layers with your own apps and libs

### Running an image - a.k.a. creating a container

is the part where you use the most parameters (external mountpoint, port publishing etc.). Once container
is defined start/stop is simple operation without parameters! Available parameters when running an image as a container

* `--name <name>` important if you don't want a random name like "stupid_trump"
* `-p 8080:8080` port to publish (make available from host) - syntax -p <host-port>:<container-port>
* `-e VAR_NAME="var value"` set an env var inside the container
* `-v <local-folder>:<container-folder>` binds a container-folder to local-folder so you can see and share the final data from the host.
   This is actually recommended to store user data outside the appplication container. You can either use this `-v` option or `--volumes-from`
   to use a dedicated data container. Why? Because when you would update the version of your application container you would loose all data
   with it!
* `-d` detach container - useful for servers
* `-rm` remove container when it exists - useful for stateless applications

Example of one of my `run` command

```
docker run -d \
   --name multishop.postgres \
   -e POSTGRES_PASSWORD=my-password \
   -e PGDATA=/var/lib/postgresql/data/pgdata \
   -p 5432:5432 \
   -v `pwd`/data:/var/lib/postgresql/data/pgdata \  # the second part is obviously inside the container
   "multishop/postgres:9.6"  # image to be run
```

### Re-publishing an image

Images are "named" by `tag`s. Tag contains even source of the image. Therefore if I download an image from local docker hub A 
`docker pull hub-a.mycompany.com/orgunit/my-image:latest` the image appears in
```
docker images
REPOSITORY                               TAG                 IMAGE ID            CREATED             SIZE
hub-a.mycompany.com/orgunit/my-image     8.0.7               23ef52fadd22        4 weeks ago         1.94GB
busybox                                  latest              6d5fcfe5ff17        3 months ago        1.22MB
```
Then you add a new tag to the image `docker tag hub-a.mycompany.com/orgunit/my-image:8.0.7 hub-b.mycompany.com/orgunit/my-image:8.0.7`
and you will be rewarded by a new tag on the same image (see equal IMAGE_IDs)
```
docker images
REPOSITORY                               TAG                 IMAGE ID            CREATED             SIZE
hub-a.mycompany.com/orgunit/my-image     8.0.7               23ef52fadd22        4 weeks ago         1.94GB
hub-b.mycompany.com/orgunit/my-image     8.0.7               23ef52fadd22        4 weeks ago         1.94GB
busybox                                  latest              6d5fcfe5ff17        3 months ago        1.22MB
```
Now you can push the image to your other repository `docker push hub-b.mycompany.com/orgunit/my-image:8.0.7` 

## Docker Container

Is a running process that comes from an image. It creates one extra FS layer containing your modifications and data.
Container can be stopped and restarted.

* create a running container from an image `docker run [bazilion-of-options] nginx`
* stop a container `docker stop nginx1`
* (re)start a container `docker start nginx1`
* list running containers `docker ps`
* list running and stopped containers `docker ps -a`

Examples at https://docs.docker.com/engine/reference/commandline/run/