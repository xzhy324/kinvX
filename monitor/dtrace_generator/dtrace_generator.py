import sys
import ctypes  # load the shared library
import config

start_symbol = config.start_symbol
end_symbol = config.end_symbol
gap = config.gap  # if gap != 0 ,then end_symbol is not used
rep_type = config.mode
bytes_to_read = config.bytes_to_read

# load the shared library from pa_fetcher
fetcher = ctypes.cdll.LoadLibrary(config.path_to_libfetcher)
fetcher.get_pa.restype = ctypes.c_char_p

with open("counter.txt", "r") as f:
    counter = int(f.read())

dtrace_name = str(counter) + ".dtrace"


# 从动态链接库中直接访问dram设备读取裸机内存
def get_cur_symbols():
    ret = {}
    with open(config.path_to_table, "r") as f:
        lines = f.readlines()

        # 在[start_symbol, end_symbol) 或 [start_symbol, start_symbol+gap)中分析数据不变式
        for index, line in enumerate(lines):
            if line.split()[0] == start_symbol:
                start_position = index
            if line.split()[0] == end_symbol:
                end_position = index
        end_position = start_position + gap if gap != 0 else end_position
        lines = lines[start_position:end_position]

        # 利用动态链接库获取物理内存对应的值
        for line in lines:
            name = line.split()[0]
            physical_address = line.split()[2]
            pa_in_char_p = ctypes.c_char_p(bytes(physical_address, "utf-8"))
            value = fetcher.get_pa(pa_in_char_p, bytes_to_read).decode("utf-8")
            ret[name] = int(value, 16)

    return ret


# 从之前保存的文件中读取上一次的数据
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
    if rep_type == "java.lang.String":
        print('"%s"' % value)
    else:
        print(value)
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
            f.write("%s %x\n" % (name, value))

    with open("counter.txt", "w") as f:
        f.write(str(counter + 1))
