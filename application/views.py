from pyramid.view import view_config, view_defaults


@view_defaults(route_name='user', renderer='templates/home.html')
class User:
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        name = self.request.matchdict['name']
        age = self.request.matchdict['age']
        return {'greet': 'Welcome', 'name': f'{name}', 'age': f'{age}'}


class Student:
    def __init__(self, request):
        self.request = request

    @view_config(
        route_name='create',
        renderer='templates/myform.html',
    )
    def post(self):
        return {}

    @view_config(
        route_name='list',
        renderer='templates/marklist.html',
    )
    def get(self):
        students = [
            {"id": 1, "name": "Ravi", "percent": 75},
            {"id": 2, "name": "Mona", "percent": 80},
            {"id": 3, "name": "Mathews", "percent": 45},
        ]
        student = {
            'id': self.request.params['id'],
            'name': self.request.params['name'],
            'percent': int(self.request.params['percent'])
        }
        students.append(student)
        return {'students': students}


@view_config(
    context='pyramid.httpexceptions.HTTPNotFound',
    renderer='templates/404.html')
def notfound(request):
    return {}
