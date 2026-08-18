Create KernelModule project skeleton
--------------------------------------

**gen_kernel_module** is tool for creating KernelModule project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_kernel_module python checker| |gen_kernel_module python package| |github issues| |documentation status| |github contributors|

.. |gen_kernel_module python checker| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml

.. |gen_kernel_module python package| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg
   :target: https://github.com/vroncevic/gen_kernel_module/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-kernel_module/badge/?version=latest
   :target: https://gen-kernel_module.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
------------------

|gen_kernel_module python3 build|

.. |gen_kernel_module python3 build| image:: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_kernel_module/releases

To install **gen_kernel_module** type the following

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_kernel_module

📦 Dependencies
-----------------

**gen_kernel_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-------------------

**gen_kernel_module** is based on OOP.

Tool structure

.. code-block:: bash

    gen_kernel_module/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_kernel_module_command_definition.py
         │   │   ├── gen_kernel_module_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_kernel_module.cfg
         │   │   ├── gen_kernel_module.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 44 files

✨ Features
-------------

* Automatically scaffolds Linux Kernel Module (LKM) driver projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
------------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
----------

Install package

.. code-block:: bash

    pip3 install gen_kernel_module

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_kernel_module/main/main.py

Running tool for creating new KernelModule project skeleton

.. code-block:: bash

    python3 main.py create --name mytool --type char --output ./demo/

📚 Docs
---------

More documentation and info at

* `gen_kernel_module.readthedocs.io <https://gen-kernel_module.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
-----------------

`Contributing to gen_kernel_module <https://github.com/vroncevic/gen_kernel_module/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
---------------------------

Copyright (C) 2025 - 2026 by `vroncevic.github.io/gen_kernel_module <https://vroncevic.github.io/gen_kernel_module>`_

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
