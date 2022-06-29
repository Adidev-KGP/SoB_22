def verify_merkle_proof(index : int , leaf : bytes , proof : List[bytes]):

    len=obj.__len__()
 
    left_len = largest_power_of_2_less_than(len)

    index+=1

    level=0

    if index <= left_len:
            for i in proof:
                if(index % 2 ==0):
                    ver_root = combine_hashes(i,leaf)
                    leaf=ver_root
                    level+=1

                else:
                    ver_root = combine_hashes(leaf,i)
                    leaf=ver_root
                    level+=1
                    
                index = math.ceil(index/2)


    elif (index == len):
        for i in proof:
            ver_root = combine_hashes(i,leaf)
            leaf = ver_root

    return ver_root
