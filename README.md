# Create KernelModule project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/gen_kernel_module_logo.png" width="25%">

**gen_kernel_module** is tool for creating KernelModule project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

[![gen_kernel_module python checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python_checker.yml) [![gen_kernel_module package checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_kernel_module.svg)](https://github.com/vroncevic/gen_kernel_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/debtux.png)

[![gen_kernel_module python3 build](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_python3_build.yml) [![gen_kernel_module_interface_checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_interface_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_interface_checker.yml) [![gen_kernel_module_isp_checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_isp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_isp_checker.yml) [![gen_kernel_module_srp_checker](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_srp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_kernel_module/actions/workflows/gen_kernel_module_srp_checker.yml)

Currently there are four ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_kernel_module** is located at **[pypi.org](https://pypi.org/project/gen_kernel_module/)**.

You can install by using pip

```bash
# python3
pip3 install gen_kernel_module
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
# python3
python3 get-pip.py
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_kernel_module-*-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_kernel_module/releases)** download and extract release archive.

To install **gen_kernel_module** locate and run setup.py with arguments

```bash
tar xvzf gen_kernel_module-x.y.z.tar.gz
cd gen_kernel_module-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_kernel_module** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_kernel_module** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
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
```
</details>

#### ✨ Features

* Automatically scaffolds KernelModule projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_kernel_module/__init__.py` | 8 | 0 | 100%|
| `gen_kernel_module/core/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_kernel_module/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/core/service/engine.py` | 27 | 0 | 100%|
| `gen_kernel_module/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_kernel_module/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_kernel_module/engine.py` | 57 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/engine.py` | 39 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/icli.py` | 14 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/opt_validator.py` | 36 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_kernel_module/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/gen_kernel_module_command_definition.py` | 24 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/gen_kernel_module_command_executor.py` | 21 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_kernel_module/infrastructure/command/icommand_executor.py` | 13 | 0 | 100%|
| `gen_kernel_module/infrastructure/subprocessor.py` | 55 | 0 | 100%|
| `gen_kernel_module/setup/__init__.py` | 9 | 0 | 100%|
| `gen_kernel_module/setup/bundle.py` | 23 | 0 | 100%|
| `gen_kernel_module/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_kernel_module/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_kernel_module/setup/factory.py` | 48 | 0 | 100%|
| `gen_kernel_module/setup/keys.py` | 27 | 0 | 100%|
| `gen_kernel_module/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_kernel_module/setup/options.py` | 12 | 0 | 100%|
| `gen_kernel_module/setup/registry.py` | 32 | 0 | 100%|
| `gen_kernel_module/setup/validator.py` | 48 | 0 | 100%|
| **Total** | 927 | 0 | 100% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_kernel_module
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/main/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_kernel_module/main/main.py
```

Running tool for creating new KernelModule project skeleton

```bash
python3 main.py create --name mytool --type char --output ./demo/
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-kernel-module/badge/?version=latest)](https://gen-kernel-module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_kernel_module.readthedocs.io](https://gen-kernel-module.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_kernel_module](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2025 - 2026 by [vroncevic.github.io/gen_kernel_module](https://vroncevic.github.io/gen_kernel_module/)

**gen_kernel_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_kernel_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
