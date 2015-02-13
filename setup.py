import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cellar",
    version = "0.1",
    author = "Jonathan Huot",
    author_email = "jonathan.huot@gmail.com",
    description = ("cellarpy empower python web-applications based on bottlepy"),
    license = "MIT",
    keywords = "bottle web wsgi",
    url = "https://github.com/JonathanHuot/cellarpy",
    packages=['cellar'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
