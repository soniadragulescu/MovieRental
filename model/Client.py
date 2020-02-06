class Client(object):
    
    def __init__(self, __id, __nume, __cnp):
        self.__id = __id
        self.__nume = __nume
        self.__cnp = __cnp
        self.__noRents=0

    def __str__(self):
        return str(self.__id) + " " + str(self.__nume) + " " + str(self.__cnp)+" "+str(self.__noRents)


    def __eq__(self, value):
        return self.__id == value.__id

    def set_no_rents(self):
        self.__noRents +=1

    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp


    def set_nume(self, value):
        self.__nume = value

    id = property(get_id, None, None, None)
    nume = property(get_nume, set_nume, None, None)
    cnp = property(get_cnp, None, None, None)
