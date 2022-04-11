#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/stat.h>
#include <string.h>
#include "../sha256.h"


//array mth stores the Merkle Tree Hash
char mth[]="149F173B07EDBAD8DF5BA7EA5FAD18852384FD3CBAD0FE8665687020739281BA"

int main(int argc, char *argv[])
{
	char *Data = {
					"Let us",
					"do something",
					"interesting",
					"this summer"};
						
	uint8_t DataSize[] = {6,12 , 11, 11};
	
	char *merkle_proof[] = {"F57471A3FCF40ABA631A64EC31DC5BAEBC511EE86F0B8193F02884B209227829" ,
	                         "FC283FDC2C82B775CFD1A1EDD61D12E133D4CF0B15ABCD89B8B3768144ACC8AE"};
						
    
	
	printf("\nTesting function: sha256_data()\n");
	printf("Number of tests: 2\n");
	
	char target_file[64]="interesting";
	int target_file_size = 11;
	target_file_hash = sha256_data(target_file, target_file_size, NOT_VERBOSE);
	
	for(int i = 0; i < 2; i++)
	{
		//Computing sha256
		
		strcat(target_file_hash,merkle_proof[i]); //concatenating the sha256 hashes to get the next node
		target_file_hash = sha256_data(target_file_hash,target_file_size+DataSize[i],NOT_VERBOSE);
		target_file_size+=DataSize[i];
	    
	    int c=0;
	
		for(int j = 0; j < 64; j++)
		{
			if(target_file_hash[j] == mth[j])
			{
				c++;
				
			}
			else
			{
				printf("File is corrupt");
			}
		}if(c==64)printf("The file is correct");
		
		
	}
	
	return 0;
}
