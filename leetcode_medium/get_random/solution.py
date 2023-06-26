# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:

    def __init__(self):
        self.dict = dict()
        self.list = list()
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            print('After adding')
            print(self.list)
            print(self.dict)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.dict[self.list[index]] = index
            self.list.pop()
            del self.dict[val]
            print('after removal')
            print(self.list)
            print(self.dict)    
            return True
        else:
            return False

    def getRandom(self) -> int:
        print(self.list)
        print(self.dict)
        return self.list[int(random.random() * len(self.list))]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]

obj = RandomizedSet()
param_1 = obj.insert(0)
print(param_1)
param_2 = obj.insert(1)
print(param_2)
param_3 = obj.remove(0)
print(param_3)
param_4 = obj.insert(2)
print(param_4)
param_4 = obj.remove(1)
print(param_4)
param_5 = obj.getRandom()
print(param_5)