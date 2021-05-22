Generating Kernel Modules
--------------------------

**gen_kernel_module** is tool for generation Linux Kernel Module project.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_kernel_module/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_kernel_module/badge/?version=latest
   :target: https://gen_kernel_module.readthedocs.io/projects/gen_kernel_module/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python2%20Package%20gen_kernel_module/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python2%20Package%20gen_kernel_module/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python3%20Package%20gen_kernel_module/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python3%20Package%20gen_kernel_module/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_kernel_module/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf gen_kernel_module-x.y.z.tar.gz
    cd gen_kernel_module-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    # python2
    pip install gen-kernel-module
    # python3
    pip3 install gen-kernel-module

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_kernel_module/workflows/gen_kernel_module%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions?query=workflow%3A%22gen_kernel_module+docker+checker%22

Dependencies
-------------

**gen_kernel_module** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow
----------------

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module_flow.png

Tool structure
------------------

**gen_kernel_module** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module.png

Code structure:

.. code-block:: bash

    gen_kernel_module/
    ├── conf/
    │   ├── gen_kernel_module.cfg
    │   ├── gen_kernel_module_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── lkm_block_device/
    │       │   ├── lkm.template
    │       │   ├── Makefile.template
    │       │   └── test.template
    │       ├── lkm_charachter_device/
    │       │   ├── lkm.template
    │       │   ├── Makefile.template
    │       │   └── test.template
    │       ├── lkm_network_interfaces/
    │       │   ├── lkm.template
    │       │   ├── Makefile.template
    │       │   └── test.template
    │       └── lkm_vma/
    │           ├── lkm.template
    │           ├── Makefile.template
    │           └── test.template
    ├── __init__.py
    ├── lkm/
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── pro_name.py
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    ├── log/
    │   └── gen_kernel_module.log
    └── run/
        └── gen_kernel_module_run.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/gen_kernel_module <https://vroncevic.github.io/gen_kernel_module>`_

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
