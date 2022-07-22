# SoB_22

# Running the sha256_usingopenssl.c file

1) First compile the file sha256_usingopenssl.c using ```gcc sha256_usingopenssl.c -lcrypto```

2) Let the name of the executable file be a.out

3) run the exccutable file to get the output as follows: ```./a.out sha256```

A tiny and simple C library without dependencies that compute SHA256 digest from a file. Comes with a test program that compute the SHA256 disgest of an input file.

To use this library you need to add these files to your project: ```sha256.c``` and ```sha256.h```. After that, just put ```#include <sha256.h>``` on you main program.

These are the functions available:

```
//Return 32 bytes digest of Data array on success. Return NULL if fail.
//VerboseStatus = SHA256_VERBOSE --> Will print progress
//VerboseStatus = SHA256_NOT_VERBOSE --> Will not print progress
uint8_t *sha256_data(uint8_t *Data, uint64_t DataSizeByte, uint8_t VerboseStatus);

//Return 32 bytes digest of file on success. Return NULL if fail.
//VerboseStatus = SHA256_VERBOSE --> Will print progress
//VerboseStatus = SHA256_NOT_VERBOSE --> Will not print progress
uint8_t *sha256_file(const char *Filename, uint8_t VerboseStatus);

```

# Example Programs

The function ```sha256_data()``` are implemented on example program testdata.c

The function ```sha256_file()``` are implemented on example program testfilehash.c

The example programs can be compiled by runing ```$ make``` on terminal. For compilation you need to have ```gcc``` and ```make``` installed on your machine. If you do not have it, you can install with the command ```$ sudo apt install build-essential``` on Ubuntu.

To build you need make and gcc compiler. After just run: ```$ make```
