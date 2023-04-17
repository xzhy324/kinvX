# kinvX
a runtime kernel invariants detector, based on the [Daikon](https://plse.cs.washington.edu/daikon/) tool. 

## Usage

initialize when kernel starts up
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