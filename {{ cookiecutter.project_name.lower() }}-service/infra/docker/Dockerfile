FROM registry.acme.com/python AS base

ENV ACME_ENV=production

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
COPY ./infra/uwsgi.yaml /code/infra/uwsgi.yaml
COPY --chown=non_root_user:non_root_user ./infra/docker/entrypoint.sh /docker-entrypoint.sh

RUN chmod +x "/docker-entrypoint.sh"
RUN gosu non_root_user bash /docker-entrypoint.sh install

ENTRYPOINT ["/docker-entrypoint.sh"]

FROM base AS production
COPY . /code
RUN python -m compileall .
USER non_root_user

FROM base AS development
ENV ACME_ENV=development
RUN gosu non_root_user bash /docker-entrypoint.sh install-dev-dependencies
COPY . /code
RUN python -m compileall .
# For better developer experience we use root user for development target,
# to avoid permission denied error when creating new files.
USER root
