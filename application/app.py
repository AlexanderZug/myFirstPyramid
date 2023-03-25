from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def main():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_static_view('static', 'application:static')
    config.add_route('user', '/{name}/{age}/')
    config.add_route('create', '/')
    config.add_route('list', '/students')
    config.scan('views')
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
