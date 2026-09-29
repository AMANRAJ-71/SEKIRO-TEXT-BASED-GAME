import random
import time
from src.player import Player
from src.boss import Boss

def display_status(player: Player, boss: Boss) -> None:
    print("\n" + "=" * 50)
    print(f"👤 {player.name} | HP: {player.hp}/{player.max_hp} | Posture: {player.posture}/{player.max_posture} | Gourds: {player.gourds}")
    print(f"👹 {boss.name} | HP: {boss.hp}/{boss.max_hp} | Posture: {boss.posture}/{boss.max_posture}")
    print("=" * 50)

def battle(boss_name: str, boss_hp: int, boss_posture: int) -> None:
    player = Player("Sekiro")
    boss = Boss(boss_name, boss_hp, boss_posture)

    print(f"\n⚔️ A formidable foe approaches: {boss.name}! ⚔️")
    time.sleep(1)

    while player.is_alive() and boss.is_alive():
        display_status(player, boss)

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Heal (Healing Gourd)")
        
        choice = input("> ").strip()
        
        if choice == "2":
            if player.heal():
                print(f"\n🧪 You drank Healing Gourd! ({player.gourds} left)")
            else:
                print("\n❌ Healing Gourd is empty!")
                continue
        elif choice == "1":
            print(f"\n💥 You slash at {boss.name}!")
            boss_defense = random.choice(["hit", "block", "deflect"])
            
            if boss_defense == "hit":
                boss.take_damage(20)
                boss.add_posture(10)
                print(f"✨ Direct hit! {boss.name} takes damage and posture!")
            elif boss_defense == "block":
                boss.take_damage(5)
                boss.add_posture(15)
                print(f"🛡️ {boss.name} blocks your attack, taking heavy posture damage!")
            else:
                player.add_posture(15)
                print(f"⚡ DEFLECT! {boss.name} deflected your attack!")

        if boss.posture >= boss.max_posture:
            print(f"\n🔴 [DEATHBLOW!] You broke {boss.name}'s posture!")
            print(f"🗡️ You perform a Shinobi Deathblow on {boss.name}!")
            boss.hp = 0
            break

        if boss.is_alive():
            time.sleep(1)
            attack_type = boss.choose_attack()

            if attack_type == "regular":
                print(f"\n⚔️ {boss.name} prepares a standard attack!")
                print("React: (1) Deflect  (2) Dodge")
                reaction = input("> ").strip()

                if reaction == "1":
                    print(f"✨ Clang! You perfectly deflected {boss.name}'s blade!")
                    boss.add_posture(20)
                else:
                    player.take_damage(25)
                    player.add_posture(10)
                    print("💥 You failed to avoid the attack!")

            elif attack_type == "thrust":
                print(f"\n⚠️ [危 PERILOUS ATTACK] {boss.name} winds up a THRUST attack!")
                print("React: (1) Mikiri Counter  (2) Jump Dodge")
                reaction = input("> ").strip()

                if reaction == "1":
                    print(f"🦶 MIKIRI COUNTER! You stomp {boss.name}'s blade!")
                    boss.add_posture(35)
                else:
                    player.take_damage(40)
                    player.add_posture(20)
                    print("💀 The thrust impales you!")

            elif attack_type == "sweep":
                print(f"\n⚠️ [危 PERILOUS ATTACK] {boss.name} prepares a SWEEP attack!")
                print("React: (1) Mikiri Counter  (2) Jump & Kick")
                reaction = input("> ").strip()

                if reaction == "2":
                    print(f"🦘 You jump over the blade and kick {boss.name}!")
                    boss.add_posture(30)
                else:
                    player.take_damage(35)
                    player.add_posture(20)
                    print("🧹 You got swept off your feet!")

        if player.posture > 0:
            player.recover_posture(5)

        if player.posture >= player.max_posture:
            print("\n💥 YOUR POSTURE WAS BROKEN!")
            player.take_damage(20)
            player.posture = 0

    if not player.is_alive():
        print("\n☠️  DEATH - Hesitation is defeat. ☠️")
    elif not boss.is_alive():
        print("\n🌸  SHINOBI EXECUTION 🌸")

if __name__ == "__main__":
    battle("Genichiro Ashina", boss_hp=120, boss_posture=100)
