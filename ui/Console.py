from errors.Errors import *
from model.Client import *
from model.Movie import *


class Console(object):
    
    def __init__(self, __servMovie, __servClient, __servRent):
        self.__servMovie = __servMovie
        self.__servClient = __servClient
        self.__servRent = __servRent
    
    def __uiAddMovie(self, params):
        if len(params) != 3:
            print("nr params invalid!")
            return

        id = int(params[0])
        titlu = params[1]
        gen = params[2]
        self.__servMovie.addMovie(id, titlu, gen)
    
    def __uiDeleteMovie(self, params):
        if len(params) != 1:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        self.__servMovie.deleteMovie(id)
        
    def __uiSearchMovie(self, params):
        if len(params) != 1:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        movie = self.__servMovie.searchMovie(id)
        print(movie)
    
    def __uiPrintMovies(self, params):
        if len(params) != 0:
            print("nr invalid de params!")
            return
        l = self.__servMovie.getAllMovies()
        if len(l) == 0:
            print("Nu exista niciun film in lista!")
        else:
            for x in l:
                print(x)
            
    def __uiUpdateMovie(self, params):
        if len(params) != 3:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        titlu = params[1]
        gen = params[2]
        movie = Movie(id, titlu, gen)
        self.__servMovie.updateMovie(movie)
            
    def __uiAddClient(self, params):
        if len(params) != 3:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        nume = params[1]
        cnp = int(params[2])
        self.__servClient.addClient(id, nume, cnp)
    
    def __uiDeleteClient(self, params):
        if len(params) != 1:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        self.__servClient.deleteClient(id)
        
    def __uiSearchClient(self, params):
        if len(params) != 1:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        client = self.__servClient.searchClient(id)
        print(client)
        
    def __uiSearchClientByName(self, params):
        if len(params) != 1:
            print("nr params invalid!")
            return
        
        nume =params[0]
        clients = self.__servClient.getClientByName(nume)
        if len(clients)!=0:
            for x in clients:
                print (x)
        else:
            print("Nu exista clienti cu numele respectiv!")
            
    def __uiPrintClients(self, params):
        if len(params) != 0:
            print("nr invalid de params!")
            return
        l = self.__servClient.getAllClients()
        if len(l) == 0:
            print ("Nu exista niciun client!")
        else:
            for x in l:
                print(x)
    
    def __uiUpdateClient(self, params):
        if len(params) != 3:
            print("nr params invalid!")
            return
        
        id = int(params[0])
        nume = params[1]
        cnp = params[2]
        client = Client(id, nume, cnp)
        self.__servClient.updateClient(client)
        
    def __uiAddRent(self, params):
        if len(params)!=2:
            print("nr params invalid!")
            return
        
        mid=int(params[0])
        cid=int(params[1])
        movie=self.__servMovie.getMovieById(mid)
        client=self.__servClient.getClientById(cid)
        self.__servRent.addRent(movie, client)
        l = self.__servRent.getAllRents()
        if len(l) == 0:
            print ("Nu exista nicio inchiriere!")
        else:
            for x in l:
                print(x)
                
    def __uiReturn(self, params):
        if len(params)!=2:
            print("nr params invalid!")
            return
        
        mid=int(params[0])
        cid=int(params[1])
        movie=self.__servMovie.getMovieById(mid)
        client=self.__servClient.getClientById(cid)
        self.__servRent.unRent(movie, client)
        l = self.__servRent.getAllRents()
        if len(l) == 0:
            print ("Nu exista nicio inchiriere!")
        else:
            for x in l:
                print(x)
                
    def __uiRaport1(self, params):
        if len(params)!=0:
            print("nr params invalid!")
            return
        
        l=self.__servRent.sortRentName()
        if len(l) == 0:
            print ("Nu exista clienti cu inchirieri!")
        else:
            for x in l:
                print(x)
                
    def __uiRaport2(self,params):
        if len(params)!=0:
            print("nr params invalid!")
            return
        
        l=self.__servRent.sortRentNo()
        if len(l) == 0:
            print ("Nu exista clienti cu inchirieri!")
        else:
            for x in l:
                print(x)
                
    def __uiRaport3(self, params):
        if len(params)!=0:
            print("nr params invalid!")
            return
        
        l=self.__servRent.top30()
        if len(l) == 0:
            print ("Nu exista clienti cu inchirieri!")
        else:
            for x in l:
                print(x)
                
    def __uiRaport4(self, params):
        clients = self.__servClient.getAllClients()
        movies = self.__servMovie.getAllMovies()
        rents = self.__servRent.getAllRents()
        print(len(clients), "clienti")
        print(len(movies), "filme")
        print(len(rents), "inchirieri")
        filmeinchiriate=[]
        for rent in rents:
            filmeinchiriate.append(rent.get_titlu())
        for movie in movies:
            titlu=movie.get_titlu()
            if titlu not in filmeinchiriate:
                print(movie)
                
            

    def run(self):
        
        meniu1 = "\n1.Adauga film\n2.Sterge film\n3.Lista filme\n4.Cauta film\n5.Modifica film"
        meniu2 = "\n6.Adauga client\n7.Sterge client\n8.Lista clienti\n9.Cauta client\n10.Modifica client"
        meniu3 = "\n11.Inchiriaza\n12.Returneaza"
        meniu4 = "\nRapoarte clienti cu filme inchiriate ordonate:\n13.dupa nume\n14.dupa nr de filme inchiriate "
        meniu5 = "\n15.Cele mai inchiriate filme\n16.Raport final\nExit"
        comenzi = {"1":self.__uiAddMovie,
                   "2":self.__uiDeleteMovie,
                   "3":self.__uiPrintMovies,
                   "4":self.__uiSearchMovie,
                   "5":self.__uiUpdateMovie,
                   "6":self.__uiAddClient,
                   "7":self.__uiDeleteClient,
                   "8":self.__uiPrintClients,
                   "9":self.__uiSearchClientByName,
                   "10":self.__uiUpdateClient,
                   "11":self.__uiAddRent,
                   "12":self.__uiReturn,
                   "13":self.__uiRaport1,
                   "14":self.__uiRaport2,
                   "15":self.__uiRaport3,
                   "16":self.__uiRaport4} 
        
        while True:
            print (meniu1)
            print (meniu2)
            print(meniu3)
            print(meniu4)
            print(meniu5)
            
            cmd = input("comanda: ")
            params = cmd.split(" ")
            if cmd == "exit":
                return 
            if params[0] in comenzi:
                try:
                    comenzi[params[0]](params[1:])
                except ValueError as ve:
                    print("ID-ul trebuie sa fie numar natural!")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            else:
                print("Comanda invalida!")

