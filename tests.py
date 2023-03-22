import unittest
from webtest import TestApp

from app import main


class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        app = main()
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Welcome' in res.body)


if __name__ == '__main__':
    unittest.main()
