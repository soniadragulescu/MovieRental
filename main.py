from teste.TestMovie import TestMovie
from repo.Repository import Repository
from business.Controllers import MovieService, ClientService, RentService
from valid.Validators import MovieValidator, ClientValidator, RentValidator
from ui.Console import Console
from teste.TestClient import TestClient
from model.Client import Client
from model.Movie import Movie
from model.Rent import Rent
import random
from errors.Errors import RepoError

# def randomString():
#     chars='ABCDEFGHIJKLMNOPQRSTUVXYZ'
#     return ''.join(random.choice(chars) for _ in range(random.randint(3, 10)))

t = TestMovie()
t.runTests()
t2 = TestClient()
t2.runTests()

repoMovies = Repository()
repoClients = Repository()
repoRents = Repository()

# for i in range(10):
#     ok=0
#     while ok==0:
#         try:
#             id=random.randint(9, 99999)
#             nume=randomString()
#             cnp=random.randint(1000, 100000)
#             
#             client=Client(id, nume, cnp)
#             repoClients.add(client)
#             ok=1
#         except RepoError as re:
#             ok=0
    
    

movie1 = Movie(101, 'Ronin', 'action')
movie2 = Movie(1, "TheNun", "horror")
movie3 = Movie(34, "Venom", "fantasy")

client1 = Client(10, "Andrei", 1961210)
client2 = Client(42, "Sonia", 2990703)
client3 = Client(19, "Mara", 20209)
client6 = Client(199, "Maria", 199)
client4 = Client(78, "Mihaela", 99)
client5 = Client(20, "Marian", 123)
 
repoClients.add(client1)
repoClients.add(client2)
repoClients.add(client3)

repoMovies.add(movie1)
repoMovies.add(movie2)
repoMovies.add(movie3)
    
# rent1=Rent(101, 10, 'inchiriat') 
# #repoRents.add(rent1)
# rent2=Rent(101, 42, 'inchiriat')
# rent3=Rent(101, 19, 'inchiriat')
# rent4=Rent(1, 10, 'inchiriat')
# rent5=Rent(34, 42, 'inchiriat')
# rent6=Rent(34, 19, 'inchiriat')
# rent7=Rent(34, 199, 'inchiriat')
# rent8=Rent(34,78 , 'inchiriat')
# rent9=Rent(34, 20, 'inchiriat')
# repoRents.add(rent2)
# repoRents.add(rent3)
# repoRents.add(rent4)
# repoRents.add(rent5)
# repoRents.add(rent6)
# repoRents.add(rent7)
# repoRents.add(rent8)

validatorMovie = MovieValidator()
validatorClient = ClientValidator()
validatorRent = RentValidator()

servMovies = MovieService(repoMovies, validatorMovie)
servClients = ClientService(repoClients, validatorClient)
servRents = RentService(repoMovies, repoClients, repoRents, servMovies, servClients)

cons = Console(servMovies, servClients, servRents)

cons.run()
