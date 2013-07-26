.. urlshots-api documentation master file, created by
   sphinx-quickstart on Sat May 25 22:24:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. highlight:: python
.. currentmodule:: urlshots


=================================
URLShots Python API Documentation
=================================

This document should serve as a guide for utilizing the installable urlshots-api
python egg with your projects.

.. rubric:: Quickstart Example with defaults:

::

    >>> from urlshots import API
    >>> urlshots_api = API(api_key='DEMO')
    >>> shot = urlshots_api.image('http://www.google.com')
    >>> with open('image.png', 'w') as open_file:
    ...     open_file.write(shot)

Contents:

.. toctree::
   :maxdepth: 2

   tutorial
   api
   changes



.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

