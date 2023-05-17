import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("../../config", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("symbol_type"):
            symbol_type = line.split("=")[1].strip("[]\n").split(",")
            symbol_type = [symbol.strip() for symbol in symbol_type]

path_to_system_map = "./System.map"
path_to_table_txt = "./table.txt"
