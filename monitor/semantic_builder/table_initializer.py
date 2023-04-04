import sys

path_to_system_map = "/home/ubuntu/projects/lkm_samples/semantic_builder/System.map-5.15.0-67-generic"
path_to_table_txt = "/home/ubuntu/projects/lkm_samples/semantic_builder/table.txt"

cord = {
    "name": "",
    "va": "",
    "pa": ""
}
offset = 0
table = {}


if len(sys.argv) < 4:
    print("Usage: python3 table_initializer.py cord_name cord_va cord_pa")
    exit(1)

cord["name"] = sys.argv[1]
cord["va"] = sys.argv[2]
cord["pa"] = sys.argv[3]

print("table_initializer.py: {}".format(cord))

fin = open(path_to_system_map, "r")
fout = open(path_to_table_txt, "w")

records = fin.read().splitlines()
for record in records:
    va, type_, name = record.split(" ")
    # 只导出位于高地址空间的内核符号
    if int(va, 16) >= 0xffffffff00000000:
        table[name]= [int(va, 16), 0]

# 通过给定的坐标cord，计算出va和pa的偏移量
va_offset = int(cord["va"], 16) - table[cord["name"]][0]
va2pa_offset = int(cord["pa"], 16) - int(cord["va"], 16)


# 根据计算出的偏移量更新table
for name in table.keys():
    table[name][0] = table[name][0] + va_offset
    table[name][1] = table[name][0] + va2pa_offset
    msg ="%s %#X %#X\n" % (name, table[name][0], table[name][1])
    fout.write(msg)
    
fin.close()
fout.close()
    