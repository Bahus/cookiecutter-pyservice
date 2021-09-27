# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## poetry installation

```shell
pip install poetry
```

Authentication setup for private PYPI server:

```shell
poetry config http-basic.acme-pypi [login] <ENTER> [password]
poetry config http-basic.acme-pypi-proxy [login] <ENTER> [password]
```

Dependency installation:

```shell
poetry install
```

Create separate bridge network for ACME services:

```shell
docker network create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1 acme-net
```

Local development in 4 steps:

```shell
docker-compose -f docker-compose.provision.yaml run database -d

docker-compose -f docker-compose.provision.yaml run --rm create-db

docker-compose -f docker-compose.provision.yaml run --rm migrate

docker-compose up
```

Linting and tests:


```shell
docker-compose -f docker-compose.test.yaml run --rm check

docker-compose -f docker-compose.test.yaml run --rm tests
```
