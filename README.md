# FastAPI App Template

## Run app

-   Use `./run.sh` to build Docker image and run a container.
-   Use `docker stop <container-name>` to stop service.
-   Use `docker image rm <image-name>` to remove image.

-   Options:

    -   `-h`: Help message
    -   `-n <name>`: Name of the Docker image/container (optional, default: fastapi-app-template)
    -   `-p <port>`: Port to expose this app (optional, default: 8080)
    -   `-v <path>`: Path to volume mount (optional, default: <run-script-path>/data/<container-name>/)

-   Example:

    -   `./run.sh -p 8080`
