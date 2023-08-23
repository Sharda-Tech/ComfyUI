#!/bin/bash

# Step 1: Build Docker Image
echo "Building Docker image..."
docker build -t comfy .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Error: Docker image build failed."
    exit 1
fi

# Step 2: Run Docker Container
echo "Running Docker container..."
container_id=$(docker run -d --gpus all comfy)

# Check if the container is running
if [ -z "$container_id" ]; then
    echo "Error: Failed to start Docker container."
    exit 1
fi

# Step 3: Show Container Logs and Check for Errors
echo "Container logs:"
docker logs -f "$container_id" | tee container_logs.txt

# Check if specific error messages are not found in the logs
if ! grep -q "Finished" container_logs.txt || ! grep -q "Local testing complete, exiting." container_logs.txt; then
    echo "Error detected in container logs. Stopping..."
    docker stop "$container_id"
    exit 1
fi

# Step 4: Tag and Push Docker Image
echo "Tagging Docker image..."
docker tag comfy forme2/comfy

echo "Pushing Docker image..."
docker push forme2/comfy

# Check if the push was successful
if [ $? -ne 0 ]; then
    echo "Error: Docker image push failed."
    exit 1
fi

echo "Script completed successfully."

