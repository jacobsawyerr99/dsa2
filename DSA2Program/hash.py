# this class inits a hash function. It will include the init, lookup, insert, delete

# sources used:
# C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code 
# Received permissoin from professor Ligocki, this code is okay to use from the webinars

#### Big O of class = O(n) worst case. average is o(1) for hash function

class hashFunc:

    #### Big O = O(n)
    # constructor - adopted from C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code 
    def __init__(self, initial_capacity = 1):
        # creates table to be used
        self.table = []
        # loops through initial capacity (i just used 1 for mine)
        for i in range (initial_capacity):
            # appends initial amount onto table
            self.table.append([])

    #### Big O = O(n)
    # inserts/ updates into hashmap.
    # adopted from C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code 
    def insert(self, key, value): #  does both insert and update 
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # update key if it is already in the bucket
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            kv[1] = value
            return True
        
        # if not, insert the item to the end of the bucket list.
        key_value = [key, value]
        bucket_list.append(key_value)
        return True
    
    #### Big O = O(n)
    # looks for key value pair within hashmap, uses key to look up
    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # uses bucket to find Key
        for keyVal in bucket_list:
          #print (key_value)
          if keyVal[0] == key:
            return keyVal[1] # value
        return None
    
    #### Big O = O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
              bucket_list.remove([kv[0],kv[1]])