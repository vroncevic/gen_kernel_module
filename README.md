# Generating Kernel Modules

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module_logo.png" width="25%">

**gen_kernel_module** is tool for generation Linux Kernel Module project.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_kernel_module python checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml) [![gen_kernel_module package checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/debtux.png)

[![gen_kernel_module python3 build](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_kernel_module/)**.

You can install by using pip

```bash
# python3
pip3 install gen-kernel-module
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_kernel_module/releases/)** download and extract release archive.

To install **gen_kernel_module** type the following

```bash
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
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/gen_kernel_module/releases/)** download and extract release archive.

To install **gen_kernel_module** locate and run setup.py with arguments

```bash
tar xvzf gen_kernel_module-x.y.z.tar.gz
cd gen_kernel_module-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_kernel_module** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Tool structure

**gen_kernel_module** is based on OOP.

Generator structure

```bash
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_kernel_module/badge/?version=latest)](https://gen-kernel-module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at
* [gen_kernel_module.readthedocs.io](https://gen-kernel-module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/gen_kernel_module](https://vroncevic.github.io/gen_kernel_module)

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
