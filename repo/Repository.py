from errors.Errors import RepoError

class Repository(object):
    
    def __init__(self):
        self.__elems = []
        
    def __len__(self):
        return len(self.__elems)
    
    def add(self, elem):
        if elem in self.__elems:
            raise RepoError("existing elem!")
        self.__elems.append(elem)
    
    def search(self, elem):
        if elem not in self.__elems:
            raise RepoError("inexisting elem!")
        for x in self.__elems:
            if x == elem:
                return x
    
    def update(self, elem):
        if elem not in self.__elems:
            raise RepoError("inexisting elem!")
        for i in range(len(self.__elems)):
            if self.__elems[i] == elem:
                self.__elems[i] = elem
                return
    
    def removeee(self, elem):
        if elem not in self.__elems:
            raise RepoError("inexisting elem!")
        for i in range(len(self.__elems)):
            if self.__elems[i] == elem:
                del self.__elems[i]
                return
    
    def getAll(self):
        return self.__elems[:]

