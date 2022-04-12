
import sys

import yaml
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def read_yaml(rel_path):
    with open(rel_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


def get_appveyor_version():
    
    data = read_yaml("appveyor.yml")
    
    if "version" not in data:
        raise RuntimeError("Unable to find version string.")
    
    appveyor_version = data["version"]
    last_dot_idx = appveyor_version.rindex(".")
    
    return appveyor_version[:last_dot_idx]


setup(
    name='dtocean-qt',
    version=get_appveyor_version(),
    license='MIT License',
    maintainer='Mathew Topper',
    maintainer_email='mathew.topper@dataonlygreater.com',
    description=('Utilities to use pandas (the data analysis / manipulation '
                 'library for Python) with Qt.'),
    packages=['dtocean_qt'],
    install_requires=['easygui',
                      'pandas>=0.23',
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
