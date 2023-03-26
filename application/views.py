from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.events import NewRequest
from pyramid.events import subscriber

from app import session
from models import Students


class Student:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='index', renderer='templates/myform.html')
    def index(self):
        return {}

    @view_config(
        route_name='create',
        request_method='POST',
    )
    def create(self):
        id = int(self.request.POST['id'])
        name = self.request.POST['name']
        if self._unique_check(id, name):
            self.request.session.flash('Record already exists')

        percent = int(self.request.POST['percent'])
        student = Students(id=id, name=name, percent=percent)
        session.add(student)
        session.commit()
        return HTTPFound(location='/list')

    @view_config(
        route_name='list',
        renderer='templates/marklist.html',
    )
    def list(self):
        students = session.query(Students).all()
        return {'students': students}

    @view_config(route_name='update', request_method='POST')
    def update(self):
        id = int(self.request.POST['id'])
        student = session.query(Students).filter(Students.id == id).first()
        student.percent = int(self.request.POST['percent'])
        session.commit()
        return HTTPFound(location='/list')

    @view_config(route_name='show', renderer='templates/showform.html')
    def show(self):
        id = self.request.matchdict['id']
        row = session.query(Students).filter(Students.id == id).first()
        student = {'id': row.id, 'name': row.name, 'percent': row.percent}
        return {'student': student}

    @view_config(route_name='delete', renderer='templates/delete.html')
    def delete(self):
        id = self.request.matchdict['id']
        student = session.query(Students).filter(Students.id == id).first()
        session.delete(student)
        session.commit()
        return {'message': 'Redcord has been deleted'}

    def _unique_check(self, id, name):
        if session.query(Students).filter(
            Students.id == id
        ).first() or session.query(Students).filter(
            Students.name == name
        ).first() is not None:
            return True
        return False


@subscriber(NewRequest)
def add_base_url(event):
    event.request.base_url = event.request.application_url
    print(event.request.application_url)


@view_config(
    context='pyramid.httpexceptions.HTTPNotFound',
    renderer='templates/404.html')
def notfound(request):
    return {}
