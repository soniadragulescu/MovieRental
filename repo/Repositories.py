class RepoError(Exception):
    pass

class RepoMovie(object):
    
    
    def __init__(self):
        self.__movies = []
    
    def searchById(self,idActor):
        for movie in self.__movies:
            if movie==idMovie:
                return movie
        raise RepoError("inexisting movie!")
    
    
    def store_movie(self,movie):
        if movie in self.__movie:
                raise RepoError("existing actor!")
        self.__actors.append(actor)

    def get_all(self):
        return self.__actors[:]
    
class RepoMovie(object):
    
    
    def __init__(self):
        self.__movies = []
    
    
    def store_movie(self,movie):
        if movie in self.__movies:
            raise RepoError("existing movie!")
        self.__movies.append(movie)

    def searchById(self,idMovie):
        for movie in self.__movies:
            if movie.get_ident()==idMovie:
                return movie
        raise RepoError("inexisting movie!")


    def get_all(self):
        return self.__movies[:]
        


class RepoCast(object):
    
    
    def __init__(self):
        self.__casts = []
    
    def store_cast(self,cast):
        if cast in self.__casts:
            raise RepoError("existing cast!")
        self.__casts.append(cast)


    def get_all(self):
        return self.__casts[:]

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

