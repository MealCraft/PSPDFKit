import multiprocessing
from psycogreen.gevent import patch_psycopg


def post_fork(server, worker):
    patch_psycopg()


bind = "0.0.0.0:80"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 300
loglevel = "DEBUG"
worker_class = "gevent"
