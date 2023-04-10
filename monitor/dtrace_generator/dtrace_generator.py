import sys
import ctypes

# load the shared library from pa_fetcher
fetcher = ctypes.cdll.LoadLibrary('/home/ubuntu/projects/kinvX/host/pa_fetcher/lib_fetcher.so')
fetcher.get_pa.restype = ctypes.c_char_p

with open("counter.txt", "r") as f:
    counter = int(f.read())

dtrace_name = str(counter) + ".dtrace"


def get_cur_symbols():
    ret = {}
    with open("../semantic_builder/table.txt", "r") as f:
        lines = f.readlines()

        # 在data段中分析数据不变式
        for (index, line) in enumerate(lines):
            if line.split()[0] == "_sdata":
                start_position = index
            if line.split()[0] == "_edata":
                end_position = index
                break
        lines = lines[start_position:end_position]

        # 利用动态链接库获取物理内存对应的值
        for line in lines:
            name = line.split()[0]
            physical_address = line.split()[2]
            arg = ctypes.c_char_p(bytes(physical_address, 'utf-8'))
            value = fetcher.get_pa(arg, 8).decode('utf-8') #注意这里的第二个参数，表示读取n个字节，但是该接口没有实现，只能读8个字节
            ret[name] = int(value,16)

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
