"""

This is an implementation of Merkle Tree Hash Algorithm

"""

import hashlib

class MerkleTreeHash(object):
    def __init__(self):
        pass
    
    def find_merkle_hash(self, file_hashes):
        #Here we are finding the merkle tree hash of all the file file hashes
        #passed to this function. Note we are going to be using recurssion
        #to solve this problem.
        
        #This is the simple procedure we will follow for finding the hashes.
        #Given a list of hashes we first group all the hashes in twos
        #Next we concatenate the hashes in each group and compute the hashes
        #of the group, then keep track of the group hashes. The same steps are
        #repeated until there is a single hash which is the Merkle Tree Hash
        
        blocks = []
        
        if not file_hashes:
            raise ValueError("Missing required file hashes for computing Merkle Tree Hash")
            
        #First we need to sort the hashes    
        for m in sorted(file_hashes):
            blocks.append(m)
            
        list_len = len(blocks)
        #Adjust the block of hashes until we have an even number of items
        #in the blocks, this entails appending to the end of the block 
        #the last entry . To do this we use modulus math to determine when 
        #we have an even number of items.
        
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)
            
        #Now we have an even number of items in the blocks
        #We need to group the items in twos
        
        secondary = []
        
        for k in [blocks[x:x+2] for x in range(0, len(blocks),2)]:
            #Note: k is a list with only 2 items, which is what we want.
            #This is so that we can concatenate them and create a new 
            #hash from them.
            
            hasher = hashlib.sha256()
            hasher.update(k[0].encode('utf-8')+k[1].encode('utf-8'))
            secondary.append(hasher.hexdigest())
            
        #Now because this is a recurssive method, we need to determine when
        #we only have a single item in the list . This marks the end of the 
        #iteration and we can return the last hash as the merkle root.
        
        if len(secondary) ==1:
            return secondary[0]
        else:
            #If the number of items in the lists is more than one, we still
            #need to iterate through this so we pass it back to the 
            #method. We pass the secondary list since it holds the second
            #iteration results.
            return self.find_merkle_hash(secondary)
    
if __name__ == '__main__':
    
    #Ok its time to test the class. We will test by generating 13 random
    #hashes and try to find their merkle tree hash.
    
    import uuid
    file_hashes = []
    
    
    for i in range(0,13):
        file_hashes.append(str(uuid.uuid4().hex))
    
    print('Finding the merkle tree hash of {0} random hashes'.format(len(file_hashes)))
       
    cls=MerkleTreeHash()
    mk = cls.find_merkle_hash(file_hashes)
    print('The merkle tree hash of the hashes below is : {0}'.format(mk))
    print('....')
    print (file_hashes)
        
