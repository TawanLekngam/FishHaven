class FishData:
    def __init__(self, id: str, genesis: str, pheromone_threshold: int, crowd_threshold: int, lifespan: int = 60, parent_id: str = None):
        self.__id = id
        self.__parent_id = parent_id
        self.__genesis = genesis
        self.__pheromone = 0
        self.__pheromone_threshold = pheromone_threshold
        self.__crowd_threshold = crowd_threshold
        self.__age = 0
        self.__lifespan = lifespan

    def get_id(self):
        return self.__id

    def get_parent_id(self):
        return self.__parent_id

    def get_genesis(self):
        return self.__genesis

    def get_pheromone(self):
        return self.__pheromone

    def get_pheromone_threshold(self):
        return self.__pheromone_threshold

    def get_crowd_threshold(self):
        return self.__crowd_threshold

    def get_age(self):
        return self.__age

    def get_lifespan(self):
        return self.__lifespan

    def set_pheromone(self, pheromone: float):
        self.__pheromone = pheromone

    def set_age(self, age: int):
        self.__age = age
