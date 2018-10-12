# docker-pudb
Debug Python code within a Docker container remotely from your terminal using pudb.

## Prerequisites:
- [Python](https://docs.python.org/3/index.html)
- [Docker](https://docs.docker.com/)
- [pudb](https://documen.tician.de/pudb/)
- [telnet client](https://en.wikipedia.org/wiki/Telnet)

## How to do it?
### Python
Just add the following line wherever you want you entry point to be:
```python
from pudb.remote import set_trace; set_trace(term_size=(160, 40), host='0.0.0.0', port=6900)
```
If you wanted to debug using `pudb` locally you'd write instead:
```python
import pudb; pu.db
```
Which is similar to how one would do it for the built-in pdb:
```python
import pdb; pdb.set_trace()
```

### Docker
#### Dockerfile
- `pudb` needs to be installed on the Docker image. One way to do it is adding this line to the Dockerfile:
```
RUN pip install pudb
```
- The port `pudb` is listening to must be open. In our example it is 6900. One way to do it is adding to your Dockerfile:
```
EXPOSE 6900
```

#### docker-compose
If you use docker-compose yml files the syntax is different. You should add:
```
ports:
    - "6900:6900"
```

### Telnet
**Mac users:** If you don't have any `telnet` client, you can install one via [Homebrew](https://brew.sh/). Type `brew install telnet` on your terminal.

When all above is done, run the container. When the entrypoint is reached, the code execution will stop. Then you need to connect to it via a telnet client, e.g. `telnet 127.0.0.1 6900`. Now you will see the `pudb` screen and debugging can start :D

## Try it out!
Clone this repository and from its root folder run:
```sh
# Build the image
docker build -t pudb-example .
# Run the container (in the background) with port 6900 open
docker run -p 6900:6900  --detach pudb-example
# Connect to pudb via telnet
telnet 127.0.0.1 6900
# Enjoy debugging!
```

## Acknowledgements
- This repository was inspired by [this blog post](http://kartowicz.com/dryobates/2016-09/debugging_gunicorn_on_docker_with_pudb/). Since there were some instructions but not any code readily available to try it out, I built this.
