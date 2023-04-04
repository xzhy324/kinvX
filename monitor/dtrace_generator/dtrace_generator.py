import time
import sys

import random


with open("counter.txt", "r") as f:
    counter = int(f.read())

dtrace_name = str(counter) + ".dtrace"


def get_cur_symbols():
    ret = {}
    with open("../semantic_builder/table.txt", "r") as f:
        lines = f.readlines()
        lines = lines[62900:63000]
        for line in lines:
            ret[line.split()[0]] = random.randint(0, 2**64)
    return ret


def get_prev_symbols():
    symbols = {}
    with open("result%d.txt" % (counter - 1), "r") as f:
        lines = f.readlines()
    for line in lines:
        name, value = line.split()
        symbols[name] = int(value, 16)
    return symbols


def make_dtrace_header():
    print(
        """input-language C/C++
decl-version 2.0
var-comparability implicit


..main():::ENTER
this_invocation_nonce
0"""
    )


def make_dtrace_variable(name: str, value, modified=0):
    print(name)
    print('"%s"' % value)
    print(modified)


def make_dtrace_ender():
    print(
        """
..main():::EXIT0
this_invocation_nonce
0"""
    )


if __name__ == "__main__":
    cur_symbols = get_cur_symbols()
    prev_symbols = get_prev_symbols() if counter > 0 else cur_symbols

    with open(dtrace_name, "w") as f:
        sys.stdout = f
        make_dtrace_header()
        for name, value in prev_symbols.items():
            make_dtrace_variable(name, value)
        print()
        make_dtrace_ender()
        for name, value in cur_symbols.items():
            make_dtrace_variable(name, value, modified=1)

    with open("result%d.txt" % counter, "w") as f:
        for name, value in cur_symbols.items():
            f.write("%s %s\n" % (name, value))

    with open("counter.txt", "w") as f:
        f.write(str(counter + 1))
