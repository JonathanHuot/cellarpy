import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="cellarpy",
    version="1.1",
    author="Jonathan Huot",
    author_email="jonathan.huot@gmail.com",
    description=("cellarpy empower python web-applications based on bottlepy"),
    license="MIT",
    keywords="bottle web wsgi",
    url="https://github.com/JonathanHuot/cellarpy",
    packages=['cellar'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Framework :: Bottle',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
