import random
from src.entity import Entity

class Boss(Entity):
    """Boss entity featuring randomized attack selection."""
    
    def __init__(self, name: str, max_hp: int, max_posture: int):
        super().__init__(name, max_hp, max_posture)

    def choose_attack(self) -> str:
        """Returns one of three attack patterns: regular, thrust, or sweep."""
        roll = random.random()
        if roll < 0.6:
            return "regular"
        elif roll < 0.8:
            return "thrust"
        else:
            return "sweep"
