from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='templates/home.jinja2'
)
def home(request):
    return {'greet': 'Welcome', 'name': 'Alex'}


@view_config(
    route_name='index',
    renderer='templates/index.html'
)
def index_view(request):
    return {}
