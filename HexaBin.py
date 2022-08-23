#!usr/bin/env python3.10
# coding utf-8
# Author : Isis & Dxsk
# Twitter : https://twitter.com/0x1sis / https://twitter.com/daihyxsk / https://Twitter.com/Vozec1
import re
import argparse
import base64

banner = """
 _    _                ____  _              ___    ___  
| |  | |              |  _ \(_)            |__ \  / _ \ 
| |__| | _____  ____ _| |_) |_ _ __   __   __ ) || | | |
|  __  |/ _ \ \/ / _` |  _ <| | '_ \  \ \ / // / | | | |
| |  | |  __/>  < (_| | |_) | | | | |  \ V // /_ | |_| |
|_|  |_|\___/_/\_\__,_|____/|_|_| |_|   \_/|____(_)___/ 
By Isis  (https://github.com/1sis), Dxsk (https://github.com/dxsk)
and Vozec (https://github.com/Voz3c)
"""

# Check Number
def Check_number(number_input):
    if not number_input.isnumeric():
        log("[-] Please give a real integer",'error')
        exit(-1)
    else:
        return int(number_input)

#####################
#### ENCODE PART ####
#####################

# Number to Hexadecimal
def Num_to_hex(num: int) -> int:
     return hex(Check_number(num))

# Number to Binary
def Num_to_bin(num: int) -> bin:
    return bin(Check_number(num))

# Number to Base64
def Num_to_b64(num: str) -> str:
    return base64.b64encode(bytes(num,'utf-8')).decode()

# Number to Base32
def Num_to_b32(num: str) -> str:
    return base64.b32encode(bytes(num,'utf-8')).decode()

#####################
#### DECODE PART ####
#####################

# Hexadecimal to Number
def Hex_to_num(num: str) -> int:
     return int(num.replace('0x',''), 16)

# Binary to Number
def Bin_to_num(binary: str) -> bin:
    return int(binary, 2)

# Base64 to Number
def B64_to_num(num: str) -> int:
    try:
        return int(base64.b64decode(bytes(num,'utf-8')).decode())
    except:
        log("[-] Invalid Base64 !",'fail')
        return -1

# Base32 to Number
def B32_to_num(num: str) -> int:
    try:
        return int(base64.b32decode(bytes(num,'utf-8')).decode())
    except:
        log("[-] Invalid Base32 !",'fail')
        return -1

###################
#### SWAP PART ####
###################

# Change binary to hexadecimal
def Bin_to_hex(binary: str) -> hex:
    pattern = re.compile("[a-z][A-Z][2-9]")
    if not pattern.match(binary):
        return hex(int(binary, 2))
    else:
        log("[-] It's not a binary number !",'fail')
        return -1

# Change hexadecimal to binary
def Hex_to_bin(hexadecimal: str) -> bin:
    pattern = re.compile("^0x")
    if pattern.match(hexadecimal):
        return bin(int(hexadecimal, 16))
    else:
        log("[-] It's not a hexadecimal number !",'fail')
        return -1


# Parsing
def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(metavar='number',dest="number",type=str,help="Number")
    parser.add_argument("-e", "--encode",choices=['hex', 'bin','base64','base32'],help="Encode your number")
    parser.add_argument("-d", "--decode",choices=['hex', 'bin','base64','base32'],help="Decode your number")
    parser.add_argument("-s", "--swap",choices=['bin2hex', 'hex2bin'],help="Encode your number")
    return parser.parse_args()

# Logging
def log(message: str,color=None):
    context = {
        'blue':'\033[94m',
        'green':'\033[92m',
        'yellow':'\033[93m',
        'fail':'\033[91m',
        None:''
    }
    print('%s%s%s'%(context[color],message,'\033[0m'))

def Change(number: int,args) -> int:
    options_encode = {
        'hex' : Num_to_hex,
        'bin' : Num_to_bin,
        'base64' : Num_to_b64,
        'base32' : Num_to_b32
    }
    options_decode = {
        'hex' : Hex_to_num,
        'bin' : Bin_to_num,
        'base64' : B64_to_num,
        'base32' : B32_to_num
    }
    options_swap = {
        'bin2hex' : Bin_to_hex,
        'hex2bin' : Hex_to_bin
    }
    if(args.encode):
        return options_encode[args.encode](args.number)
    elif(args.decode):
        return options_decode[args.decode](args.number)
    elif(args.swap):
        return options_swap[args.swap](args.number)

    return -1
  
def main(args):
    result = Change(args.number,args)
    if result != -1:
        log('[+] Number \'%s\' <=> %s'%(args.number,result),'green')

if __name__ == "__main__":
    log(banner,'blue')
    main(parseArgs())
