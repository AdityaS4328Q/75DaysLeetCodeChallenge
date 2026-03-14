class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        store={}
        for i in s:
            store[i]=store.get(i,0)+1
        for i in t:
            store[i]=store.get(i,0)-1

        for val in store.values():
            if val !=0:
                return False
            
        return True