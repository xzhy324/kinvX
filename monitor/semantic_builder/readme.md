# 物理内存语义重建
## linux内核地址空间
linux内核地址存在着两层随机：
1. 在加载内核时，内核的起始物理地址是随机的，这个随机性是由内核加载器（例如grub）决定的。
2. 在内核运行时，内核的虚拟地址也是随机的，这个随机性是由内核自身的ASLR功能所提供的堆栈随机化决定的。
虽然存在这两重随机性，但是内核符号间的相对偏移是不变的，通过参考System.map文件，我们可以得到任意两个内核符号之间的相对偏移。\
因此，只需要确定任意一个符号的对应的虚拟地址，就能够还原本次启动之后内核的所有符号的虚拟地址。\

## 重建方式
在拥有System.map文件
通过(cord_name, cord_va ,cord_pa) 三元组来重建物理内存语义，其中cord_name为linux内核某一导出符号的名称，cord_va为该符号的虚拟地址，cord_pa为该符号的物理地址。通过这三个元素，我们可以重建出物理内存的语义。

# Usage
## 1. Build Semantics
1. cp `/boot/System.map-*` to a path you want and filled it in the table_initializer.py
2. add read permission to the copied System.map
3. specify the path of the System.map and output file in the table_initializer.py

a possible version of the usage is as follows:
```bash
cd semantic_builder
cp /boot/System.map-5.15.0-56-generic ./
chmod 644 System.map-5.15.0-56-generic
vim table_initializer.py
make run
```

注意：导出System.map步骤可以替换为
```bash
sudo nm path/to/vmlinux > ./System.map # 从vmlinux中导出System.map
```


## 2. Inspect table's layout
```bash
python3 table_inspector.py
```