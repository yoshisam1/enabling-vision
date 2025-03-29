from enum import Enum
from moves import Move

class CharacterClass(Enum):
    KNIGHT = {
        "health": 100,
        "defense": 15,
        "attack": 7,
        "moves": [
            Move("Boulder Smash", "EARTH", 5, 10, "Lowers Enemy Defense by 2"),
            Move("Inferno Counter", "FIRE", 0, 5, "Deals retaliation damage equal to ⅓ of the last hit taken"),
            Move("Lava Strike", "FIRE", 2, 10, "Raises Attack by 2"),
            Move("Earthen Tremor", "EARTH", 3, 8, "Lowers enemy attack by 2"),
            Move("Magma Punch", "FIRE", 4, 8, "Heals 25% of damage dealt"),
            Move("Rock Breaker", "EARTH", 6, 6, "Bonus damage vs. high defense opponents")
        ]
    }
    WIZARD = {
        "health": 140,
        "defense": 8,
        "attack": 12,
        "moves": [
            Move("Flame Surge", "FIRE", 2, 10, "Raises Attack by 2"),
            Move("Hydro Blast", "WATER", 5, 5, "Damage scales with HP (if HP > 100, add +5)"),
            Move("Ember Wave", "FIRE", 0, 12, "Restores HP equal to 25% of damage dealt"),
            Move("Steam Burst", "WATER", 3, 8, "Lowers enemy attack by 2"),
            Move("Volcanic Surge", "FIRE", 4, 7, "If HP < 50%, roll twice and take the higher number"),
            Move("Tidal Crash", "WATER", 6, 6, "Deals bonus damage based on missing HP (missing HP / 10 = extra damage)")
        ]
    }
    ARCHER = {
        "health": 60,
        "defense": 10,
        "attack": 15,
        "moves": [
            Move("Flame Arrow", "FIRE", 3, 12, "Raises Attack by 1 (Stacks up to +3)"),
            Move("Piercing Shot", "EARTH", 5, 10, "Ignores enemy defense and lowers it by 2"),
            Move("Searing Volley", "FIRE", 0, 8, "Hits twice, raises attack by 2"),
            Move("Rock Barrage", "EARTH", 0, 10, "Hit 2-5 times, lowers enemy Defense by 1 per hit"),
            Move("Explosive Shot", "FIRE", 10, 5, "Deals recoil (user loses ⅓ of damage dealt)"),
            Move("Sharpened Quake", "EARTH", 6, 6, "Deals extra damage if the target's HP is below 50%")
        ]
    }

class Character:
    def __init__(self, player_name: str):
        self.name = player_name
        self.character_class = None
        self.health = 0
        self.max_health = 0
        self.defense = 0
        self.attack = 0
        self.is_alive = True
        self.moves = []
        self.last_damage_taken = 0
        self.last_element_used = None

    def select_character_class(self):
        print("\nChoose your character class:")
        print("1. Knight - Moderate health, high defense, low attack")
        print("2. Wizard - High health, low defense, moderate attack")
        print("3. Archer - Low health, moderate defense, high attack")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice == "1":
                self.character_class = CharacterClass.KNIGHT
            elif choice == "2":
                self.character_class = CharacterClass.WIZARD
            elif choice == "3":
                self.character_class = CharacterClass.ARCHER
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Initialize character stats based on chosen class
            self.health = self.character_class.value["health"]
            self.max_health = self.character_class.value["health"]
            self.defense = self.character_class.value["defense"]
            self.attack = self.character_class.value["attack"]
            self.moves = self.character_class.value["moves"].copy()
            break

    def take_damage(self, damage):
        """Reduce character's health by the specified damage amount"""
        self.health -= damage
        self.last_damage_taken = damage
        self.health -= damage
        self.last_damage_taken = damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def heal(self, amount):
        """Heal the character by the specified amount"""
        if self.is_alive:
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health

    def use_move(self, move_index, target):
        """Use a move on the target"""
        if 0 <= move_index < len(self.moves):
            return self.moves[move_index].use(self, target)
        return False, "Invalid move!"

    def get_available_moves(self):
        """Return a list of moves that still have uses"""
        return [move for move in self.moves if move.current_uses > 0]

    def __str__(self):
        """String representation of the character"""
        moves_str = "\nMoves:"
        for i, move in enumerate(self.moves):
            moves_str += f"\n{i+1}. {move}"
        return f"{self.character_class.name} - Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}{moves_str}" 