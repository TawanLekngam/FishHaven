class FishModel:
    def __init__(self, id: str, genesis: str, parentId: str = None):
        self.id = id
        self.genesis = genesis
        self.parentId = parentId
