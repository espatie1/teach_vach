//include
#include <stdio.h>
#include <stdlib.h>

int main(){
    volatile unsigned long long count = 0;
    for (int i = 0; i <= 1000000000; i++){
        count++;
    }
    printf("Count: %llu\n", count);
    return 0;
}