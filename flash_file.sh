#!/bin/bash
d_port="/dev/ttyUSB0"
d_file="./esp8266-20191220-v1.12.bin"
esptool.py --port $d_port erase_flash
esptool.py --port $d_port --baud 460800 write_flash --flash_size=detect 0 $d_file
