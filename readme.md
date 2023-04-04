# kinvX
a runtime kernel invariants detector, based on the [Daikon](https://plse.cs.washington.edu/daikon/) tool. 
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
    > system.map can be replaced by nm inference from a kernel image.
    * table_reader: behold the triple unit table and dictionaryize it to accelerate access.
* Dtrace Generator
    * decls_generator : generate the dtrace's decls part with the help of table_reader.
    * dtrace_generator : generate the dtrace's probe part with the help of table_reader.
* Data Extractor
    > TBC