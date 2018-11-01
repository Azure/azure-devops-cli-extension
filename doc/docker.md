# VSTS CLI Docker Image

## Create the image

1. Use `docker build` to create the image:
   ```bash
   export CLI_VERSION=0.1.0b0.dev4347880
   
   docker build --no-cache --build-arg BUILD_DATE="`date -u +"%Y-%m-%dT%H:%M:%SZ"`" --build-arg CLI_VERSION=${CLI_VERSION} -f DockerFile . --tag microsoft/azdos-cli:${CLI_VERSION}
   ```

## Verify the image

1. Use `docker run` to create and start an instance of the image:
   ```
   docker run -it microsoft/azdos-cli:${CLI_VERSION}
   ```

2. Verify the CLI works as expected:
   ```
   azdos -v
   ```

## Publish the image

1. Use `docker push` to publish the image to Docker Hub:
   ```
   docker push microsoft/azdos-cli:${CLI_VERSION}
   ```
