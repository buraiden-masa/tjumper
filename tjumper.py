#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, datetime, sys, os, argparse

def main(sec):

        offset = sec
        now_t = time.time()

        print("Correct {0} second.......".format(sec))

        if now_t + sec < 0:
                print("error: Specified time is too large, over the unix time !")
                exit(99)

        print("current   time = {0}".format(datetime.datetime.fromtimestamp(now_t)))

        conv_t = now_t + offset
        try:
                os.system("date -s '{0}' > /dev/null ".format(datetime.datetime.fromtimestamp(conv_t)))

        except OSError as e:
                print("except : Cannot set the time. errno={0}, msg=[{1}]".format(e.errno, e.strerror))
                exit(98)

        # Re-acquisition of current time
        conv_t = time.time()
        print("converted time = {0}".format(datetime.datetime.fromtimestamp(conv_t)))
        return 0

if __name__ == "__main__":

        parser = argparse.ArgumentParser(
                        prog='tjumper.py',
                        usage='Correct the system clock arbitray number of seconds',
                        description='description',
                        epilog='[EOF]',
                        add_help='True',
                        )

        parser.add_argument('-t', '--time',
                        help='specify the number of seconds you wanna advance/rewind',
                        type=int,
                        nargs=1,
                        )

        parser.add_argument('-d', '--date',
                        help='show current system clock',
                        action='store_true',
                        )

        # Analyze arguments...
        args = parser.parse_args()

        if args.date:
                cur_t = time.time()
                print("{0}".format(datetime.datetime.fromtimestamp(cur_t)))

        if args.time:
                main(args.time[0])
