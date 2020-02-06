from model.Rent import Rent
from model.Client import Client
from model.Movie import Movie
from errors.Errors import ValidError,RepoError
from repo.Repository import Repository
from business.Controllers import RentService

class TestClient(object):
    
    
    def __init__(self):
        self.__mid = 32
        self.__cid = 10
        self.__status = "inchiriat"
        self.__rent = Rent(self.__mid,self.__cid,self.__status)
        self.__repo = Repository()
        self.__service = RentService(repoMovies, repoClients, repoRents, servMovies, servClients)

    
    def __testModel(self):
        assert self.__client.get_mid()== self.__mid
        assert self.__client.get_cid()==self.__cid
        assert self.__client.get_status()==self.__status
    
    def __testRepo(self):
        assert len(self.__repo)==0
        self.__repo.add(self.__rent)
        assert len(self.__repo)==1
        try:
            self.__repo.add(self.__rent)
            assert False
        except RepoError as re:    
            assert str(re)=="existing elem!"
        keyClient = Rent(self.__id,None,None)
        assert self.__repo.search(keyClient)==self.__client
        try:
            self.__repo.search(self.__badClient)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        newClient = Client(self.__id,"Marius",299)
        self.__repo.update(newClient)
        all = self.__repo.getAll()
        assert all == [newClient]
        assert self.__repo.search(keyClient) == newClient
        try:
            self.__repo.update(self.__badClient)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        removeElem = Client(self.__id,None,None)
        self.__repo.removeee(removeElem)  
        try:
            self.__repo.removeee(removeElem)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        
    
    def __testBusiness(self):
        assert self.__service.getAllClients()==[]
        self.__service.addClient(self.__id,self.__nume,self.__cnp)
        clients = self.__service.getAllClients()
        assert clients == [self.__client]
        client0 = Client(67,"Mihai",199)
        #movie1 = Client(3,"LOTR","fantasy")
        
        self.__service.addClient(67,"Mihai",199)
#         self.__service.addMovie(34,"AStarIsBorn","romance")
#         self.__service.addMovie(14,"AmericanPie","comedy")
#         self.__service.addMovie(3,"LOTR","fantasy")
        goodClients = self.__service.getClientById(67)
        assert goodClients == client0
        
    def runTests(self):
        self.__testModel()
        self.__testValid()
        self.__testRepo()
        self.__testBusiness()
