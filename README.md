# SoB_22

# Running the sha256_usingopenssl.c file

1) First compile the file sha256_usingopenssl.c using ```gcc sha256_usingopenssl.c -lcrypto```

2) Let the name of the executable file be a.out

3) run the exccutable file to get the output as follows: ```./a.out sha256```

A tiny and simple C library without dependencies that compute SHA256 digest from a file. Comes with a test program that compute the SHA256 disgest of an input file.

To use this library you need to add these files to your project: ```sha256.c``` and ```sha256.h```. After that, just put ```#include <sha256.h>``` on you main program.
