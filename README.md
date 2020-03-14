# Generating Kernel Modules.

gen_kernel_module is toolset for generation Linux Kernel Module project.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_kernel_module/workflows/Python%20package/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/graphs/contributors)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/gen_kernel_module/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf gen_kernel_module-1.0.tar.gz
cd gen_kernel_module-1.0/python-tool
cp -R ~/bin/   /root/scripts/gen_kernel_module/
cp -R ~/conf/  /root/scripts/gen_kernel_module/
cp -R ~/log/   /root/scripts/gen_kernel_module/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF LINUX KERNEL MODULE

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/python-tool-docs/gen_kernel_module_flow.png)

### TOOL STRUCTURE

gen_kernel_module is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/python-tool-docs/gen_kernel_module.png)

Generator structure:

```
.
├── bin
│   ├── gen_kernel_module.py
│   ├── gen_kernel_module_run.py
│   └── lkm
│       ├── gen_lkm.py
│       ├── __init__.py
│       ├── module_selector.py
│       ├── read_template.py
│       └── write_template.py
├── conf
│   ├── gen_kernel_module.cfg
│   ├── gen_kernel_module_util.cfg
│   ├── project.yaml
│   └── template
│       ├── lkm_block_device
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test.template
│       ├── lkm_charachter_device
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test.template
│       ├── lkm_network_interfaces
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test.template
│       └── lkm_vma
│           ├── lkm.template
│           ├── Makefile.template
│           └── test.template
└── log
    └── gen_kernel_module.log
```

### COPYRIGHT AND LICENCE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Copyright (C) 2018 by https://vroncevic.github.io/gen_kernel_module

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

