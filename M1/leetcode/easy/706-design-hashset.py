# https://leetcode.com/problems/design-hashmap/

# another simple introductory problem for hashmap , OOPs

# dict solution 

class MyHashMap:

    def __init__(self):
        self.hmap = {}

    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value
# simply assigns the corresponding value to the key

    def get(self, key: int) -> int:
        return self.hmap.get(key,-1)
# used get func, if the key is present, we obtain it's value, if not, -1 is returned

    def remove(self, key: int) -> None:
        self.hmap.pop(key,None)
# pops key if key is present, else None 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)