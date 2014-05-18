from __future__ import print_function

import argparse

import serial

from blinkm import BlinkM

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='BlinkM CLI.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('device',
            help="Serial i2c bridge to use for communication")

    parser.add_argument('--speed', default=19200, type=int,
            help="Baudrate of the device")

    parser.add_argument('--address', default=0x09, type=int,
            help="i2c address of BlinkM")

    for func, cmd in BlinkM.commands.items():
        if cmd[1] == 0:
            parser.add_argument("--" + func.lower(), action='store_true',
                    help=func)
        else:
            parser.add_argument("--" + func.lower(), nargs=cmd[1],
                    help=func)

    args = parser.parse_args()
    ser = serial.Serial(args.device, args.speed, timeout=0.1)
    b = BlinkM(ser, args.address)
    for func, cmd in BlinkM.commands.items():
        if getattr(args, func.lower()):
            met = getattr(b, func)
            margs = []
            if cmd[1] > 0:
                margs = [int(x) for x in getattr(args, func.lower())]
            ret = met(*margs)
            print(ret)
