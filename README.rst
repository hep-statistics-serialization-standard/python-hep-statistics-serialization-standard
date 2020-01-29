========
Overview
========

Standardization of serialization formats for statistics in HEP

* Free software: BSD 3-Clause License

Installation
============

::

    pip install hep-statistics-standard

You can also install the in-development version with::

    pip install git+ssh://git@https://github.com/hep-statistics-standard/python-hep-statistics-standard/hep-statistics-standard/python-hep-statistics-standard.git@master

Documentation
=============


https://python-hep-statistics-standard.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
