from pyramid.view import view_config
from pyramid.response import Response


@view_config(
    route_name='home',
    request_method='GET',
    renderer='../templates/home.jinja2'
)
def home(request):
    return {'greet': 'Welcome', 'name': 'Alex'}


@view_config(
    route_name='index',
    renderer='../templates/index.html'
)
def index_view(request):
    return {}


@view_config(
    context='pyramid.httpexceptions.HTTPNotFound',
    renderer='../templates/404.html')
def notfound(request):
    return {}
