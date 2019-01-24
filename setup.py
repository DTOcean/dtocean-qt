
from __future__ import print_function

import io
import os
import re
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

version_file = open(os.path.join(here, 'dtocean_qt', '__init__.py'), 'rU')
__version__ = re.sub(
    r".*\b__version__\s+=\s+'([^']+)'.*",
    r'\1',
    [line.strip() for line in version_file if '__version__' in line].pop(0)
)
version_file.close()


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='dtocean-qt',
    version=__version__,
    license='MIT License',
    namespace_packages = ['dtocean_qt'],
    author='Matthias Ludwig, Marcel Radischat, Mathew Topper',
    install_requires=['easygui',
                      'pandas',
                      # 'PyQt4',
                      'python-magic',
                      'setuptools',
                      # 'sip'
                      ],
    tests_require=['pytest', 'pytest-qt'],
    cmdclass={'test': PyTest},
    author_email='m.Ludwig@datalyze-solutions.com, dataonlygreater@gmail.com',
    description=('Utilities to use pandas (the data analysis / manipulation '
                 'library for Python) with Qt.'),
    include_package_data=True,
    packages=['dtocean_qt'],
    platforms='any',
    test_suite='tests',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: German',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces'
        ]
)