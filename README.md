
# hello-python-docker

Sample of a Python webapp dockerized as decribed in [https://docs.docker.com/get-started/part2/](https://docs.docker.com/get-started/part2/).

The *dockefile* creates an images which is based on python:2.7-slim and runs a simple web app the uses the Flask framework to run. Port 80 is exposed to make the web app available to the world outside the container.

The application code is located in the file *app.py*. The dependencies are listed in file *requirements.txt*.

The events like startup and visit count are logged to the file *app.log* inside the container for testing purposes. 

## Build the image

To build the image use
`docker build --tag=hello-python .`

Use `docker image ls` to see the image in your local repository.

## Build and run the container
To run the app in a container in background and make it available at port 4000 at your local machine (e.g. http://localhost:4000/) use
`docker run -d -p 4000:80 hello-python`.

Use `docker ps` or `docker ls` or `docker ls -a` to explore the containers in your system.
Use `docker start <container id>` to start a container.
Use `docker stop <container id>` to stop a container.

The image is also published at [https://cloud.docker.com/repository/docker/ashburnere/hello-python-docker](https://cloud.docker.com/repository/docker/ashburnere/hello-python-docker).

Use `docker run -d -p 4000:80 ashburnere/hello-python-docker:v1` if you want to run the app directly from the image from the docker repository.

## Useful Docker commands
Here is a list of useful Docker commands:

### Docker basics

- `docker build -t <container id|name> .`  # Create image using the current directory's Dockerfile
- `docker run -p 4000:80 <container id|name>`  # Run the container with the given name or ID with mapping port 4000 to 80
- `docker run -d -p 4000:80 <container id|name>`         # Same thing, but in detached mode
- `docker container ls`                                # List all running containers
- `docker container ls -a`             # List all containers, even those not running
- `docker container stop <hash>`          # Gracefully stop the specified container
- `docker container kill <hash>`         # Force shutdown of the specified container
- `docker container rm <hash>`        # Remove specified container from this machine
- `docker container rm $(docker container ls -a -q)`         # Remove all containers
- `docker image ls -a`                             # List all images on this machine
- `docker image rm <image id>`            # Remove specified image from this machine
- `docker image rm $(docker image ls -a -q)`   # Remove all images from this machine
- `docker login`             # Log in this CLI session using your Docker credentials
- `docker tag <image> username/repository:tag`  # Tag <image> for upload to registry
- `docker push username/repository:tag`            # Upload tagged image to registry
- `docker run username/repository:tag`                   # Run image from a registry
- `docker start <container id|name>` 	# Start container
- `docker stop <container id|name>` 	# Stop container
- `docker exec -it <container id|name>` /bin/sh	# Open shell in running container
- `docker rmi <image>`	# Remove image with name
- `docker container logs -f <container id|name>` # View the logs of the given container

### Docker services
- `docker stack ls` # List stacks or apps
- `docker swarm init` # Initialze docker swarm
- `docker stack deploy -c <composefile> <appname>`  # Run the specified Compose file
- `docker service ls` # List running services associated with an app
- `docker service ps <service>` # List tasks associated with an app
- `docker inspect <task or container>`  # Inspect task or container
- `docker container ls -q`  # List container IDs
- `docker stack rm <appname>` # Tear down an application
- `docker swarm leave --force`  # Take down a single node swarm from the manager



