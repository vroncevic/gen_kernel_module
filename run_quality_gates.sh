#!/bin/bash
#
# @brief   gen_kernel_module
# @version 1.4.0
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_kernel_module
python3 gates/gates/isp_checker.py gen_kernel_module
python3 gates/gates/limits_checker.py gen_kernel_module
python3 gates/gates/srp_checker.py gen_kernel_module

echo "Done"
