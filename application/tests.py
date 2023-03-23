import unittest
from webtest import TestApp

from app import main
from views import home, index_view


class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        app = main()
        self.testapp = TestApp(app)

    def test_home(self):
        result = home({})
        self.assertEqual(result['greet'], 'Welcome')
        self.assertEqual(result['name'], 'Alex')

    def test_index(self):
        result = index_view({})
        self.assertEqual(result, {})

    def test_notfound(self):
        res = self.testapp.get('/notfound', status=404)
        self.assertEqual(res.body, b'Not Found')

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Welcome' in res.body)


if __name__ == '__main__':
    unittest.main()
