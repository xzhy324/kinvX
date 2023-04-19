import sys
import config

start_symbol = config.start_symbol
end_symbol = config.end_symbol
gap = config.gap  # if gap != 0 ,then end_symbol is not used
rep_type = config.mode


def get_symbols():
    ret = []
    with open(config.path_to_table, "r") as f:
        lines = f.readlines()
        start_position = -1

        # 在[start_symbol, end_symbol) 或 [start_symbol, start_symbol+gap)中分析数据不变式
        for index, line in enumerate(lines):
            if line.split()[0] == start_symbol:
                start_position = index
            if line.split()[0] == end_symbol:
                end_position = index
        if start_position < 0:
            raise Exception("start_symbol:%s not found" % start_symbol)
        end_position = start_position + gap if gap != 0 else end_position
        lines = lines[start_position:end_position]

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
        make_decls_variable(name=symbol, rep_type=rep_type)
    print()
    make_decls_ender()
    for symbol in symbols:
        make_decls_variable(name=symbol, rep_type=rep_type)

    with open("counter.txt", "w") as f:
        f.write("0")
