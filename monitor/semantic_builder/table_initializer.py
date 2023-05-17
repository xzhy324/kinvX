import sys
import config

path_to_system_map = config.path_to_system_map
path_to_table_txt = config.path_to_table_txt

cord = {"name": "", "va": "", "pa": ""}
offset = 0
table = {}


if len(sys.argv) < 4:
    print("Usage: \n>  python3 table_initializer.py cord_name cord_va cord_pa")
    exit(1)

cord["name"] = sys.argv[1]
cord["va"] = sys.argv[2]
cord["pa"] = sys.argv[3]

print("table_initializer.py: {}".format(cord))

fin = open(path_to_system_map, "r")
fout = open(path_to_table_txt, "w")

symbol_type = {}
for type_ in config.symbol_type:
    symbol_type[type_] = 0


records = fin.read().splitlines()
for record in records:
    va, type_, name = record.split(" ")
    # 只导出位于高地址空间的部分内核符号
    if int(va, 16) >= 0xFFFFFFFF00000000 and type_ in symbol_type.keys():
        table[name] = [int(va, 16), 0]
        symbol_type[type_] += 1

# 打印type_counter各种数据类型的数量 到stdout
for type_ in symbol_type.keys():
    print("table_initializer.py: {} {}".format(type_, symbol_type[type_]))

# 通过给定的坐标cord，计算出va和pa的偏移量
va_offset = int(cord["va"], 16) - table[cord["name"]][0]
va2pa_offset = int(cord["pa"], 16) - int(cord["va"], 16)


# 根据计算出的偏移量更新table
for name in table.keys():
    table[name][0] = table[name][0] + va_offset
    table[name][1] = table[name][0] + va2pa_offset
    msg = "%s %#X %#X\n" % (name, table[name][0], table[name][1])
    fout.write(msg)

fin.close()
fout.close()
