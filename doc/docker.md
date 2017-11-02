VSTS CLI Docker
===============


Create the image 
----------------

1. Use `docker build` to create the image:
   ```
   $ export CLI_VERSION=0.1.0b0.dev4335832
   
   $ docker build --no-cache --build-arg BUILD_DATE="`date -u +"%Y-%m-%dT%H:%M:%SZ"`" --build-arg CLI_VERSION=${CLI_VERSION} -f DockerFile . --tag vsts:${CLI_VERSION}
   ```

2. Use `docker run` to create and run an instance of the new image:
   ```
   $ docker run -it vsts:${CLI_VERSION}

   # vsts -v
   # vsts --help
   ```

