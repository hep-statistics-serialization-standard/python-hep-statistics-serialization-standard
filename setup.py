#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='hep-statistics-standard',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/hep_statistics_standard/_version.py',
        'fallback_version': '0.0.1',
    },
    license='BSD-3-Clause',
    description='Standardization of serialization formats for statistics in HEP',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='HEP statistics standard',
    author_email='hep-statistics-standard@cern.ch',
    url='https://https://github.com/hep-statistics-standard/python-hep-statistics-standard/hep-statistics-standard/python-hep-statistics-standard',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        # 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        # 'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://python-hep-statistics-standard.readthedocs.io/',
        'Changelog': 'https://python-hep-statistics-standard.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://https://github.com/hep-statistics-standard/python-hep-statistics-standard/hep-statistics-standard/python-hep-statistics-standard/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
    extras_require={
    },
    setup_requires=[
        'setuptools_scm>=3.3.1',
    ],
    entry_points={
        'console_scripts': [
            'hep-statistics-standard = hep_statistics_standard.cli:main',
        ]
    },
)
