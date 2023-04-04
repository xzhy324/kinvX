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
#    @sudo dmesg | tail -1
	@python3 ../../monitor/semantic_builder/table_initializer.py \
		$(shell sudo dmesg | tail -1 | awk '{print $$2}') \
		$(shell sudo dmesg | tail -1 | awk '{print $$3}') \
		$(shell sudo dmesg | tail -1 | awk '{print $$4}')
clean:  
	@make -C $(KERNEL) M=$(PWD) clean