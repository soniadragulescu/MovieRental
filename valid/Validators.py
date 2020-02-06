from errors.Errors import *


class ClientValidator(object):
    
    def __init__(self):
        pass
    
    def valideazaClient(self, client):
        errors = ""
        if client.get_id() < 0:
            errors += "bad id!\n"
        if client.get_nume() == "":
            errors += "bad nume!\n"
        if client.get_cnp() < 0:
            errors += "bad cnp!\n"
        if len(errors) > 0:
            raise ValidError(errors)

    def valideazaIDClient(self, client):
        errors = ""
        if client.get_id() < 0:
            errors += "bad id!\n"
        if len(errors) > 0:
            raise ValidError("")
        

class MovieValidator(object):
    
    def __init__(self):
        pass
    
    def valideazaMovie(self, movie):
        errors = ""
        if movie.get_id() < 0:
            errors += "bad id!\n"
        if movie.get_titlu() == "":
            errors += "bad titlu!\n"
        if movie.get_gen() == '':
            errors += "bad gen!\n"
        if len(errors) > 0:
            raise ValidError(errors)


class RentValidator(object):
    
    def __init__(self):
        pass
    
    def valideazaRent(self, rent):
        pass