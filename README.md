# Generating Kernel Modules.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/gen_kernel_module/bin/   /root/scripts/gen_kernel_module/ver.1.0/
cp -R ~/gen_kernel_module/conf/  /root/scripts/gen_kernel_module/ver.1.0/
cp -R ~/gen_kernel_module/log/   /root/scripts/gen_kernel_module/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### Tool structure

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/python-tool-docs/gen_kernel_module.png)

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
│   └── template
│       ├── lkm_block_device
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test_lkm.template
│       ├── lkm_charachter_device
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test_lkm.template
│       ├── lkm_network_interfaces
│       │   ├── lkm.template
│       │   ├── Makefile.template
│       │   └── test_lkm.template
│       └── lkm_vma
│           ├── lkm.template
│           ├── Makefile.template
│           └── test_lkm.template
└── log
    └── gen_kernel_module.log

```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/gen_kernel_module

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

