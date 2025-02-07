class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

class MyHashMap(object):

    def __init__(self):
        self.hash_key_space = 2069
        self.hash_table = [Bucket() for i in range(self.hash_key_space)]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        k = key % self.hash_key_space
        self.hash_table[k].update(key, value)

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        k = key % self.hash_key_space
        return self.hash_table[k].get(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = key % self.hash_key_space
        self.hash_table[k].remove(key)        


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1,101)
    obj.put(2,202)
    print(obj.get(1))
    print(obj.get(2))
    obj.remove(1)
    print(obj.get(1))
    print(obj.get(2))