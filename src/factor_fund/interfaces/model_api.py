from typing import Protocol

class ModelAPI(Protocol):
    def predict(self, X):...
