path_to_table_txt = "/home/ubuntu/projects/kinvX/monitor/semantic_builder/table.txt"


def load_table():
    table = {}
    with open(path_to_table_txt, "r") as f:
        records = f.read().splitlines()
        for record in records:
            name, va, pa = record.split(" ")
            table[name] = (int(va, 16), int(pa, 16))
    return table


if __name__ == "__main__":
    table = load_table()
    symbols = [
        # "sys_call_table",
        # "idt_table",
        # "phys_base",
        "_stext",
        "_etext",
        "__start_rodata",
        "__end_rodata",
        "_sdata",
        "_edata",
        "__init_begin",  # __init_begin和__init_end为init段的起始和结束地址，包含了大部分模块初始化的数据。
        "__init_end",
        "__bss_start",  # __bss_start和__bss_stop为BSS段的开始和结束地址，包含初始化为0的所有静态全局变量
        "__bss_stop",
    ]
    for index, item in enumerate(table):
        if item in symbols:
            print(
                "%6d %20s  0x%x  0x%x" % (index, item, table[item][0], table[item][1])
            )
