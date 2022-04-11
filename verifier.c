#include<stdio.h>
#include<string.h>
#include<math.h>
#include <limits.h>
#define mod ULONG_MAX
#define int unsigned long long int
#define mth ['A','B'] //  this line stores the Merkle Tree Hash in mth

/* Iterative Function to calculate (x^y)%p in O(log y) */
int power(int x,int y,int p)
{
    int res = 1;     // Initialize result
 
    x = x % p; // Update x if it is more than or
                // equal to p
  
    if (x == 0) return 0; // In case x is divisible by p;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}
 
int hextodc(char *hex){ // converts hexadecimal to decimal
  int y = 0;
  int dec = 0;
  int x, i;
  for(i = strlen(hex) - 1 ; i >= 0 ; --i){
      if(hex[i]>='0'&&hex[i]<='9'){
         x = hex[i] - '0';
      }
      else{
         x = hex[i] - 'A' + 10;
      }
      dec = (dec%mod) + ((x%mod) * power(16 , y,mod))%mod;
      dec%=mod;
      y++;// converting hexadecimal to integer value ++y;
      //printf("%d",dec);printf("\n");
  }
  return ((dec%mod)+(mod))%mod;
}
int main(){
    
  int n;
  int sum=0;
  scanf("%lld",n)// this line takes number of hashes in merkle proof which can also be derived as ceil(log2(no. of initial hashes))
  for(int i=0;i<n;i++){
     char hex[100];
     printf("Enter Hexadecimal: ");
     scanf("%s", hex);
     int hex1 = hextodc(hex);
     sum=((sum%mod)+hex1)%mod;
    }
//   printf("\nDecimal: %llu", hextodc(hex));
//   return 0;
    if(hextodc(mth)==sum) printf("The file is correct");
    else printf("The file is incorrect or has been modified");
}
