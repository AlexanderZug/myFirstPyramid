from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='templates/home.jinja2'
)
def home(request):
    return {"greet": 'Welcome', "name": 'Alexander'}


def main():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
