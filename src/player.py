from src.entity import Entity

class Player(Entity):
    """Player representation extending Entity with healing mechanics."""
    
    def __init__(self, name: str = "Wolf"):
        super().__init__(name, max_hp=100, max_posture=100)
        self.gourds = 3

    def heal(() -> bool:
        if self.gourds > 0:
            self.gourds -= 1
            heal_amount = 45
            self.hp = min(self.max_hp, self.hp + heal_amount)
            return True
        return False
