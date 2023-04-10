obj-m :=cord_exporter.o
KERNEL :=/lib/modules/$(shell uname -r)/build 
PWD :=$(shell pwd)  
modules:  
	@$(MAKE) -C $(KERNEL) M=$(PWD) modules

install:modules
	@sudo insmod cord_exporter.ko

uninstall:clean
	@sudo rmmod cord_exporter

run:install uninstall
	zsh run.sh
clean:  
	@make -C $(KERNEL) M=$(PWD) clean