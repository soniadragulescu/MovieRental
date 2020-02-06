from model.Client import Client
from valid.Validators import ClientValidator
from errors.Errors import ValidError,RepoError
from repo.Repository import Repository
from business.Controllers import ClientService

class TestClient(object):
    
    
    def __init__(self):
        self.__id = 32
        self.__nume = "Alex"
        self.__cnp = 345
        self.__client = Client(self.__id,self.__nume,self.__cnp)
        self.__validator = ClientValidator()
        self.__badId = -23
        self.__badNume = ""
        self.__badCnp = -345
        self.__badClient = Client(self.__badId,self.__badNume,self.__badCnp)
        self.__repo = Repository()
        self.__service = ClientService(self.__repo,self.__validator)
    
    def __testModel(self):
        assert self.__client.get_id()== self.__id
        assert self.__client.get_nume()==self.__nume
        assert self.__client.get_cnp()==self.__cnp
    
    
    def __testValid(self):
        try:
            self.__validator.valideazaClient(self.__client)
            assert True
        except ValidError:
            assert False
        
        try:
            self.__validator.valideazaClient(self.__badClient)
            assert False
        except ValidError as ve:
            assert str(ve)=="bad id!\nbad nume!\nbad cnp!\n"

    
    def __testRepo(self):
        assert len(self.__repo)==0
        self.__repo.add(self.__client)
        assert len(self.__repo)==1
        try:
            self.__repo.add(self.__client)
            assert False
        except RepoError as re:    
            assert str(re)=="existing elem!"
        keyClient = Client(self.__id,None,None)
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
