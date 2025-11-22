#!/bin/bash


show_help() {
    cat <<EOF
Usage: $0 [options]

Options:
  -n <name>    Name of the Docker image/container (optional, default: fastapi-app-template)
  -p <port>    Port to expose (optional, default: 8080)
  -v <path>    Path to volume mount (optional, default: <run-script-path>/data/<container-name>/)
  -h           Show this help message and exit
EOF
    exit 0
}

# Get the directory of the script
RUN_SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Default values
NAME="fastapi-app-template"
PORT="8080"
VOLUME_PATH="$RUN_SCRIPT_DIR/data/$NAME/"

# Parse command-line options
while getopts "n:p:v:h" opt; do
    case "$opt" in
        n) NAME="$OPTARG" ;;
        p) PORT="$OPTARG" ;;
        v) VOLUME_PATH="$OPTARG" ;;
        h) show_help ;;
        *)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# Build Docker image
docker build -t $NAME .
if [ $? -ne 0 ]; then
    echo "-------------------------------------"
    echo "Docker build failed for image '$NAME'" >&2
    echo "Please check the Dockerfile and build context for issues." >&2
    echo "-------------------------------------" >&2
    exit 1
else
    echo "-------------------------------------"
    echo "Docker image '$NAME' built successfully!"
    echo "-------------------------------------"
fi

# Run Docker container
docker run -d --rm --name $NAME -p $PORT:8080 -v $VOLUME_PATH:/app/data $NAME
if [ $? -ne 0 ]; then
    echo "-------------------------------------"
    echo "Failed to start Docker container '$NAME'" >&2
    echo "Please ensure that the port $PORT is not already in use." >&2
    echo "Or use 'docker logs $NAME' to check the error details." >&2
    echo "-------------------------------------" >&2
    exit 1
else
    echo "-------------------------------------"
    echo "Docker container '$NAME' started successfully!"
    echo "You can access the application at 'http://127.0.0.1:$PORT/docs'"
    echo "If you want to publish this service, please use a reverse proxy like Nginx or Apache."
    echo "-------------------------------------"
fi
