#!/bin/bash
#
# @brief   gen_kernel_module
# @version 1.4.0
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "my_char_driver" --type "char" --output "./demo/char"
python3 main.py create --name "my_block_driver" --type "block" --output "./demo/block"
python3 main.py create --name "my_net_driver" --type "net" --output "./demo/net"
python3 main.py create --name "my_vma_driver" --type "vma" --output "./demo/vma"
