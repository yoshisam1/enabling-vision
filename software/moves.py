from enum import Enum
import random

class Move:
    class MoveType(Enum):
        FIRE = "Fire"
        EARTH = "Earth"
        WATER = "Water"
    
    @staticmethod
    def get_move_type(type_str):
        """Convert string to MoveType enum"""
        type_map = {
            "FIRE": Move.MoveType.FIRE,
            "EARTH": Move.MoveType.EARTH,
            "WATER": Move.MoveType.WATER
        }
        return type_map.get(type_str.upper())
    
    def __init__(self, name, move_type, power, max_uses, effect_description):
        self.name = name
        # Accept either string or MoveType enum
        self.move_type = move_type if isinstance(move_type, Move.MoveType) else Move.get_move_type(move_type)
        self.power = power
        self.max_uses = max_uses
        self.current_uses = max_uses
        self.effect_description = effect_description

    def calculate_damage(self, attacker, defender, ignore_defense=False):
        """Calculate damage using the formula: D = ((d20 + B)/2) × (A/d) + 2
        where:
        D = Damage dealt
        d20 = Random roll (1-20)
        B = Move-specific bonus (self.power)
        A = Attacker's Attack Stat
        d = Defender's Defense stat"""
        d20 = random.randint(1, 20)
        base = (d20 + self.power) / 2
        
        if ignore_defense:
            defense_factor = 1
        else:
            # Prevent division by zero by ensuring minimum defense of 1
            defense = max(1, defender.defense)
            defense_factor = attacker.attack / defense
            
        damage = int(base * defense_factor + 2)
        return max(2, damage)  # Ensure minimum damage of 2

    def use(self, user, target):
        if self.current_uses <= 0:
            return False, f"{self.name} has no uses left!"
        
        self.current_uses -= 1
        
        # Apply move-specific effects
        if self.name == "Boulder Smash":
            damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            target.defense = max(0, target.defense - 2)
            return True, f"{user.name} used Boulder Smash! Lowered {target.name}'s defense by 2! Dealt {damage} damage!"
            
        elif self.name == "Inferno Counter":
            bonus_power = self.power + (user.last_damage_taken // 3)
            self.power = bonus_power  # Temporarily modify power for damage calculation
            damage = self.calculate_damage(user, target)
            self.power = 0  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Inferno Counter! Dealt {damage} damage!"
            
        elif self.name == "Lava Strike":
            damage = self.calculate_damage(user, target)
            user.attack += 2
            target.take_damage(damage)
            return True, f"{user.name} used Lava Strike! Attack raised by 2! Dealt {damage} damage!"
            
        elif self.name == "Earthen Tremor":
            damage = self.calculate_damage(user, target)
            target.attack = max(0, target.attack - 2)
            target.take_damage(damage)
            return True, f"{user.name} used Earthen Tremor! Lowered {target.name}'s attack by 2! Dealt {damage} damage!"
            
        elif self.name == "Magma Punch":
            damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            heal_amount = damage // 4
            user.heal(heal_amount)
            return True, f"{user.name} used Magma Punch! Dealt {damage} damage and healed {heal_amount}!"
            
        elif self.name == "Rock Breaker":
            if target.defense > 10:
                self.power += 5  # Temporarily increase power
            damage = self.calculate_damage(user, target)
            if target.defense > 10:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Rock Breaker! Dealt {damage} damage!"

        # Wizard moves
        elif self.name == "Flame Surge":
            damage = self.calculate_damage(user, target)
            user.attack += 2
            target.take_damage(damage)
            return True, f"{user.name} used Flame Surge! Attack raised by 2! Dealt {damage} damage!"
            
        elif self.name == "Hydro Blast":
            if user.health > 100:
                self.power += 5  # Temporarily increase power
            damage = self.calculate_damage(user, target)
            if user.health > 100:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Hydro Blast! Dealt {damage} damage!"
            
        elif self.name == "Ember Wave":
            damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            heal_amount = damage // 4
            user.heal(heal_amount)
            return True, f"{user.name} used Ember Wave! Dealt {damage} damage and healed {heal_amount}!"
            
        elif self.name == "Steam Burst":
            damage = self.calculate_damage(user, target)
            target.attack = max(0, target.attack - 2)
            target.take_damage(damage)
            return True, f"{user.name} used Steam Burst! Lowered {target.name}'s attack by 2! Dealt {damage} damage!"
            
        elif self.name == "Volcanic Surge":
            if user.health < user.max_health // 2:
                # Roll twice and take the higher number
                damage1 = self.calculate_damage(user, target)
                damage2 = self.calculate_damage(user, target)
                damage = max(damage1, damage2)
            else:
                damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            return True, f"{user.name} used Volcanic Surge! Dealt {damage} damage!"
            
        elif self.name == "Tidal Crash":
            missing_hp = user.max_health - user.health
            self.power += missing_hp // 10  # Add bonus damage based on missing HP
            damage = self.calculate_damage(user, target)
            self.power -= missing_hp // 10  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Tidal Crash! Dealt {damage} damage!"

        # Archer moves
        elif self.name == "Flame Arrow":
            damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            user.attack = min(user.attack + 1, user.attack + 3)  # Stack up to +3
            return True, f"{user.name} used Flame Arrow! Attack raised by 1! Dealt {damage} damage!"
            
        elif self.name == "Piercing Shot":
            damage = self.calculate_damage(user, target, ignore_defense=True)  # Ignores defense
            target.take_damage(damage)
            target.defense = max(0, target.defense - 2)
            return True, f"{user.name} used Piercing Shot! Lowered {target.name}'s defense by 2! Dealt {damage} damage!"
            
        elif self.name == "Searing Volley":
            # Hit twice with half damage each time
            damage1 = self.calculate_damage(user, target) // 2
            damage2 = self.calculate_damage(user, target) // 2
            total_damage = damage1 + damage2
            target.take_damage(total_damage)
            user.attack += 2
            return True, f"{user.name} used Searing Volley! Attack raised by 2! Dealt {total_damage} damage!"
            
        elif self.name == "Rock Barrage":
            hits = random.randint(2, 5)
            total_damage = 0
            for _ in range(hits):
                damage = self.calculate_damage(user, target) // 2  # Half damage per hit
                total_damage += damage
            target.take_damage(total_damage)
            target.defense = max(0, target.defense - hits)  # Lower defense by 1 per hit
            return True, f"{user.name} used Rock Barrage! Hit {hits} times! Lowered {target.name}'s defense by {hits}! Dealt {total_damage} damage!"
            
        elif self.name == "Explosive Shot":
            damage = self.calculate_damage(user, target)
            target.take_damage(damage)
            recoil = damage // 3
            user.take_damage(recoil)
            return True, f"{user.name} used Explosive Shot! Dealt {damage} damage and took {recoil} recoil damage!"
            
        elif self.name == "Sharpened Quake":
            if target.health < target.max_health // 2:
                self.power += 5  # Add bonus damage against low HP targets
            damage = self.calculate_damage(user, target)
            if target.health < target.max_health // 2:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Sharpened Quake! Dealt {damage} damage!"
            
        return False, "Move failed!"

    def __str__(self):
        return f"{self.name} ({self.move_type.value}) - Power: d20 + {self.power}, Uses: {self.current_uses}/{self.max_uses}" 