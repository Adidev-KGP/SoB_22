"""

This is an implementation of Merkle Tree Hash Algorithm and Algorithm to generate Merkle Proof

"""

##############################################################################################################################################

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
            
            
        for m in file_hashes:
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
            
            token=k[0]+k[1]
            d = (hashlib.sha256(token.encode('utf-8')).hexdigest())
            secondary.append(d)
            
            #The sha256 strings are directly concatenated
            #and their sha256 is produced again to get the 
            #next node of the Merkle Tree
            
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
            

##############################################################################################################################################

    """

    This is an implementation of algorithm to generate Merkle Proof
 
    """          
    
    def find_merkle_proof(self,blocks,target_hash,proof):
        
        #Here we are finding the merkle proof of all the file hashes
        #passed to this function. Note we are going to be using recurssion
        #to solve this problem.
        
        #This is the simple procedure we will follow for finding the merkle proof.
        #Given a list of hashes we first group all the hashes in twos
        #Next we concatenate the hashes in each group and see if the target hash belongs to any of the pair.
        #If so then the other hash of the pair is pushed as a part of the proof.
        #Now the concatenated hashes are the new set of hashes with the target hash as the concatenated pair
        #having the target hash. 
        #This set of new hashes with the new target hash is passed on. Using this recurssive
        #solution we find the merkle proof.
    
        
        if len(blocks) ==1:
            return proof
            
        #Now because this is a recurssive method, we need to determine when
        #we only have a single item in the list . This marks the end of the 
        #iteration and we can return the proof as the merkle proof.
        
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
            
            token=k[0]+k[1]
            d = (hashlib.sha256(token.encode('utf-8')).hexdigest())
            secondary.append(d)
            
            #The sha256 strings are directly concatenated
            #and their sha256 is produced again to get the 
            #next node of the Merkle Tree
            
            #Now we have to compare if the target hash is present
            #in the pair of hashes that are to be concatenated
            
            if(target_hash==k[0]):
                
                proof.append(k[1]) #The hash which does not match with the target hash in the pair is appended to the proof
                target_hash=d
                
            elif(target_hash==k[1]):
                
                proof.append(k[0]) #The hash which does not match with the target hash in the pair is appended to the proof
                target_hash=d
            
        return self.find_merkle_proof(secondary,target_hash,proof)
        
############################################################################################################################################
        
    
if __name__ == '__main__':
    
    #Ok its time to test the class. We will test by generating n random
    #hashes and try to find their merkle tree hash.
    n=int(input("Enter the number of files"))
    import uuid
    
    file_hashes = []
    hashes_near_power_2 = []
    hashes_after_near_power_2 = []
    
    cls=MerkleTreeHash() #creating an instance of class
    
    
    k= 0;
    while((1<<k)<n):
        k+=1
    k-=1
    
    #where pow(2,k)<n and k is the largest possible number to satisfy this condition
    
    c=0 #counter variable
    
    for i in range(0,n):
        token = uuid.uuid4()
        d = (hashlib.sha256(token.bytes).hexdigest())
        file_hashes.append(d)
        if(c<=(1<<k)):
            hashes_near_power_2.append(d)
        else:
            hashes_after_near_power_2.append(d)
            
            
    #root_hash_1 stores the Merkle Root Hash that is formed from the pow(2,k)
    #number of hashes which is a subset of the initial given Merkle Tree
    
    root_hash_1 = cls.find_merkle_hash(hashes_near_power_2) 
 
################################################  replace_leaf  ############################################################################   
    #replace_leaf takes 2 parameters:
    #1) index: the index which is to be replaced
    #2) the hash value with which that particular index has to be replaced

    def replace_leaf(index , new_hash):
        #merkle_proof_old stores the Merkle Root Hash of the initial Merkle Tree
        
        proof= []
        
        merkle_proof_old = cls.find_merkle_proof(file_hashes,file_hashes[index],proof)
        
        #Now the Merkle Tree that is stored in file_hashes is updated with the new_hash
        
        file_hashes[index] = new_hash
        
        #new_file_set_hash_with_proof_hash stores the
        #1) new_hash
        #2) followed by the old Merkle Proof of the index
        #Together with the old Merkle Proof and new_hash the new Merkle Root Hash can be generated
        
        new_file_set_hash_with_proof_hash = []
        
        new_file_set_hash_with_proof_hash.append(new_hash)
        
        #new_file_set_hash_with_proof_hash is now storing the old Merkle Proof of index
        
        for i in range(0,len(merkle_proof_old)):
            new_file_set_hash_with_proof_hash.append(merkle_proof_old[i])
            
        
        new_root_hash = cls.find_merkle_hash(new_file_set_hash_with_proof_hash)
        
        return new_root_hash
################################################  replace_leaf  ############################################################################

################################################  append_new_hashes ############################################################################

    #append_new_hashes takes two parameters
    #1) the number of hashes to be added to the Merkle Tree ,k
    #2) the list of hashes which are to be added to the old Merkle Tree
       
    def append_new_hashes(k , hash_list):
        
        file_hashes.extend(hash_list)  # to make sure that the Merkle Tree is udated
        
        #hashes_after_near_power_2 is now updates with the hash_list
        hashes_after_near_power_2.extend(hash_list)   #error --> resolve it
       
        #the Merkle Tree Hash of hashes_after_near_power_2 is generated as root_hash_2
        root_hash_2 = cls.find_merkle_hash(hashes_after_near_power_2)
        
        #the concatenation of root_hash_1 and root_hash_2 gives the final updated Merkle Tree Hash
        token = root_hash_1 + root_hash_2
        return (hashlib.sha256(token.encode('utf-8')).hexdigest())
        
        
################################################  append_new_hashes  ############################################################################
                 
    
    #Printing the results
    
    print('....')
    print("....")

    print("The initial hashes are : {0}".format(file_hashes))
    
    ch = int(input('''Enter your choice:
                   1:Find the Merkle Root Hash
                   2:Find the Merkle Proof of a particular leaf in Merkle tree
                   3:Replace a particular leaf in Merkle Tree with other hash and get the new Merkle Root hash
                   4:Add new hashes to the existing Merkle Tree'''))
    
    cls=MerkleTreeHash()
    
    if(ch ==1):
        mk = cls.find_merkle_hash(file_hashes)
        print('Finding the merkle tree hash of {0} random hashes'.format(len(file_hashes)))
        print('The merkle Root hash of the hashes below is : {0}'.format(mk))
        
    elif(ch == 2):
        proof = []
        num=int(input("Enter the file number you want the proof for"))
    
        if(num<=n):
            mp = cls.find_merkle_proof(file_hashes,file_hashes[num-1],proof)
             print('The merkle proof of the Target Hash is :\n')
             print('{0}'.format(mp))
        else:
             print("Invalid request :(")
             
    elif(ch == 3):
        index = int(input("Enter the index of the leaf you want to replace"))
        if(index<n):
            new_hash = input("Enter the hash you want to replace with")
            print(replace_leaf(index , new_hash))
        else:
            print("Invalid response :(")
            
    elif(ch == 4):
        
        k =int(input("Enter the number of hashes you want to append"))
        hash_list = []
        for i in range(0,k):
            z = input("Enter the hash")
            hash_list.append(z)
        print(append_new_hashes(k,hash_list))
        
        
