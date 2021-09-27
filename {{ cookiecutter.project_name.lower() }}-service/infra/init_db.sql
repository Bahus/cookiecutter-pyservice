-- Creates initial database and required roles

CREATE ROLE {{cookiecutter.project_name.lower()}}_user WITH LOGIN PASSWORD '{{cookiecutter.project_name.lower()}}_password';

CREATE DATABASE {{cookiecutter.project_name.lower()}} WITH
    TEMPLATE = template0
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8';

ALTER DATABASE {{cookiecutter.project_name.lower()}} OWNER TO {{cookiecutter.project_name.lower()}}_user;
