import unittest
import bottle
import cellar.menu


appmenu = bottle.Bottle()


@appmenu.get('/foo')
def foo():
    pass


@appmenu.get('/aaa', menu='primary', name="Aaa", title="I'm aaa and I know it", desc="Long description")
def aaa():
    pass


@appmenu.get('/bbb', menu='primary', name="Bbb", title="I'm bbb and I know it", desc="Bbb description")
def bbb():
    pass


@appmenu.get('/ccc', menu='secondary', name="ccc", title="I'm ccc and I know it", desc="Def description")
def ccc():
    pass


class test_appmenu(unittest.TestCase):
    def setUp(self):
        bottle.app.push(appmenu)

    def tearDown(self):
        bottle.app.pop()

    def test_menu(self):
        pri = cellar.menu.read_menu("primary")
        self.assertEqual(len(pri), 2, "two menu items in primary menu")
        self.assertEqual(pri[0], {
            'name': 'Aaa',
            'url': '/aaa',
            'menu': 'primary',
            'title': "I'm aaa and I know it",
            'desc': 'Long description'
        })
        self.assertEqual(pri[1], {
            'name': 'Bbb',
            'url': '/bbb',
            'menu': 'primary',
            'title': "I'm bbb and I know it",
            'desc': 'Bbb description'
        })

    def test_current(self):
        pass

    def test_breadcrumb(self):
        pass
