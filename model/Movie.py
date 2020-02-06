class Movie(object):
    
    def __init__(self, __id, __titlu, __gen):
        self.__id = __id
        self.__titlu = __titlu
        self.__gen = __gen
        self.__noRents = 0

    def get_no_rents(self):
        return self.__noRents


    def set_no_rents(self):
        self.__noRents +=1

    def __str__(self):
        return str(self.__id) + " " + str(self.__titlu) + " " + str(self.__gen)+" "+str(self.__noRents)

    def __eq__(self, value):
        return self.__id == value.__id

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_gen(self):
        return self.__gen

    def set_titlu(self, value):
        self.__titlu = value

    def set_gen(self, value):
        self.__gen = value

    id = property(get_id, None, None, None)
    titlu = property(get_titlu, set_titlu, None, None)
    gen = property(get_gen, set_gen, None, None)
    noRents = property(get_no_rents, set_no_rents, None, None)
        
