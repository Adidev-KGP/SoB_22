#ifndef SHA256_H
#define SHA256_H

#define VERBOSE		1
#define NOT_VERBOSE	0

/******************************************************************************/
//Return 32 bytes digest of Data array on success. Return NULL if fail.
//VerboseStatus = SHA256_VERBOSE --> Will print progress
//VerboseStatus = SHA256_NOT_VERBOSE --> Will not print progress
uint8_t *sha256_data(uint8_t *Data, uint64_t DataSizeByte, uint8_t VerboseStatus);

//Return 32 bytes digest of file on success. Return NULL if fail.
//VerboseStatus = SHA256_VERBOSE --> Will print progress
//VerboseStatus = SHA256_NOT_VERBOSE --> Will not print progress
uint8_t *sha256_file(const char *Filename, uint8_t VerboseStatus);


#endif
