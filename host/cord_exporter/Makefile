obj-m :=cord_exporter.o
KERNEL :=/lib/modules/$(shell uname -r)/build 
PWD :=$(shell pwd)
modules:
	@echo "Generating cord_exporter.ko..."
	@$(MAKE) -C $(KERNEL) M=$(PWD) modules -s

install:modules
	@sudo insmod cord_exporter.ko

uninstall:clean
	@sudo rmmod cord_exporter

run:install uninstall
	$(PWD)/run.sh
clean:  
	@make -C $(KERNEL) M=$(PWD) clean