

class Flower:
    def __init__(self, name: str, petals: int, annunal: bool):
        self.name = name 
        self.annual = annunal
        self.petals = petals


    def bloom(self) -> str:
        if self.annual:
            return f'the {self.name} blooms with {self.petals} petals every year!'
        else:
            return f'the {self.name} blooms with {self.petals} petals this year!'
