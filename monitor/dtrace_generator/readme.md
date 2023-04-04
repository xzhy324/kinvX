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

## Usage

```bash
python decl_generate.py
python dtrace_generator.py
python dtrace_generator.py
python dtrace_generator.py
...
```
```