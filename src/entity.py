class Entity:
    """Base class for combatants with Health and Posture management."""
    
    def __init__(self, name: str, max_hp: int, max_posture: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_posture = max_posture
        self.posture = 0

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def add_posture(self, amount: int) -> None:
        self.posture = min(self.max_posture, self.posture + amount)

    def recover_posture(self, amount: int) -> None:
        self.posture = max(0, self.posture - amount)
