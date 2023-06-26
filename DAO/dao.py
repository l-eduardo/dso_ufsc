import pickle
from exceptions.chave_unica import ChaveUnicaException


class DAO():
    __assunto = {}

    def __init__(self, datasource = "", subjects = []) -> None:
        self.__datasource = datasource
        self.__subjects = subjects
        self.__cache = {}
        self.__pkl_path = "./data/" + self.__datasource + ".pkl"
        self.setup()

    def setup(self):
        try:
            self.inscrever([self.__datasource, *self.__subjects])
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def inscrever(self, subjects):
        for subject in subjects:
            if subject in DAO.__assunto.keys():
                DAO.__assunto[subject].append(self)
            else:
                DAO.__assunto[subject] = [self]
            print(DAO.__assunto[subject])

    def desinscrever(self):
        pass

    def __notificar_update(self, *args):
        for i in DAO.__assunto[self.__datasource]:
            i.__recebe_notificacao(self.update, args)
    
    def __notificar_remove(self, *args):
        for i in DAO.__assunto[self.__datasource]:
            i.__recebe_notificacao(self.remove, args)

    def __recebe_notificacao(self, fn, *args):
        print(args, fn)
        fn(*args)

    def __dump(self):
        pickle.dump(self.__cache, open(self.__pkl_path, "wb"))
    
    def __load(self):
        self.__cache = pickle.load(open(self.__pkl_path, "rb"))
    
    def get(self, key):
        try:
            self.__load()
            return self.__cache[key]
        except KeyError:
            return None
    
    def get_all(self):
        self.__load()
        return self.__cache

    def add(self, key, value):
        if key not in self.__cache.keys():
            self.__cache[key] = value
        else:
            raise ChaveUnicaException()
        self.__dump()
        return value

    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
            self.__notificar_remove(key)
        except KeyError:
            self.__load()
            return []
    
    def update(self, key, value):
        try:
            self.__cache[key] = value
            self.__dump()
            self.__notificar_update(key, value)
            return value
        except Exception as e:
            print(repr(e))
