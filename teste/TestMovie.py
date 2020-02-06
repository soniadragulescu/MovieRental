from model.Movie import Movie
from valid.Validators import MovieValidator
from errors.Errors import ValidError,RepoError
from repo.Repository import Repository
from business.Controllers import MovieService

class TestMovie(object):
    
    
    def __init__(self):
        self.__id = 23
        self.__titlu = "Ronin"
        self.__gen = "action"
        self.__movie = Movie(self.__id,self.__titlu,self.__gen)
        self.__validator = MovieValidator()
        self.__badId = -23
        self.__badTitlu = ""
        self.__badGen = ""
        self.__badMovie = Movie(self.__badId,self.__badTitlu,self.__badGen)
        self.__repo = Repository()
        self.__service = MovieService(self.__repo,self.__validator)
    
    def __testModel(self):
        assert self.__movie.get_id()== self.__id
        assert self.__movie.get_titlu()==self.__titlu
        assert self.__movie.get_gen()==self.__gen
    
    
    def __testValid(self):
        try:
            self.__validator.valideazaMovie(self.__movie)
            assert True
        except ValidError:
            assert False
        
        try:
            self.__validator.valideazaMovie(self.__badMovie)
            assert False
        except ValidError as ve:
            assert str(ve)=="bad id!\nbad titlu!\nbad gen!\n"

    
    def __testRepo(self):
        assert len(self.__repo)==0
        self.__repo.add(self.__movie)
        assert len(self.__repo)==1
        try:
            self.__repo.add(self.__movie)
            assert False
        except RepoError as re:    
            assert str(re)=="existing elem!"
        keyMovie = Movie(self.__id,None,None)
        assert self.__repo.search(keyMovie)==self.__movie
        try:
            self.__repo.search(self.__badMovie)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        newMovie = Movie(self.__id,"TheNun","horror")
        self.__repo.update(newMovie)
        all = self.__repo.getAll()
        assert all == [newMovie]
        assert self.__repo.search(keyMovie) == newMovie
        try:
            self.__repo.update(self.__badMovie)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        removeElem = Movie(self.__id,None,None)
        self.__repo.removeee(removeElem)  
        try:
            self.__repo.removeee(removeElem)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        
    
    def __testBusiness(self):
        assert self.__service.getAllMovies()==[]
        self.__service.addMovie(self.__id,self.__titlu,self.__gen)
        movies = self.__service.getAllMovies()
        assert movies == [self.__movie]
        movie0 = Movie(67,"Red","action")
        #movie1 = Movie(3,"LOTR","fantasy")
        
        self.__service.addMovie(67,"Red","action")
#         self.__service.addMovie(34,"AStarIsBorn","romance")
#         self.__service.addMovie(14,"AmericanPie","comedy")
#         self.__service.addMovie(3,"LOTR","fantasy")
        goodMovies = self.__service.getMovieById(67)
        assert goodMovies == movie0
        
    def runTests(self):
        self.__testModel()
        self.__testValid()
        self.__testRepo()
        self.__testBusiness()
