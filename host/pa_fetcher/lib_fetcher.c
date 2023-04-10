#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

#define MEM_DEVICE "/dev/dram"
#define BUFSIZE 8 // 一次读入8个字节，64位

char ret[BUFSIZE * 3];

char* get_pa(const char* pa, int bytes) {
    //printf("lib:pa:%s bytes:%d\n", pa, bytes);
    char buffer[BUFSIZE];
    int fd = open(MEM_DEVICE, O_RDONLY);
    if (fd < 0)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }
    long long position = strtoll(pa, NULL, 16);
    lseek64(fd, position, SEEK_SET);
    char *where = buffer;
    int to_read = BUFSIZE;
    while (to_read > 0)
    {
        int nbytes = read(fd, where, to_read);
        if (nbytes <= 0)
            break;
        to_read -= nbytes;
        where += nbytes;
    }
    unsigned char *out = (unsigned char *)buffer;
    //从高到低输出
    int offset = 0;
    offset += sprintf(ret + offset,"0x", out[7]);
    for (int i = BUFSIZE - 1; i >= 0; i--)
    {
        offset += sprintf(ret + offset,"%02x", out[i]); 
    }
    ret[offset] = '\0';
    return ret;
}
