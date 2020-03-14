# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        # New head
        new_head = LinkedPair(key, value)
        # if the Linked list is empty
        if self.head == None:
            # create first entry
            self.head = new_head
        # If the linked list is NOT empty
        else:
            # store old head
            old_head = self.head
            # Save new value as head
            self.head = new_head
            # set the next value of the new head
            self.head.next = old_head

    def contains(self, key):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next

    def remove(self, key):
        if not self.head:
            print("Error: Key not found")
        elif self.head.key == key:
            # Remove head
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    # Remove node
                    parent.next = current.next
                    return
                current = current.next
            print("Error: Key not found")

    def retrieve(self, key):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return False


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.bucket = LinkedList()

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # 1. use hash_mod to turn our key into an index
        index = self._hash_mod(key)
        new_entry = LinkedPair(key, value)
        # 2. check in storage if something is at that index already
        if self.storage[index] is not None:
            print("WARNING you are overwriting stuff")
            pair = self.storage[index]
            done = False
            # 1.Loop on linkedlist
            while pair is not None and not done:
                # if the key is the same as the current key overwrite value
                if pair.key is key:
                    pair.value = value
                    done = True
                # Else create a new entry
                else:
                    pair.next = new_entry
                    done = True
        # 3. If there is nothing at index
        else:
            self.storage[index] = new_entry

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # 1.create hash
        hash_key = self._hash_mod(key)
        # 2. Find the index in the array
        if self.storage[hash_key]:
            self.storage[hash_key] = None
            print(f"Removed successfuly, current array: {self.storage}")
        else:
            print(f"Cannot remove because {key} is not found in the array")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # 1.create hash
        hash_key = self._hash_mod(key)
        # 2. Check if it exist
        value = self.storage[hash_key]
        if value:
            print(f"Found {value}")
            return self.bucket.contains(value)

        else:
            print(f"{key} not found in array")

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # copy stuff into new array
        for idx in range(len(self.storage)):
            new_storage[idx] = self.storage[idx]
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
