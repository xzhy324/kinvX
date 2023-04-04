obj-m:=dram.o      
CURRENT_PATH := $(shell pwd)       
LINUX_KERNEL := $(shell uname -r)   
LINUX_KERNEL_PATH := /usr/src/linux-headers-$(LINUX_KERNEL) 

build:
	make -C $(LINUX_KERNEL_PATH) M=$(CURRENT_PATH) modules
	gcc bit64_fetcher.c -o bit64_fetcher -w

install: build
	sudo insmod dram.ko
	sudo mknod /dev/dram c 85 0   # major_dev_id(85) is specified in dram.c

uninstall:clean
	sudo rmmod dram.ko
	sudo rm /dev/dram

clean:
	make -C $(LINUX_KERNEL_PATH) M=$(CURRENT_PATH) clean 
	rm bit64_fetcher