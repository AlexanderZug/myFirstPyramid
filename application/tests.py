import unittest
from webtest import TestApp

from app import main


class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        app = main()
        self.testapp = TestApp(app)

    def test_user(self):
        request = self.testapp.get('/alex/20/', status=200)
        self.assertTrue(b'20' in request.body)
        self.assertTrue(b'alex' in request.body)

    def test_student(self):
        request = self.testapp.post('/students/', params={
            'id': 4,
            'name': 'Alex',
            'percent': 90
        }, status=200)
        self.assertTrue(b'Alex' in request.body)
        self.assertTrue(b'90' in request.body)

    def test_notfound(self):
        request = self.testapp.get('/notfound/')
        self.assertTrue(b'Try again a little later' in request.body)


if __name__ == '__main__':
    unittest.main()
