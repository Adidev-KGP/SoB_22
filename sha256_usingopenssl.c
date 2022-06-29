 #include <openssl/sha.h>

 int SHA1_Init(SHA_CTX *c);
 int SHA1_Update(SHA_CTX *c, const void *data, size_t len);
 int SHA1_Final(unsigned char *md, SHA_CTX *c);
 unsigned char *SHA1(const unsigned char *d, size_t n,
      unsigned char *md);

 int SHA224_Init(SHA256_CTX *c);
 int SHA224_Update(SHA256_CTX *c, const void *data, size_t len);
 int SHA224_Final(unsigned char *md, SHA256_CTX *c);
 unsigned char *SHA224(const unsigned char *d, size_t n,
      unsigned char *md);

 int SHA256_Init(SHA256_CTX *c);
 int SHA256_Update(SHA256_CTX *c, const void *data, size_t len);
 int SHA256_Final(unsigned char *md, SHA256_CTX *c);
 unsigned char *SHA256(const unsigned char *d, size_t n,
      unsigned char *md);

 int SHA384_Init(SHA512_CTX *c);
 int SHA384_Update(SHA512_CTX *c, const void *data, size_t len);
 int SHA384_Final(unsigned char *md, SHA512_CTX *c);
 unsigned char *SHA384(const unsigned char *d, size_t n,
      unsigned char *md);

 int SHA512_Init(SHA512_CTX *c);
 int SHA512_Update(SHA512_CTX *c, const void *data, size_t len);
 int SHA512_Final(unsigned char *md, SHA512_CTX *c);
 unsigned char *SHA512(const unsigned char *d, size_t n,
      unsigned char *md);
