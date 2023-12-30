Generating Kernel Modules
--------------------------

**gen_kernel_module** is tool for generation Linux Kernel Module project.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_kernel_module python checker| |gen_kernel_module python package| |github issues| |documentation status| |github contributors|

.. |gen_kernel_module python checker| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml

.. |gen_kernel_module python package| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_kernel_module/badge/?version=latest
   :target: https://gen-kernel-module.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_kernel_module python3 build|

.. |gen_kernel_module python3 build| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_kernel_module/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_kernel_module-x.y.z.tar.gz
    cd gen_kernel_module-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_kernel_module-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_kernel_module_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_kernel_module_run.py /usr/local/bin/gen_kernel_module_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen-kernel-module

Dependencies
-------------

**gen_kernel_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_kernel_module** is based on OOP

Code structure

.. code-block:: bash

    gen_kernel_module/
        ├── conf/
        │   ├── gen_kernel_module.cfg
        │   ├── gen_kernel_module.logo
        │   ├── gen_kernel_module_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── block/
        │       │   ├── lkm.template
        │       │   ├── Makefile.template
        │       │   └── test.template
        │       ├── char/
        │       │   ├── lkm.template
        │       │   ├── Makefile.template
        │       │   └── test.template
        │       ├── net/
        │       │   ├── lkm.template
        │       │   ├── Makefile.template
        │       │   └── test.template
        │       └── vma/
        │           ├── lkm.template
        │           ├── Makefile.template
        │           └── test.template
        ├── __init__.py
        ├── lkm/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        ├── log/
        │   └── gen_kernel_module.log
        └── run/
            └── gen_kernel_module_run.py
        
        10 directories, 22 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_kernel_module <https://vroncevic.github.io/gen_kernel_module>`_

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
