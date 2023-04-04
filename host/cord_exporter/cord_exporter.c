#include <linux/module.h>

static int h_init(void)
{
    printk("[cord_exporter.ko] init");
    unsigned long page_offset = __START_KERNEL_map; //should be 0xffffffff80000000 on x86 no matter what
    unsigned long value = phys_base; // random value on each startup
    unsigned long va = &phys_base;
    unsigned long pa = va - page_offset + value; //use phys_base's value, vaddr and a constant to calculate the paddr of phys_base
    printk("phys_base 0x%lx 0x%lx",va,pa);
    return 0;
}

static void h_exit(void)
{
    printk("[cord_exporter.ko] exit");
}

module_init(h_init);
module_exit(h_exit);
MODULE_LICENSE("GPL");