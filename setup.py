
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
    maintainer='Mathew Topper',
    maintainer_email='mathew.topper@dataonlygreater.com',
    description=('Utilities to use pandas (the data analysis / manipulation '
                 'library for Python) with Qt.'),
    packages=['dtocean_qt'],
    install_requires=['easygui',
                      'pandas',
                      # 'PyQt4',
                      'python-magic',
                      # 'sip'
                      ],
    tests_require=['pytest', 'pytest-qt'],
    include_package_data=True,
    cmdclass={'test': PyTest},
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