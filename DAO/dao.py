import pickle


class DAO():
    def __init__(self, datasource = "") -> None:
        self.__datasource = datasource
        self.__cache = {}
        self.__pkl_path = "./data/" + self.__datasource + ".pkl"
        self.setup()

    def setup(self):
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

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
        self.__cache[key] = value
        self.__dump()
        return value

    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
        except KeyError:
            self.__load()
            return []
    
    def update(self, key, value):
        self.__cache[key] = value
        self.__dump()
        return value