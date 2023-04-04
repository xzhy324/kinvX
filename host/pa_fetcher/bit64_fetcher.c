#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

#define MEM_DEVICE "/dev/dram"
#define BUFSIZE 8 // 一次读入8个字节，64位
char buffer[BUFSIZE];

int main(int argc, char **argv)
{
    // 打开 /dev/mem 设备文件
    int fd = open(MEM_DEVICE, O_RDONLY);
    if (fd < 0)
    {
        perror("open");
        exit(EXIT_FAILURE);
    }

    long long position = 0LL;
    if(argc < 2){
        exit(-1);
    } else {
        position = strtoll(argv[1], NULL, 16);
    } 
    // position &= 0xFFFFF000; //page aligned
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
    printf("0x");
    //从低到高输出
    // for (int i = 0; i < BUFSIZE; i++)
    // {
    //     printf("%02x", bp[i]);
    // }
    // printf("\n");

    //从高到低输出
    for (int i = BUFSIZE - 1; i >= 0; i--)
    {
        printf("%02x", out[i]);
    }
    printf("\n");
}
