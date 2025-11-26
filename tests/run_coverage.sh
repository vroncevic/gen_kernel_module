#!/bin/bash
#
# @brief   gen_kernel_module
# @version v1.0.1
# @date    Sat Aug 1 07:52:38 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_kernel_module_coverage.xml gen_kernel_module_coverage.json .coverage
rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
python3 -m coverage run -m --source=../gen_kernel_module unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_kernel_module_coverage.xml 
python3 -m coverage json -o gen_kernel_module_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n gen_kernel_module
rm htmlcov/.gitignore
echo "Done"