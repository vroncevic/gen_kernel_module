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
- [Dependencies](#dependencies)
- [Generation flow](#generation-flow)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python2%20Package%20gen_kernel_module/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_kernel_module/workflows/Install%20Python3%20Package%20gen_kernel_module/badge.svg?branch=master)

Navigate to release **[page](https://github.com/vroncevic/gen_kernel_module/releases/)** download and extract release archive.

To install **gen_kernel_module** type the following:

```
tar xvzf gen_kernel_module-x.y.z.tar.gz
cd gen_kernel_module-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_kernel_module
copying gen_kernel_module/__init__.py -> build/lib.linux-x86_64-2.7/gen_kernel_module
creating build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
copying gen_kernel_module/lkm/__init__.py -> build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
copying gen_kernel_module/lkm/write_template.py -> build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
copying gen_kernel_module/lkm/read_template.py -> build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
copying gen_kernel_module/lkm/module_selector.py -> build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
copying gen_kernel_module/lkm/gen_lkm.py -> build/lib.linux-x86_64-2.7/gen_kernel_module/lkm
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module
copying build/lib.linux-x86_64-2.7/gen_kernel_module/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
copying build/lib.linux-x86_64-2.7/gen_kernel_module/lkm/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
copying build/lib.linux-x86_64-2.7/gen_kernel_module/lkm/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
copying build/lib.linux-x86_64-2.7/gen_kernel_module/lkm/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
copying build/lib.linux-x86_64-2.7/gen_kernel_module/lkm/module_selector.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
copying build/lib.linux-x86_64-2.7/gen_kernel_module/lkm/gen_lkm.py -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm/read_template.py to read_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm/module_selector.py to module_selector.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_kernel_module/lkm/gen_lkm.py to gen_lkm.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_kernel_module.egg-info
writing requirements to gen_kernel_module.egg-info/requires.txt
writing gen_kernel_module.egg-info/PKG-INFO
writing top-level names to gen_kernel_module.egg-info/top_level.txt
writing dependency_links to gen_kernel_module.egg-info/dependency_links.txt
writing manifest file 'gen_kernel_module.egg-info/SOURCES.txt'
reading manifest file 'gen_kernel_module.egg-info/SOURCES.txt'
writing manifest file 'gen_kernel_module.egg-info/SOURCES.txt'
Copying gen_kernel_module.egg-info to /usr/local/lib/python2.7/dist-packages/gen_kernel_module-1.1.0-py2.7.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_kernel_module/run/gen_kernel_module_run.py -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf
copying gen_kernel_module/conf/gen_kernel_module.cfg -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/
copying gen_kernel_module/conf/gen_kernel_module_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/
copying gen_kernel_module/conf/project.yaml -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma
copying gen_kernel_module/conf/template/lkm_vma/Makefile.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/
copying gen_kernel_module/conf/template/lkm_vma/test.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/
copying gen_kernel_module/conf/template/lkm_vma/lkm.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device
copying gen_kernel_module/conf/template/lkm_charachter_device/Makefile.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/
copying gen_kernel_module/conf/template/lkm_charachter_device/test.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/
copying gen_kernel_module/conf/template/lkm_charachter_device/lkm.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device
copying gen_kernel_module/conf/template/lkm_block_device/Makefile.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/
copying gen_kernel_module/conf/template/lkm_block_device/test.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/
copying gen_kernel_module/conf/template/lkm_block_device/lkm.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces
copying gen_kernel_module/conf/template/lkm_network_interfaces/Makefile.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/
copying gen_kernel_module/conf/template/lkm_network_interfaces/test.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/
copying gen_kernel_module/conf/template/lkm_network_interfaces/lkm.template -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/
creating /usr/local/lib/python2.7/dist-packages/gen_kernel_module/log
copying gen_kernel_module/log/gen_kernel_module.log -> /usr/local/lib/python2.7/dist-packages/gen_kernel_module/log/
```

Or You can use docker to create image/container.

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
.
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
│   ├── gen_lkm.py
│   ├── __init__.py
│   ├── module_selector.py
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

Copyright (C) 2018 by [vroncevic.github.io/gen_kernel_module](https://vroncevic.github.io/gen_kernel_module/)

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
