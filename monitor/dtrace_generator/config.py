import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open ("../../config", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("#"):
            continue
        if line.startswith("start_symbol"):
            start_symbol = line.split("=")[1].strip()
        if line.startswith("end_symbol"):
            end_symbol = line.split("=")[1].strip()
        if line.startswith("gap"):
            gap = int(line.split("=")[1].strip())

path_to_table = "../semantic_builder/table.txt"
path_to_libfetcher = '../../host/pa_fetcher/lib_fetcher.so'

if __name__ == "__main__":
    print("config: ./monitor/dtrace_generator")
    print("      start_symbol:   %s" % start_symbol)
    if gap == 0:
        print("        end_symbol:   %s" % end_symbol)
    else:
        print("               gap:   %d" % gap)
    print("     path_to_table:   %s" % path_to_table)
    print("path_to_libfetcher:   %s" % path_to_libfetcher)