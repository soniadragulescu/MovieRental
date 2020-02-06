from model.Movie import Movie
from model.Client import Client
from model.Rent import Rent
from errors.Errors import *


class MovieService(object):
    
    def __init__(self, __repoMovie, __validatorMovie):
        self.__repoMovie = __repoMovie
        self.__validatorMovie = __validatorMovie
        
    def addMovie(self, id, titlu, gen):
        m = Movie(id, titlu, gen)
        try:
            self.__validatorMovie.valideazaMovie(m)
        except ValueError as ve:
            print(ve)
            
        try:
            self.__repoMovie.add(m)
        except RepoError as re:
            print (re)
        
    def deleteMovie(self, id):
        movie = self.getMovieById(id)
        self.__repoMovie.removeee(movie)             
    
    def searchMovie(self, id):
        movie = self.getMovieById(id)
        return self.__repoMovie.search(movie)
    
    def updateMovie(self, movie):
        self.__repoMovie.update(movie)            
        
    def getAllMovies(self):
        return self.__repoMovie.getAll()

    def getMovieById(self, movieId):
        m = Movie(movieId, None, None)
        return self.__repoMovie.search(m)


class ClientService(object):
    
    def __init__(self, __repoClient, __validatorClient):
        self.__repoClient = __repoClient
        self.__validatorClient = __validatorClient
        
    def addClient(self, id, nume, cnp):
        c = Client(id, nume, cnp)
        try:
            self.__validatorClient.valideazaClient(c)
        except ValueError as ve:
            print(ve)
            
        try:
            self.__repoClient.add(c)
        except RepoError as re:
            print(re)
        
    def getClientById(self, clientId):
        c = Client(clientId, None, None)
        return self.__repoClient.search(c)
    
    def getClientByName(self, nume):
        l=[]
        clients=self.__repoClient.getAll()
        for client in clients:
            if client.get_nume()==nume:
                l.append(client)
        return l
            
    def deleteClient(self, id):
        client = self.getClientById(id)
        self.__repoClient.removeee(client)
        
    def searchClient(self, nume):
        client = self.getClientByName(nume)
        return self.__repoClient.search(client)      
    
    def searchClient(self, id):
        client = self.getClientById(id)
        return self.__repoClient.search(client)
    
    def updateClient(self, client):
        self.__repoClient.update(client)      
        
    def getAllClients(self):
        return self.__repoClient.getAll()

    
class RentService(object):
    
    def __init__(self, __repoMovie, __repoClient, __repoRent, __servMovie, __servClient):
        self.__repoMovie = __repoMovie
        self.__repoClient = __repoClient
        self.__repoRent = __repoRent
        self.__servMovie = __servMovie
        self.__servClient = __servClient
        
    def addRent(self, movie, client):
        mid = movie.get_id()
        cid = client.get_id()
        t=movie.get_titlu()
        n=client.get_nume()
        r = Rent(mid, cid, t, n, 'inchiriat')
        
        try:
            self.__repoRent.add(r)
            movie.set_no_rents()
            client.set_no_rents()
        except RepoError as re:
            print("Deja inchiriat!")
            
    def unRent(self, movie, client):
        mid = movie.get_id()
        cid = client.get_id()
        t=movie.get_titlu()
        n=client.get_nume()
        r = Rent(mid, cid, t, n, 'inchiriat')
        
        try:
            r2 = self.__repoRent.search(r)
            r2.set_status("returnat")
        except RepoError as re:
            print("Nu exista inchirierea!")
        
    def getAllRents(self):
        return self.__repoRent.getAll()

    def sortRentName(self):
        rents = self.getAllRents()
        rez = []
        for rent in rents:
            if rent.get_status() == 'inchiriat':
                client = self.__servClient.getClientById(rent.get_cid())
                nume = client.get_nume()
                if nume in rez:
                    pass
                else:
                    rez.append(nume)
        return sorted(rez)
    
    def sortRentNo(self):
        rents = self.getAllRents()
        rez = {}
        for rent in rents:
            client = self.__servClient.getClientById(rent.get_cid())
            nume = client.get_nume()
            if nume in rez:
                rez[nume] += 1
            else:
                rez[nume] = 1
        return sorted(rez.items(), key=lambda x:x[1], reverse=True)
    
    def topRents(self):
        rents = self.getAllRents()
        rez = {}
        for rent in rents:
            movie = self.__servMovie.getMovieById(rent.get_mid())
            titlu = movie.get_titlu()
            if titlu in rez:
                rez[titlu] += 1
            else:
                rez[titlu] = 1
        return sorted(rez.items(), key=lambda x:x[1], reverse=True)
    
    def top30(self):
        rents = self.getAllRents()
        rez = {}
        for rent in rents:
            client = self.__servClient.getClientById(rent.get_cid())
            nume = client.get_nume()
            if nume in rez:
                rez[nume] += 1
            else:
                rez[nume] = 1
        n=int(len(rez)/3)
        return sorted(rez.items(), key=lambda x:x[1], reverse=True)[:n]
        
