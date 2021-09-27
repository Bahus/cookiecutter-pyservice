from gevent import monkey
from psycogreen.gevent import patch_psycopg


monkey.patch_all()
patch_psycopg()

from gevent.pywsgi import WSGIServer

from {{cookiecutter.project_slug}} import create_app


app = create_app()


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', {{cookiecutter.project_port}}), app)
    http_server.serve_forever(stop_timeout=45)
