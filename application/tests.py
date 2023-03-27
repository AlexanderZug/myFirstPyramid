import unittest
from webtest import TestApp

from app import main
from models import Students


class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        app = main()

        self.testapp = TestApp(app)

    def test_index(self):
        request = self.testapp.get('/new', status=200)
        self.assertTrue(b'Percentage' in request.body)

    def test_student_add(self):
        student = Students(id=51, name='test', percent=90)
        self.assertEqual(student.id, 51)
        self.assertEqual(student.name, 'test')
        self.assertEqual(student.percent, 90)

    def test_notfound(self):
        request = self.testapp.get('/notfound')
        self.assertTrue(b'Oops! Page Not Found' in request.body)


if __name__ == '__main__':
    unittest.main()
