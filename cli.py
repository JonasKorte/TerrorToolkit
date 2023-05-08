import core.terror as terror
import os
import argparse as argp
import sys

parser = argp.ArgumentParser(
    prog='TerrotToolkit CLI',
    description='Full Pen-Testing Toolkit',
    epilog='By Jonas Korte'
)

def main(argv):
    terror.scanModules()

    mod_name = argv[1]
    args_list = argv
    args_list.pop(0)
    args_list.pop(0)

    mod_args = {}

    for arg in args_list:
        try:
            mod_args[arg.split('=')[0]] = arg.split('=')[1]
        except IndexError:
            pass


    terror.executeModule(mod_name, args = mod_args)

if __name__ == '__main__':
    main(sys.argv)