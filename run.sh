#!/usr/bin/env bash

python3 main.py create --name "my_char_driver" --type "char" --output "./demo/char"
python3 main.py create --name "my_block_driver" --type "block" --output "./demo/block"
python3 main.py create --name "my_net_driver" --type "net" --output "./demo/net"
python3 main.py create --name "my_vma_driver" --type "vma" --output "./demo/vma"
