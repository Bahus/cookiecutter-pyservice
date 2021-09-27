#!/usr/bin/env bash
set -o errexit
set -o nounset

export ARGS=$@

case "${ARGS}" in
"")
    echo "Starting application in ${ACME_ENV} environment"
    exec poetry run uwsgi --yaml infra/uwsgi.yaml --yaml infra/uwsgi.yaml:${ACME_ENV}
    ;;
"install")
    echo "Installing dependencies"
    poetry run pip install pip==${PIP_VERSION}
    poetry install --no-dev --no-interaction --no-ansi
    ;;
"install-dev-dependencies")
    echo "Installing dev dependencies"
    poetry install --no-interaction --no-ansi
    ;;
*)
    exec ${ARGS}
    ;;
esac
