class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.usage = []
        self.cache = {}
        
    def get(self, key):
        if key in self.cache:
            self.usage.remove(key) # Update usage
            self.usage.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.usage.remove(key)  # Update usage
            self.usage.append(key)
            print(f"Value of {key} updated. ")
            return
        
        if len(self.cache) == self.capacity:
            lru_key = self.usage.pop(0)  # Get and remove LRU from usage list
            del self.cache[lru_key]      # Remove LRU from cache
            print(f"Evicting key: {lru_key}") # Added for illustrative purposes
            
        self.cache[key] = value
        self.usage.append(key)          #Add the new key as most recently used
        print("Cache: ", self.cache)


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)
    print(cache.get("B"))  # Output: 2
    cache.put("D", 4)
    print(cache.get("A"))  # Output: -1
