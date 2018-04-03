# Generated by Medikit 0.5.19 on 2018-04-03.
# All changes will be overriden.
# Edit Projectfile and run “make update” (or “medikit update”) to regenerate.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'django_zero/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    description='Zero-configuration django projects.',
    license='Apache License, Version 2.0',
    name='django_zero',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=[
        'brotli (~= 1.0)', 'django (~= 2.0)', 'django-allauth (~= 0.34)', 'django-includes (~= 0.2)',
        'jinja2 (~= 2.10)', 'mondrian (~= 0.6)', 'whitenoise (~= 3.3)'
    ],
    extras_require={
        'celery': ['celery (~= 4.1)', 'django_celery_beat (~= 1.1.1)', 'django_celery_results (~= 1.0.1)'],
        'channels': ['channels (~= 2.0, >= 2.0.2)'],
        'dev': [
            'cookiecutter (~= 1.6)', 'coverage (~= 4.4)', 'django-extensions (~= 1.9)', 'django_debug_toolbar (~= 1.9)',
            'honcho (~= 1.0)', 'medikit (~= 0.5)', 'pytest (~= 3.4)', 'pytest-cov (~= 2.5)', 'sphinx (~= 1.7)',
            'werkzeug (~= 0.14)', 'yapf'
        ],
        'prod': ['gunicorn (~= 19.7.1)']
    },
    entry_points={'console_scripts': ['django-zero = django_zero.commands:main']},
    url='https://github.com/hartym/django-zero',
    download_url='https://github.com/hartym/django-zero/archive/{version}.tar.gz'.format(version=version),
)
