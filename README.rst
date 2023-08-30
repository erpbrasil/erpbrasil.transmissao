========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/erpbrasiltransmissao/badge/?style=flat
    :target: https://readthedocs.org/projects/erpbrasiltransmissao
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/erpbrasil/erpbrasil.transmissao.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/erpbrasil/erpbrasil.transmissao

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/erpbrasil/erpbrasil.transmissao?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/erpbrasil/erpbrasil.transmissao

.. |requires| image:: https://requires.io/github/erpbrasil/erpbrasil.transmissao/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/erpbrasil/erpbrasil.transmissao/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/erpbrasil/erpbrasil.transmissao/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/erpbrasil/erpbrasil.transmissao

.. |version| image:: https://img.shields.io/pypi/v/erpbrasil.transmissao.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/erpbrasil.transmissao

.. |commits-since| image:: https://img.shields.io/github/commits-since/erpbrasil/erpbrasil.transmissao/v1.1.0..svg
    :alt: Commits since latest release
    :target: https://github.com/erpbrasil/erpbrasil.transmissao/compare/v1.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/erpbrasil.transmissao.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/erpbrasil.transmissao

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/erpbrasil.transmissao.svg
    :alt: Supported versions
    :target: https://pypi.org/project/erpbrasil.transmissao

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/erpbrasil.transmissao.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/erpbrasil.transmissao


.. end-badges

Infraestrutura de transmissao de documentos eletronicos em Python

* Transmissão de SOAP-XML e HTTP com certificado digital de maneira segura e prática.

Documentação
============

https://erpbrasil.github.io/

Créditos
========

Esta é uma biblioteca criada atravês do esforço de das empresas:

* Akretion https://akretion.com/pt-BR/
* KMEE https://www.kmee.com.br

Parte do código foi extraido da localização brasileira do Odoo: https://github.com/oca/l10n-brazil/ favor consultar a lista de contribuidores:

https://github.com/erpbrasil/erpbrasil.base/graphs/contributors

Licença
~~~~~~~

* Free software: MIT license

Installation
============

::

    pip install erpbrasil.transmissao

Documentation
=============


https://erpbrasiltransmissao.readthedocs.io/


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
