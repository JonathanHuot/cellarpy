import unittest
import cellar.web
import tempfile
from os import path


try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.tempfile import TemporaryDirectory


sample_less = b"""@nice-blue: #5B83AD;
@light-blue: @nice-blue + #111;

#header {
  color: @light-blue;
}
"""

sample_css = """#header {
  color: #6c94be;
}
"""

sample_static_tpl = b"""
hello {{name}}
"""


class test_web(unittest.TestCase):
    def test_less(self):
        with TemporaryDirectory() as cachepath:
            with tempfile.NamedTemporaryFile() as temp:
                temp.write(sample_less)
                temp.flush()
                response = cellar.web.generate_less_from_css(
                    path.basename(temp.name),
                    path.dirname(temp.name),
                    cachepath
                )
                css = response.body.read()
                if not isinstance(css, str):
                    css = str(css, 'utf-8')
                with open(path.join(cachepath, path.basename(temp.name))) as fd:
                    cached = fd.read()
                self.assertEqual(css, sample_css, "css has not been correctly generated")
                self.assertEqual(cached, sample_css, "cached has not been correctly generated")

    def test_tpl(self):
        pass
