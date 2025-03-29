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
    
    @staticmethod
    def is_super_effective(attacker_element, defender_last_element):
        """Check if the attack is super effective based on elemental advantages"""
        if defender_last_element is None:
            return False
            
        effectiveness = {
            Move.MoveType.FIRE: Move.MoveType.EARTH,   # Fire > Earth
            Move.MoveType.EARTH: Move.MoveType.WATER,  # Earth > Water
            Move.MoveType.WATER: Move.MoveType.FIRE    # Water > Fire
        }
        
        return effectiveness.get(attacker_element) == defender_last_element

    def __init__(self, name, move_type, power, max_uses, effect_description):
        self.name = name
        # Accept either string or MoveType enum
        self.move_type = move_type if isinstance(move_type, Move.MoveType) else Move.get_move_type(move_type)
        self.power = power
        self.max_uses = max_uses
        self.current_uses = max_uses
        self.effect_description = effect_description

    def calculate_damage(self, attacker, defender, ignore_defense=False):
        """Calculate damage using the formula: D = ((d20 + B)/2) × (A/d)
        where:
        D = Damage dealt
        d20 = Random roll (1-20)
        B = Move-specific bonus (self.power)
        A = Attacker's Attack Stat
        d = Defender's Defense stat"""
        d20 = random.randint(1, 20)
        base = (d20 + self.power) / 2
        
        # Check for elemental effectiveness
        effectiveness_multiplier = 1.5 if Move.is_super_effective(self.move_type, defender.last_element_used) else 1.0
        effectiveness_text = " (Super Effective!)" if effectiveness_multiplier > 1 else ""
        
        if ignore_defense:
            defense_factor = 1
            formula = f"(({d20} + {self.power})/2) × 1 × {effectiveness_multiplier}"  # Ignoring defense
        else:
            # Prevent division by zero by ensuring minimum defense of 1
            defense = max(1, defender.defense)
            defense_factor = attacker.attack / defense
            formula = f"(({d20} + {self.power})/2) × ({attacker.attack}/{defense}) × {effectiveness_multiplier}"
            
        damage = int(base * defense_factor * effectiveness_multiplier)
        damage = max(1, damage)  # Ensure minimum damage of 1
        return damage, d20, formula + effectiveness_text  # Return damage, roll, and formula

    def use(self, user, target):
        if self.current_uses <= 0:
            return False, f"{self.name} has no uses left!"
        
        self.current_uses -= 1
        
        # Store the element type used for future effectiveness calculations
        user.last_element_used = self.move_type
        
        # Apply move-specific effects
        if self.name == "Boulder Smash":
            damage, roll, formula = self.calculate_damage(user, target)
            target.take_damage(damage)
            target.defense = max(0, target.defense - 2)
            return True, f"{user.name} used Boulder Smash! (Rolled {roll}) Lowered {target.name}'s defense by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Inferno Counter":
            bonus_power = self.power + (user.last_damage_taken // 3)
            self.power = bonus_power  # Temporarily modify power for damage calculation
            damage, roll, formula = self.calculate_damage(user, target)
            self.power = 0  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Inferno Counter! (Rolled {roll}) Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Lava Strike":
            damage, roll, formula = self.calculate_damage(user, target)
            user.attack += 2
            target.take_damage(damage)
            return True, f"{user.name} used Lava Strike! (Rolled {roll}) Attack raised by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Earthen Tremor":
            damage, roll, formula = self.calculate_damage(user, target)
            target.attack = max(0, target.attack - 2)
            target.take_damage(damage)
            return True, f"{user.name} used Earthen Tremor! (Rolled {roll}) Lowered {target.name}'s attack by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Magma Punch":
            damage, roll, formula = self.calculate_damage(user, target)
            target.take_damage(damage)
            heal_amount = damage // 4
            user.heal(heal_amount)
            return True, f"{user.name} used Magma Punch! (Rolled {roll}) Damage calculation: {formula} = {damage}! Healed {heal_amount}!"
            
        elif self.name == "Rock Breaker":
            if target.defense > 10:
                self.power += 5  # Temporarily increase power
            damage, roll, formula = self.calculate_damage(user, target)
            if target.defense > 10:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Rock Breaker! (Rolled {roll}) Damage calculation: {formula} = {damage}!"

        # Wizard moves
        elif self.name == "Flame Surge":
            damage, roll, formula = self.calculate_damage(user, target)
            user.attack += 2
            target.take_damage(damage)
            return True, f"{user.name} used Flame Surge! (Rolled {roll}) Attack raised by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Hydro Blast":
            if user.health > 100:
                self.power += 5  # Temporarily increase power
            damage, roll, formula = self.calculate_damage(user, target)
            if user.health > 100:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Hydro Blast! (Rolled {roll}) Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Ember Wave":
            damage, roll, formula = self.calculate_damage(user, target)
            target.take_damage(damage)
            heal_amount = damage // 4
            user.heal(heal_amount)
            return True, f"{user.name} used Ember Wave! (Rolled {roll}) Damage calculation: {formula} = {damage}! Healed {heal_amount}!"
            
        elif self.name == "Steam Burst":
            damage, roll, formula = self.calculate_damage(user, target)
            target.attack = max(0, target.attack - 2)
            target.take_damage(damage)
            return True, f"{user.name} used Steam Burst! (Rolled {roll}) Lowered {target.name}'s attack by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Volcanic Surge":
            if user.health < user.max_health // 2:
                # Roll twice and take the higher number
                damage1, roll1, formula1 = self.calculate_damage(user, target)
                damage2, roll2, formula2 = self.calculate_damage(user, target)
                if damage1 > damage2:
                    damage, roll, formula = damage1, roll1, formula1
                else:
                    damage, roll, formula = damage2, roll2, formula2
                return True, f"{user.name} used Volcanic Surge! (Rolled {roll1} and {roll2}, took higher) Damage calculation: {formula} = {damage}!"
            else:
                damage, roll, formula = self.calculate_damage(user, target)
                target.take_damage(damage)
                return True, f"{user.name} used Volcanic Surge! (Rolled {roll}) Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Tidal Crash":
            missing_hp = user.max_health - user.health
            self.power += missing_hp // 10  # Add bonus damage based on missing HP
            damage, roll, formula = self.calculate_damage(user, target)
            self.power -= missing_hp // 10  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Tidal Crash! (Rolled {roll}) Damage calculation: {formula} = {damage}!"

        # Archer moves
        elif self.name == "Flame Arrow":
            damage, roll, formula = self.calculate_damage(user, target)
            target.take_damage(damage)
            user.attack = min(user.attack + 1, user.attack + 3)  # Stack up to +3
            return True, f"{user.name} used Flame Arrow! (Rolled {roll}) Attack raised by 1! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Piercing Shot":
            damage, roll, formula = self.calculate_damage(user, target, ignore_defense=True)  # Ignores defense
            target.take_damage(damage)
            target.defense = max(0, target.defense - 2)
            return True, f"{user.name} used Piercing Shot! (Rolled {roll}) Lowered {target.name}'s defense by 2! Damage calculation: {formula} = {damage}!"
            
        elif self.name == "Searing Volley":
            # Hit twice with half damage each time
            damage1, roll1, formula1 = self.calculate_damage(user, target)
            damage2, roll2, formula2 = self.calculate_damage(user, target)
            damage1 = damage1 // 2
            damage2 = damage2 // 2
            total_damage = damage1 + damage2
            target.take_damage(total_damage)
            user.attack += 2
            return True, f"{user.name} used Searing Volley! (Rolled {roll1} and {roll2}) Attack raised by 2! Damage calculations: {formula1} = {damage1*2}, {formula2} = {damage2*2}, Total = {total_damage}!"
            
        elif self.name == "Rock Barrage":
            hits = random.randint(2, 5)
            total_damage = 0
            rolls = []
            formulas = []
            damages = []
            for _ in range(hits):
                damage, roll, formula = self.calculate_damage(user, target)
                damage = damage // 2  # Half damage per hit
                total_damage += damage
                rolls.append(roll)
                formulas.append(formula)
                damages.append(damage)
            target.take_damage(total_damage)
            target.defense = max(0, target.defense - hits)  # Lower defense by 1 per hit
            damage_calcs = [f"Hit {i+1}: {formulas[i]} = {damages[i]}" for i in range(hits)]
            return True, f"{user.name} used Rock Barrage! (Rolled {', '.join(map(str, rolls))}) Hit {hits} times! Lowered {target.name}'s defense by {hits}! Damage calculations: {', '.join(damage_calcs)}, Total = {total_damage}!"
            
        elif self.name == "Explosive Shot":
            damage, roll, formula = self.calculate_damage(user, target)
            target.take_damage(damage)
            recoil = damage // 3
            user.take_damage(recoil)
            return True, f"{user.name} used Explosive Shot! (Rolled {roll}) Damage calculation: {formula} = {damage}! Took {recoil} recoil damage!"
            
        elif self.name == "Sharpened Quake":
            if target.health < target.max_health // 2:
                self.power += 5  # Add bonus damage against low HP targets
            damage, roll, formula = self.calculate_damage(user, target)
            if target.health < target.max_health // 2:
                self.power -= 5  # Reset power
            target.take_damage(damage)
            return True, f"{user.name} used Sharpened Quake! (Rolled {roll}) Damage calculation: {formula} = {damage}!"
            
        return False, "Move failed!"

    def __str__(self):
        return f"{self.name} ({self.move_type.value}) - Power: d20 + {self.power}, Uses: {self.current_uses}/{self.max_uses}" 