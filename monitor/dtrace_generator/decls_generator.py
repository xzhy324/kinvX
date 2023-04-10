import time
import sys


def get_symbols():
    ret = []
    with open("../semantic_builder/table.txt", "r") as f:
        lines = f.readlines()
        lines = lines[62914:63000]
        for line in lines:
            ret.append(line.split()[0])
    return ret


# decl_name = str(time.strftime('%Y-%m-%d-%H-%M')) + ".decls"
decl_name = "test.decls"


def indent(n=1):
    print("  " * n, end="")


def make_decls_header():
    print(
        """input-language C/C++
decl-version 2.0
var-comparability implicit

ppt ..main():::ENTER
  ppt-type enter"""
    )


def make_decls_ender():
    print(
        """ppt ..main():::EXIT0
  ppt-type subexit"""
    )


def make_decls_variable(
    name, type="variable", rep_type="java.lang.String", dec_type="k_addr"
):
    indent()
    print("variable %s" % name)
    indent(2)
    print("var-kind %s" % type)
    indent(2)
    print("rep-type %s" % rep_type)
    indent(2)
    print("dec-type %s" % dec_type)


if __name__ == "__main__":
    sys.stdout = open(decl_name, "w")
    symbols = get_symbols()

    make_decls_header()
    for symbol in symbols:
        make_decls_variable(symbol)
    print()
    make_decls_ender()
    for symbol in symbols:
        make_decls_variable(symbol)

    with open("counter.txt", "w") as f:
        f.write("0")
