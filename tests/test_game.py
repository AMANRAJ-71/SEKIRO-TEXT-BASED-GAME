import unittest
from src.entity import Entity
from src.player import Player
from src.boss import Boss

class TestSekiroGame(unittest.TestCase):

    def test_entity_health_and_posture(self):
        e = Entity("Test Dummy", max_hp=100, max_posture=50)
        e.take_damage(30)
        self.assertEqual(e.hp, 70)
        
        e.add_posture(40)
        self.assertEqual(e.posture, 40)
        
        e.add_posture(20)
        self.assertEqual(e.posture, 50)  # Capped at max_posture

    def test_player_healing(self):
        player = Player("Wolf")
        player.take_damage(50)
        self.assertTrue(player.heal())
        self.assertEqual(player.hp, 95)
        self.assertEqual(player.gourds, 2)

    def test_boss_attack_types(self):
        boss = Boss("Genichiro", 100, 100)
        valid_attacks = {"regular", "thrust", "sweep"}
        for _ in range(50):
            attack = boss.choose_attack()
            self.assertIn(attack, valid_attacks)

if __name__ == "__main__":
    unittest.main()
