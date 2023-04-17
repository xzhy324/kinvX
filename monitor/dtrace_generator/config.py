start_symbol = "sys_call_table"
end_symbol = "_edata"
gap = 100  # if gap != 0 ,then end_symbol is not used
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