class Rent(object):
    
    def __init__(self, __mid, __cid,__titlu, __nume, __status):
        self.__rid = str(__mid) + str(__cid)
        self.__mid = __mid
        self.__cid = __cid
        self.__titlu=__titlu
        self.__nume=__nume
        self.__status = __status

    def get_titlu(self):
        return self.__titlu


    def get_nume(self):
        return self.__nume


    def get_rid(self):
        return self.__rid

    def __str__(self):
        return str(self.__rid)+", "+str(self.__titlu) + ", " + str(self.__nume) + ", status: " + str(self.__status)

    def __eq__(self, value):
        return self.__rid == value.__rid and self.__status==value.__status

    def get_mid(self):
        return self.__mid

    def get_cid(self):
        return self.__cid

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    mid = property(get_mid, None, None, None)
    cid = property(get_cid, None, None, None)
    status = property(get_status, set_status, None, None)
    rid = property(get_rid, None, None, None)
    titlu = property(get_titlu, None, None, None)
    nume = property(get_nume, None, None, None)
        
