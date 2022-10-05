class Nodo:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return f"{self.data}"