# Phisical Memory Viewer
## Code Introduction
### dram.c
* 旧金山大学高级编程课上找的小工具，主要是通过kmap将物理内存的数据映射到一个设备文件中。
* 通过访问该设备就可以实现访问物理内存的功能。
### bit64_fetcher.c
* 依赖于dram.c的64位物理地址读取器
## Get Started
1. install dram to device-tree and compile bit64_fetcher
```bash
make install
```
2. read 64 bits from a hex physical address and print it from high to low.
```bash
./bit64_fetcher 0x84C00300
# 0xffffffff94f8ff30
```
3. remove device and clean up.
```bash
make uninstall
```


## REF
[2.4 动手实践，代码级-把虚拟内存地址转换为物理内存地址_wdh3837的博客-CSDN博客](https://blog.csdn.net/weixin_39247141/article/details/115291539)
