# https://leetcode.com/problems/design-hashset/

# this is a simple problem, more like an introductory exercise for OOPs
# set solution

class MyHashSet:

    def __init__(self):
        self.data = set()
# using set to hold the data
    def add(self, key: int) -> None:
        self.data.add(key)
# simple add func
    def remove(self, key: int) -> None:
        self.data.discard(key)
# using discard(key) does not throw error even if key is not present in set, unlike remove(key)
    def contains(self, key: int) -> bool:
        return key in self.data
# returns True if key is present, else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
