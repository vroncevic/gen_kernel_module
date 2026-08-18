#!/bin/bash
#
# @brief   gen_kernel_module
# @version 1.4.1
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_kernel_module
pylint gen_kernel_module > gen_kernel_module.report
echo "Done"
