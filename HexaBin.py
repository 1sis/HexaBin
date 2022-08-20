#!usr/bin/env python3.10
# coding utf-8
# Author : Isis & Dxsk
# Twitter : https://twitter.com/0x1sis / https://twitter.com/daihyxsk

import re
import sys
import argparse

banner = """
  _    _                ____  _              __  __ 
 | |  | |              |  _ \(_)            /_ |/_ |
 | |__| | _____  ____ _| |_) |_ _ __   __   _| | | |
 |  __  |/ _ \ \/ / _` |  _ <| | '_ \  \ \ / / | | |
 | |  | |  __/>  < (_| | |_) | | | | |  \ V /| |_| |
 |_|  |_|\___/_/\_\__,_|____/|_|_| |_|   \_/ |_(_)_|
By Isis (https://github.com/1sis) & Dxsk (https://github.com/dxsk)
"""

# Check Number
def check_number(number_input):
    if not number_input.isnumeric():
        print("[-] Please give a real integer")
        sys.exit(1)
    else:
        return int(number_input)

# Number to Hexadecimal
def number_to_hexadecimal(number: int) -> int:
     return hex(check_number(number))

# Number to Binary
def number_to_binary(num: int) -> bin:
    return bin(check_number(num))

# Change binary to hexadecimal
def binary_to_hexadecimal(binary: str) -> hex:
    pattern = re.compile("[a-z][A-Z][2-9]")
    if not pattern.match(binary):
        number = int(binary, 2)
        return hex(number)
    else:
        print("[-] It's not a binary number !")

# Change hexadecimal to binary
def hexadecimal_to_binary(hexadecimal: str) -> bin:
    pattern = re.compile("^0x")
    if pattern.match(hexadecimal):
        num = int(hexadecimal, 16)
        return bin(num)
    else:
        print("[-] It's not a hexadecimal number !")


# Parsing
def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hex", "--hexadecimal", help="Change your number to hexadecimal")
    parser.add_argument("-bin","--binary", help="Change your number to binary")
    parser.add_argument("-b2h", "--bin2hex", help="Change binary number to hexadecimal")
    parser.add_argument("-h2b", "--hex2bin", help="Change hexadecimal number to binary")
    return parser.parse_args()

def main(arguments):

    is_number_to_hexadecimal = arguments.hexadecimal
    is_number_to_binary = arguments.binary
    is_binary_to_hexadecimal = arguments.bin2hex
    is_hexadecimal_to_binary = arguments.hex2bin

    if is_number_to_hexadecimal is not None:
        print(f"[+] number {is_number_to_hexadecimal} = {number_to_hexadecimal(is_number_to_hexadecimal)}")
    
    if is_number_to_binary is not None:
        print(f"[+] number {is_number_to_binary} = {number_to_binary(is_number_to_binary)}")
        
    if is_binary_to_hexadecimal is not None: 
        print(f"[+] number {is_binary_to_hexadecimal} = {binary_to_hexadecimal(is_binary_to_hexadecimal)}")
    
    if is_hexadecimal_to_binary is not None:
        print(f"[+] number {is_hexadecimal_to_binary} = {hexadecimal_to_binary(is_hexadecimal_to_binary)}")


if __name__ == "__main__":
    print(banner)
    main(arguments=parseArgs())