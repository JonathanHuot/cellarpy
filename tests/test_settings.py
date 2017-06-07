import unittest
import tempfile
import cellar.settings
from os import path
import os
import json


try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.tempfile import TemporaryDirectory


class test_settings(unittest.TestCase):
    def test_load(self):
        with tempfile.NamedTemporaryFile() as temp:
            foo = {
                "x": 12,
                "y": [
                    "12",
                    "23"
                ],
                "z": "zzz"
            }
            json.dump(foo, temp)
            temp.flush()
            bar = cellar.settings.load_settings(
                path.basename(temp.name),
                dirs=[path.dirname(temp.name)]
            )
            self.assertEqual(foo, bar, "loaded settings must be equal to dict")

    def test_fromenv(self):
        with tempfile.NamedTemporaryFile() as temp:
            foo = {"x": 12}
            json.dump(foo, temp)
            temp.flush()

            try:
                os.environ["CELLAR_SETTINGS"] = temp.name
                bar = cellar.settings.load_settings()
                self.assertEqual(foo, bar, "loaded settings must be equal to dict")
            finally:
                del os.environ["CELLAR_SETTINGS"]

    def test_readperm(self):
        with TemporaryDirectory() as dir1:
            with TemporaryDirectory() as dir2:
                with open(path.join(dir1, "settings.json"), "w+") as fd:
                    json.dump(["foo"], fd)
                with open(path.join(dir2, "settings.json"), "w+") as fd:
                    json.dump(["bar"], fd)

                os.chmod(path.join(dir1, "settings.json"), 0)

                bar = cellar.settings.load_settings(
                    "settings.json",
                    dirs=[dir1, dir2]
                )
                self.assertEqual(["bar"], bar, "loaded settings must be the 1st w/ read access")

    def test_storage(self):
        pass
