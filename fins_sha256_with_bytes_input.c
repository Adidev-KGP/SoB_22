#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>


int main(){
int c;

unsigned char abc[32];


unsigned char rawdata[] = {0 , 108 , 101 , 102 , 116};

unsigned long n = strlen(rawdata);
unsigned char *d = SHA256(rawdata, 5 , 0);


for (c = 0; c < 32; c++){
    printf("%02x", d[c]);
}printf("\n");


return 0;
}
