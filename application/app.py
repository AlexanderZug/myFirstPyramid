from wsgiref.simple_server import make_server
from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator

from models import getsession

my_session_factory = SignedCookieSessionFactory('abcQWE123!@#')
session = getsession()


def main():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_static_view(name='static', path='static')
    config.set_session_factory(my_session_factory)
    config.add_route(name='index', pattern='/new')
    config.add_route(name='create', pattern='/create')
    config.add_route(name='list', pattern='/list')
    config.add_route(name='show', pattern='/show/{id}')
    config.add_route(name='update', pattern='/update')
    config.add_route(name='delete', pattern='/delete/{id}')
    config.scan('views')
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
