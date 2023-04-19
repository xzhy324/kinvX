# kinvX
a runtime kernel invariants detector, based on the [Daikon](https://plse.cs.washington.edu/daikon/) tool. 

## Usage
create config file from template
```bash
cp ./config.template ./config
```

edit ./config to specify the scope of the kernel symbols you want to detect invariants for.


```bash
# ./config
# start symbol must be specified
start_symbol=sys_call_table 
# either end_symbol or gap must be specified
end_symbol=_edata
gap=100
mode=java.lang.String
byte_to_read=8
```
```
> Assume that 
> 1. end_symbol's address HIGHER than start_symbol's address 
> 2. gap >= 0
> 3. mode is one of [java.lang.String, int, float, hashcode] (See DaiKon's doc for more details)
```
```
NOTE THAT:
if gap == 0 then
    scope = [start_symbol, end_symbol)
else
    scope = [start_symbol, start_symbol + gap)
```

initialize kinvX when kernel starts up
```bash
make install
```

generate kernel dtrace (kernel snapshot) during runtime,\
note that this process can be repeated multiple times to generate multiple dtrace
```bash
make generate_dtrace
```

run daikon to detect invariants based on the generated dtrace
```bash
make generate_invariants
```

reset the dtrace and invariants so another round of dtrace-generation and invariants-inference can be started
```bash
make reset
``` 

compare the invariants with the previous one
```bash
cd ./monitor/invariants
make diff 1.inv 2.inv
```

uninstall kinvX
```bash
make uninstall
```

## Requirements
1. Daikon [make sure $DAIKONDIR is set and jdk version >= 1.8]
2. linux-headers (kernel version >= 3.0)
3. python3


## Roadmap
### Host Side
* Page Fetcher
    * dram : char-type kernel driver to resolve high-end memspace
    * bit64_fetcher : a 64-bit physical address's value fetcher
* Cordinate Exporter
    * cordinate_exporter : export the self-recurssive cordinate to help build kernel space's semantics. Imported by semantic-builder on monitor's side.
    * shell script : a shell script to pass out the message from kernel's ring buffer. 
    > [which could be replaced by a module in future.]
### Monitor Side
* Semantic Builder
    * table_initializer : build the kernel space's semantics with the help of cord-exporter and system.map and result in forms of triple unit <name, va, pa>, which is used to detect the invariants.
    * table_reader: behold the triple unit table and dictionaryize it to accelerate access.
* Dtrace Generator
    * decls_generator : generate the dtrace's decls based on initialized table.
    * dtrace_generator : generate the dtrace based on initialized table.

* Invariants Detector
    * invariants_utils : useful tools for invariants file's diff and print. Also a folder to store the .inv files in a non-conflict naming way.