# Daikon front-end for data-only scenarios
v0.01
## introduction
This repo contains a front-end for Daikon that is designed to be used in data invariants inference. It is based on the [Daikon](https://plse.cs.washington.edu/daikon/) tool. 
A typical usage scenario is the following:

1. define a set of data in representation of <key, value> pairs
2. run decl_generate.py to generate a decl file for your data_set
3. run dtrace_generator.py to generate a dtrace file , and this step can be repeated multiple times,each time will use the previous data as init_state and 


## Flow
1. dataset in <key, value> format to generate decl file
2. (result0 =>) 0.dtrace => result0 => 1.dtrace => result1 => 2.dtrace => result2 => ... => n.dtrace => resultn \
> 0.dtrace use cur_data as prev_data so it's a const map

## Usage [deprecated]
please use the Makefile in root directory.

```bash
python decl_generate.py
python dtrace_generator.py
python dtrace_generator.py
python dtrace_generator.py
...
```


## Intermediary File's Format
for .dtrace and .decl file, please refer to [Daikon](https://plse.cs.washington.edu/daikon/)'s tutorial.
### .decls
kernel data is all in represention of Java.lang.String(a type supported in Daikon), which is specified in each item's declaration in .decl file. \
The reason why I choose to use String is that int type used in Daikon is only **4-Byte** long, which is not enough for **64-Bit** address(which is common for kernel symbols's value). 

### .dtrace
all symbols are in <key, value> format, in which the key is the name of the variable, and the value is 64 bits fetched from the symbol.
Value field is represented in decimal format.

### result*.txt
they are duplicate of .dtrace file, but in a more readable and parsable format. 
Value field is represented in hex format.
