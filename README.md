<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module_logo.png" width="25%">

# Generating Kernel Modules

**gen_kernel_module** is tool for generation Linux Kernel Module project.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_kernel_module/workflows/Python%20package%20gen_kernel_module/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow](#generation-flow)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python2%20Package%20gen_kernel_module/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python3%20Package%20gen_kernel_module/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_kernel_module/)**.

You can install by using pip
```
# python2
pip install gen-kernel-module
# python3
pip3 install gen-kernel-module
```

##### Install using setuptools

Navigate to release **[page](https://github.com/vroncevic/gen_kernel_module/releases/)** download and extract release archive.

To install modules, locate and run setup.py with arguments
```
tar xvzf gen_kernel_module-x.y.z.tar.gz
cd gen_kernel_module-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

[![gen_kernel_module docker checker](https://github.com/vroncevic/gen_kernel_module/workflows/gen_kernel_module%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions?query=workflow%3A%22gen_kernel_module+docker+checker%22)

### Dependencies

**gen_kernel_module** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module_flow.png)

### Tool structure

**gen_kernel_module** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module.png)

Generator structure:

```
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_kernel_module/badge/?version=latest)](https://gen_kernel_module.readthedocs.io/projects/gen_kernel_module/en/latest/?badge=latest)

More documentation and info at:
* [gen_kernel_module.readthedocs.io](https://gen_kernel_module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_kernel_module](https://vroncevic.github.io/gen_kernel_module)

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
