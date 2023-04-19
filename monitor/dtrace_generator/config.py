import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("../../config", "r") as f:
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
        if line.startswith("mode"):
            mode = line.split("=")[1].strip()
            if mode not in ["java.lang.String", "int", "hashcode", "float"]:
                raise Exception(
                    "mode should be one of one of [ java.lang.String, int, hashcode , float ]"
                )
        if line.startswith("bytes_to_read"):
            bytes_to_read = int(line.split("=")[1].strip())

path_to_table = "../semantic_builder/table.txt"
path_to_libfetcher = "../../host/pa_fetcher/lib_fetcher.so"

if __name__ == "__main__":
    print("\n./monitor/dtrace_generator/config.py:")
    print("%20s:   %s" % ("Daikon.rep-type", mode))
    print("%20s:   %s" % ("start_symbol", start_symbol))
    if gap == 0:
        print("%20s:   %s" % ("end_symbol", end_symbol))
    else:
        print("%20s:   %s" % ("gap", gap))
    print("%20s:   %s" % ("bytes_to_read", bytes_to_read))
    print("%20s:   %s" % ("table", path_to_table))
    print("%20s:   %s" % ("libfetcher", path_to_libfetcher))
